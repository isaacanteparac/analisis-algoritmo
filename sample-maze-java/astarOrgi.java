
//TITLE: DEFINICION DE VARIABLES

class AstarOri{
    int array_[] = new int[1];
    array = [
    [2,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,1,0,0,0,1,1],
    [1,1,0,1,1,1,0,1,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [1,0,1,0,1,0,0,0,0,0],
    [0,0,1,0]]
    int columna[];

    int fila[];
    void crearFilaColumna(int f, int c){
        columna = new int[c];
        fila = new int[f];
    }

    public static void main(String[] args) {
        crearFilaColumna(10,10);
    }


}
