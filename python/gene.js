

box = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
       [0, 7, 0, 0, 4, 0, 0, 0, 0, 3, 0],
       [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

nchromosomes = []

start = box[3][1]
initialPosition = 0




function compass(n){
    var retVal;
    switch(n){
        case 1:
            retVal = "n";
            break;
        case 2:
            retVal = "s";
            break;
        case 3:
            retVal = "e";
            break;
        case 4:
            retVal = "o";
            break;
        case 5:
            retVal =  "ne";
            break;
        case 6:
            retVal = "no";
            break;
        case 7:
            retVal = "se";
            break;
        case 8:
            retVal = "so";
            break;
    };
    return retVal;
    /*if(n === 1){
        return "N"; }
    else if (n == 2){
        return "S";}
    elif (n == 3){
        return "E";}
    elif (n === 4){
        return "O"}
    elif (n === 5){
        return "NE"}
    elif (n === 6){
        return "NO";}
    elif (n === 7){
        return "SE";}
    elif (n === 8){
        return "SO";}
    else{
        return "ERROR"}*/
};


function randomGenerator(n){
    for(var i=0; i<10; i++){
        const numberR = Math.floor(Math.random() * (9 - 1) + 1);
        var orientation = compass(numberR);
        if(numberR <= 4){
            obj = {
                n_random: numberR,
                weight: 10,
                orientation
            }
        }
        else{
            obj = {
                n_random: numberR,
                weight: 15,
                orientation
            }
        }
        nchromosomes.push(obj);
    };
};


function chromosomeGenerator(){
    for(var c = 0; c < 6; c++){
        randomGenerator(c);
        console.log("------------------------"+c+"----------------------------\n");
        console.log("N-RANDOM > WEIGHT > ORIENTATION");
        console.log(nchromosomes);

    }
};
/*def thin():
    global nchromosomes
    #for i in range(len(nchromosomes)):*/
        


function main(){
    console.log("\nGITHUB @isaacanteparac\n");
    chromosomeGenerator();
};

main()
