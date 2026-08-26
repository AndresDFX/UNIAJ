'use strict';
/**
 * Simulacro de las APIs de Google Apps Script que usa el .gs de encuentros.
 *
 * No pretende ser fiel a Google en todo: pretende ser fiel en lo que el script depende, y
 * poder torcer a proposito las partes dudosas (que `search` no encuentre, que la sala de Meet
 * venga "pending", que deleteEvent falle) para ver como se porta el script.
 */

let SEQ = 0;

class Guest {
  constructor(email) { this.email = email; }
  getEmail() { return this.email; }
}

class FakeEvent {
  constructor(cal, title, start, end, opts) {
    this.cal = cal;
    this.title = title;
    this.start = start;
    this.end = end;
    this.description = (opts && opts.description) || '';
    this.location = '';
    this.guests = [];
    this.id = 'ev' + (++SEQ);
    this.deleted = false;
    this.conferenceData = null;
    // trazas para las aserciones
    this.invitacionesEnviadas = 0;
    this.cancelacionEnviada = false;
    this.notificacionesDeUpdate = 0;
    if (opts && opts.guests) {
      String(opts.guests).split(',').filter(Boolean).forEach((g) => this.guests.push(new Guest(g)));
      if (opts.sendInvites) this.invitacionesEnviadas += this.guests.length;
    }
  }
  getTitle() { return this.title; }
  getId() { return this.id + '@google.com'; }
  getStartTime() { return this.start; }
  getEndTime() { return this.end; }
  getLocation() { return this.location; }
  setLocation(v) { this.cal.escrituras++; this.location = v; return this; }
  getDescription() { return this.description; }
  setDescription(v) { this.cal.escrituras++; this.description = v; return this; }
  getGuestList() { return this.guests.slice(); }
  addGuest(email) {
    if (this.cal.fallarAddGuest) throw new Error('cuota agotada (simulado)');
    this.guests.push(new Guest(email));
    this.invitacionesEnviadas++;
    return this;
  }
  deleteEvent() {
    if (this.cal.fallarDelete) throw new Error('no se pudo borrar (simulado)');
    this.deleted = true;
    if (this.guests.length) this.cancelacionEnviada = true;
    this.cal.eventos = this.cal.eventos.filter((e) => e !== this);
    this.cal.borrados.push(this);
  }
}

class FakeCalendar {
  constructor(id, name) {
    this.id = id;
    this.name = name;
    this.eventos = [];
    this.borrados = [];
    this.escrituras = 0;
    // interruptores para torcer el simulacro
    this.searchInutil = false;     // `search` no encuentra nada (como si Google no indexara)
    this.fallarDelete = false;
    this.fallarAddGuest = false;
  }
  getId() { return this.id; }
  getName() { return this.name; }
  createEvent(title, start, end, opts) {
    const e = new FakeEvent(this, title, start, end, opts);
    this.eventos.push(e);
    return e;
  }
  getEvents(from, to, opts) {
    let out = this.eventos.filter((e) => e.start >= from && e.start <= to);
    if (opts && opts.search) {
      if (this.searchInutil) return [];
      const q = String(opts.search).toLowerCase();
      out = out.filter((e) => e.title.toLowerCase().indexOf(q) !== -1);
    }
    return out;
  }
  /** Solo para el arnes: planta un evento sin pasar por createEvent. */
  plantar(title, start, end, guests) {
    const e = new FakeEvent(this, title, start, end, { guests: (guests || []).join(',') });
    this.eventos.push(e);
    return e;
  }
  porId(idApi) { return this.eventos.find((e) => e.id === idApi); }
}

function construir(opciones) {
  const o = opciones || {};
  const cal = new FakeCalendar(o.calendarId || 'clases@uniajc.edu.co', 'Clases UNIAJC');
  const otro = new FakeCalendar('otro@uniajc.edu.co', 'Personal');
  const log = [];

  // Cuantos ciclos de "pending" devuelve Meet antes de dar la URL. 0 = inmediato.
  let pendientes = o.meetPendiente || 0;
  let salas = 0;
  const salasPorRequestId = new Map();

  const api = {
    Events: {
      patch(resource, calendarId, eventId, params) {
        const ev = cal.porId(eventId);
        if (!ev) throw new Error('no existe el evento ' + eventId);
        if (resource.conferenceData && resource.conferenceData.createRequest) {
          const rid = resource.conferenceData.createRequest.requestId;
          if (o.fallarMeet) throw new Error('Meet no disponible (simulado)');
          // Google es idempotente por requestId: el mismo rid devuelve la MISMA sala.
          let uri = salasPorRequestId.get(rid);
          if (!uri) {
            salas++;
            uri = 'https://meet.google.com/sala-' + salas;
            salasPorRequestId.set(rid, uri);
          }
          ev.conferenceData = {
            conferenceId: uri.split('/').pop(),
            entryPoints: [{ entryPointType: 'video', uri }],
          };
          if (params && params.sendUpdates === 'all') ev.notificacionesDeUpdate++;
          // Si simulamos "pending", la respuesta del patch no trae entryPoints todavia.
          if (pendientes > 0) { pendientes--; return { conferenceData: { entryPoints: [] } }; }
          return { conferenceData: ev.conferenceData };
        }
        return {};
      },
      get(calendarId, eventId) {
        const ev = cal.porId(eventId);
        if (!ev) throw new Error('no existe el evento ' + eventId);
        return { conferenceData: ev.conferenceData };
      },
    },
  };

  const sandbox = {
    // Zona del PROYECTO Apps Script: es la que usa `new Date(y,m,d,h,min)`.
    // Se puede torcer (opciones.zona) para probar el guardia de zona horaria.
    Session: { getScriptTimeZone: () => (o.zona || 'America/Bogota') },
    CalendarApp: {
      getCalendarById: (id) => (id === cal.id ? cal : (id === otro.id ? otro : null)),
      getDefaultCalendar: () => otro,
      getAllCalendars: () => [cal, otro],
    },
    Calendar: o.sinServicioAvanzado ? undefined : api,
    Logger: { log: (m) => log.push(String(m)) },
    Utilities: { sleep: () => { /* el arnes no duerme */ } },
    PropertiesService: {
      getScriptProperties: () => ({
        getProperty: () => null, setProperty: () => {}, deleteProperty: () => {},
      }),
    },
    Date, String, Number, Math, JSON, Array, Object, Error, isNaN, parseInt,
  };
  sandbox.console = console;
  return { cal, otro, log, sandbox, salasCreadas: () => salas };
}

module.exports = { construir };
