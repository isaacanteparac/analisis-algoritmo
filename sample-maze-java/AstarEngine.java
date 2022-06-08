import java.awt.Dimension;
import java.util.*;

public class AstarEngine extends AbstractSearchEngine {

    int f = 0; // coste total
    int g = 0; // pasos dados
    int h = 0; // heuristica(estimacion de lo que queda)
    private int escenario[][] = new int[20][1];// nodos a ser explorados

    Stack noExplorar = new Stack();// nodos a ser explorados
    List<String> yesExplordo = new ArrayList<String>();// nodos explorados

    public AstarEngine(int width, int height) {
        super(width, height);
        iterateSearch(startLoc, 1);
    }

    private void iterateSearch(Dimension loc, int depth) {
        if (isSearching == false)
            return;
        maze.setValue(loc.width, loc.height, (short) depth);
        Dimension[] moves = getPossibleMoves(loc);
        for (int i = 0; i < 4; i++) {
            if (moves[i] == null)
                break; // out of possible moves from this location
            searchPath[depth] = moves[i];
            if (equals(moves[i], goalLoc)) {
                System.out.println("Found the goal at " + moves[i].width + ", " + moves[i].height);
                isSearching = false;
                maxDepth = depth;
                return;
            } else {
                iterateSearch(moves[i], depth + 1);
                if (isSearching == false)
                    return;
            }
        }

        for(int width = 0; width < loc.width; width++){
            for (int height = 0; height < loc.height; height++){
                calcularNoExplorar(width, height, x, y)

            }
        }
        return;
    }

    public Dimension[] getPath() {
        Dimension[] ret = new Dimension[maxDepth];
        for (int i = 0; i < maxDepth; i++) {
            ret[i] = searchPath[i];
        }
        return ret;
    }

    void calcularNoExplorar(int width, int height, int x, int y) {
        for( int o = 0; o < this.escenario.length; o++){
            if(escenario[o][0] == 0 || escenario[o][1] == 0){
                if (x > 0) {
                    int izquierda = x-1;
                    this.escenario[o][0] = y;
                    this.escenario[o][1] = izquierda;
                    this.noExplorar.push(escenario[o]);
                }
                else if(x < (width-1)){
                    int derecha = x+1; 
                    this.escenario[o][0] = y;
                    this.escenario[o][1] = derecha;
                    this,noExplorar.push(escenario[o]);
                }
                else if(y > 0){
                    int arriba = y-1;
                    this.escenario[o][0] = arriba;
                    this.escenario[o][1] = x;
                    this.noExplorar.push(escenario[o]);
                }
                else if(y < (height-1)){
                    int abajo = y+1;
                    this.escenario[o][0] = abajo;
                    this.escenario[o][1] = x;
                    this.noExplorar.push(escenario[o]);
                }
            }
          
        }
       
    }

    public static void main(String[] args) {
        int escenario[][] = new int[20][2];// nodos a ser explorados
    

        for (int s = 0; s < escenario.length; s++) {
            System.out.println(s + "/" + escenario[s][0] + " " + escenario[s][1]);
        }
    }

}
