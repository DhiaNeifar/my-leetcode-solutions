int minDominoRotations(int* tops, int topsSize, int* bottoms, int bottomsSize) {
    int count_length = 6;
    int count[6];

    for(int i = 0; i < count_length; i++){
        count[i] = 0;
    }

    for(int i = 0; i < topsSize; i++){
        count[tops[i] - 1] ++;
        count[bottoms[i] - 1] ++; 
    }

    int trump = 0, max_count = 0;
    for(int i = 0; i < count_length; i++){
        if(max_count < count[i]){
            max_count = count[i];
            trump = i + 1;
        }
    }

    int tops_operations = 0;
    for(int i = 0; i < topsSize; i++){
        if(tops[i] != trump && bottoms[i] != trump){return -1;}
        if(tops[i] != trump && bottoms[i] == trump){tops_operations++;}
    }
    int bottoms_operations = 0;
    for(int i = 0; i < topsSize; i++){
        if(bottoms[i] != trump && tops[i] != trump){return -1;}
        if(bottoms[i] != trump && tops[i] == trump){bottoms_operations++;}
    }
    return (tops_operations < bottoms_operations) ? tops_operations : bottoms_operations;
    
}