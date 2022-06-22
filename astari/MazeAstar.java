import java.util.*;

//Integrantes: Claire Daba e Isaac Antepara


public class MazeAstar {

    public static AstarEngine aStar(AstarEngine start, AstarEngine objetivo) {
        PriorityQueue<AstarEngine> closedList = new PriorityQueue<>();
        PriorityQueue<AstarEngine> openList = new PriorityQueue<>();

        start.f = start.g + start.calcularHeuristica(objetivo);
        openList.add(start);

        while (!openList.isEmpty()) {
            AstarEngine n = openList.peek();
            if (n == objetivo) {
                return n;
            }

            for (AstarEngine.Edge edge : n.vacinos) {
                AstarEngine m = edge.nodo;
                double totalpeso = n.g + edge.peso;

                if (!openList.contains(m) && !closedList.contains(m)) {
                    m.padre = n;
                    m.g = totalpeso;
                    m.f = m.g + m.calcularHeuristica(objetivo);
                    openList.add(m);
                } else {
                    if (totalpeso < m.g) {
                        m.padre = n;
                        m.g = totalpeso;
                        m.f = m.g + m.calcularHeuristica(objetivo);

                        if (closedList.contains(m)) {
                            closedList.remove(m);
                            openList.add(m);
                        }
                    }
                }
            }

            openList.remove(n);
            closedList.add(n);
        }
        return null;
    }

    public static void printPath(AstarEngine objetivo) {
        AstarEngine n = objetivo;

        if (n == null)
            return;

        List<Integer> ids = new ArrayList<>();

        while (n.padre != null) {
            ids.add(n.id);
            n = n.padre;
        }
        ids.add(n.id);
        Collections.reverse(ids);

        for (int id : ids) {
            System.out.print(id + " ");
        }
        System.out.println("");
    }

    public static void main(String[] args) {
        AstarEngine head = new AstarEngine(3);
        head.g = 0;

        AstarEngine n1 = new AstarEngine(2);
        AstarEngine n2 = new AstarEngine(2);
        AstarEngine n3 = new AstarEngine(2);

        head.addRama(1, n1);
        head.addRama(5, n2);
        head.addRama(2, n3);
        n3.addRama(1, n2);

        AstarEngine n4 = new AstarEngine(1);
        AstarEngine n5 = new AstarEngine(1);
        AstarEngine objetivo = new AstarEngine(0);

        n1.addRama(7, n4);
        n2.addRama(4, n5);
        n3.addRama(6, n4);

        n4.addRama(3, objetivo);
        n5.addRama(1, n4);
        n5.addRama(3, objetivo);

        AstarEngine res = aStar(head, objetivo);
        printPath(res);
    }

}

