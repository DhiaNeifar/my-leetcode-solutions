int numberOfSteps(int num) {
    int operations = 0;
    while(num){
        if(num % 2){num--;}
        else{num /= 2;}
        operations++;
    }
    return operations;
}