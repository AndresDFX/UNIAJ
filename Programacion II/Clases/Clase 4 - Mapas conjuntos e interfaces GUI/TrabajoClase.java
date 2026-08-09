/*
Welcome to JDoodle!

You can execute code here in 110+ languages. Right now you’re in the Java IDE.

  1. Click the orange Execute button ▶ to execute the sample code below and see how it works.

  2. Want help writing or debugging code? Type a query into JDroid on the right hand side ---------------->

  3.Try the menu buttons on the left. Save your file, share code with friends and open saved projects.

Want to change languages? Try the search bar up the top.
*/

import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;
import java.util.LinkedList;

public class MyClass {
  public static void main(String args[]) {
      
      Integer x = 2;
      ArrayList <Integer> miLista = new ArrayList<>();
      
      // FORMA DE AGREGAR UNO A UNO
      miLista.add(2);
      miLista.add(5);
      
      // FORMA DE AGREGAR VARIOS A LA VEZ
      Collections.addAll(miLista, 2, 5, 7, 8);
      //System.out.println(miLista);
      
      // PILAS
      Stack <Integer> miPila = new Stack<>();
      miPila.push(2);
      miPila.push(5);
      //Collections,
      //int y = miPila.pop(); // [2]
      //miPila.pop();          // [ ]
      //System.out.println(miPila);
      //System.out.println(miPila.isEmpty());
      //System.out.println(miPila.peek());
      
      
      // COLAS
      LinkedList <Integer> queue = new LinkedList<>();
      queue.offer(2);
      queue.offer(5);
      
      System.out.println(queue.peek()); // Mostrar
      System.out.println(queue.poll()); // Atender al primero de la Cola
      
      
      // 
      
      // 
      
      
      
      
      
      
      
    
  }
}