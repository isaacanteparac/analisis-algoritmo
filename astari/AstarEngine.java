import java.util.*;

//Integrantes: Claire Daba e Isaac Antepara

public class AstarEngine implements Comparable<AstarEngine> {
      // ID para facilitar la lectura de los resultados
      private static int idContador = 0;
      public int id;

      // padre en el camino
      public AstarEngine padre = null;

      public List<Edge> vacinos;

      // Funciones de evaluación
      public double f = Double.MAX_VALUE;
      public double g = Double.MAX_VALUE;

      // Heurística codificada
      public double h;

      AstarEngine(double h) {
            this.h = h;
            this.id = idContador++;
            this.vacinos = new ArrayList<>();
      }

      @Override
      public int compareTo(AstarEngine n) {
            return Double.compare(this.f, n.f);
      }

      public static class Edge {
            Edge(int peso, AstarEngine nodo) {
                  this.peso = peso;
                  this.nodo = nodo;
            }

            public int peso;
            public AstarEngine nodo;
      }

      public void addRama(int peso, AstarEngine nodo) {
            Edge newEdge = new Edge(peso, nodo);
            vacinos.add(newEdge);
      }

      public double calcularHeuristica(AstarEngine objetivo) {
            return this.h;
      }

}
