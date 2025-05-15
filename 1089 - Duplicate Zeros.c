void duplicateZeros(int* arr, int arrSize) {
    int zeros = 0;
    for(int i = 0; i < arrSize; i++){
        if(arr[i] == 0){zeros++;}
    }
    int i = arrSize - 1;
    while(i > -1){
        if(i + zeros < arrSize){arr[i + zeros] = arr[i];}   
        if(arr[i] == 0){
            zeros--;
            if(i + zeros < arrSize){arr[i + zeros] = arr[i];}
        }
        i--;
    }
}