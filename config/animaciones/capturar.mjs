/**
 * Captura los fotogramas de una animacion canvas del motor de Agente Habilon, con la marca UNIAJC.
 *
 *     node config/animaciones/capturar.mjs <modulo.js> "<texto>" <carpeta-salida> [fotogramas] [ancho alto]
 *
 * Reutiliza tal cual el lienzo (`lienzo.js`), el anfitrion (`animador.js`) y el navegador headless
 * (`src/pruebas/navegador.js`) de Habilon: aqui solo se pone la marca de la universidad y se recorre
 * `t` de 0 a 1 capturando la caja exacta. Los PNG los junta en GIF `gif.py`.
 *
 * El motor vive fuera de este repo; su ruta se toma de HABILON_MVP o del valor por omision.
 */
import { createServer } from 'node:http'
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs'
import { join, basename, extname, dirname } from 'node:path'
import { pathToFileURL } from 'node:url'

const MVP = process.env.HABILON_MVP || 'C:/Projects/Vivetori/Agente Habilon/mvp'
const ANIM = join(MVP, 'bibliotecas', 'base', 'animaciones')
const [MODULO, TEXTO = '', SALIDA, N = '36', ANCHO = '800', ALTO = '640'] = process.argv.slice(2)
if (!MODULO || !SALIDA) { console.log('uso: <modulo.js> "<texto>" <salida> [fotogramas] [ancho alto]'); process.exit(2) }
const huella = basename(MODULO, '.js')
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;')

// La marca de la UNIAJC: los mismos colores que `uniajc_slides_engine.py` (NAVY, CIAN, AMARILLO…).
const MARCA = `:root{--marca-accion:#095292;--marca-acento:#269CCB;--marca-cian:#269CCB;
--marca-verde:#1B7A4E;--marca-sello:#FFD000;--marca-malva:#A02030;--marca-gris:#666666;
--tinta:#333333;--papel:#FFFFFF;--fondo:#FFFFFF;--borde:#C9D6E2}
html,body{margin:0;padding:0;background:#fff;font-family:'Segoe UI',Calibri,Arial,sans-serif}`

const pagina = `<!doctype html><html lang="es"><head><meta charset="utf-8"><style>${MARCA}</style></head>
<body><div id="caja" data-fp-animacion="${huella}" data-fp-texto="${esc(TEXTO)}"
style="width:${ANCHO}px;height:${ALTO}px;overflow:hidden;font-family:'Segoe UI',Calibri,Arial,sans-serif"></div>
<script>window.matchMedia=function(q){return{matches:false,addListener(){},removeListener(){}}}</script>
<script src="/lienzo.js"></script><script src="/animador.js"></script><script src="/base.js"></script><script src="/modulo.js"></script>
</body></html>`

const srv = createServer((q, r) => {
  const ruta = (q.url || '/').split('?')[0]
  const f = ruta === '/lienzo.js' ? join(ANIM, 'lienzo.js') : ruta === '/animador.js' ? join(ANIM, 'animador.js')
    : ruta === '/modulo.js' ? MODULO
    // `_base.js` de la misma carpeta: las piezas comunes (caja, tabla, codigo) de un curso.
    : ruta === '/base.js' ? join(dirname(MODULO), '_base.js') : null
  if (!f) { r.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); r.end(pagina); return }
  if (!existsSync(f)) { r.writeHead(200, { 'content-type': 'text/javascript' }); r.end(''); return }
  r.writeHead(200, { 'content-type': extname(f) === '.js' ? 'text/javascript' : 'application/octet-stream' })
  r.end(readFileSync(f))
})
await new Promise((ok) => srv.listen(0, '127.0.0.1', ok))
const { abrirNavegador } = await import(pathToFileURL(join(MVP, 'src', 'pruebas', 'navegador.js')).href)
const espera = (ms) => new Promise((r) => setTimeout(r, ms))
const nav = await abrirNavegador(`http://127.0.0.1:${srv.address().port}/`, { ancho: Number(ANCHO) + 40, alto: Number(ALTO) + 240 })
await espera(1200)
const ok = await nav.evaluar(`!!FP_ANIMADOR.estado('${huella}')`)
if (!ok) { console.error('el modulo no se monto:', nav.errores()); await nav.cerrar(); srv.close(); process.exit(1) }
mkdirSync(SALIDA, { recursive: true })
const n = Number(N)
for (let i = 0; i < n; i++) {
  const t = n === 1 ? 1 : i / (n - 1)
  await nav.evaluar(`FP_ANIMADOR.saltar('${huella}', ${t})`)
  await espera(60)
  const { data } = await nav.cdp('Page.captureScreenshot', {
    format: 'png', clip: { x: 0, y: 0, width: Number(ANCHO), height: Number(ALTO), scale: 1 } })
  writeFileSync(join(SALIDA, `f${String(i).padStart(3, '0')}.png`), Buffer.from(data, 'base64'))
}
const errores = nav.errores()
await nav.cerrar(); srv.close()
if (errores.length) { console.error('errores en consola:', errores); process.exit(1) }
console.log(`${n} fotogramas -> ${SALIDA}`)
