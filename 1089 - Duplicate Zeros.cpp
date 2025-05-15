class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int zeros = 0;
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] == 0){zeros++;}
        }
        int i = arr.size() - 1;
        while(i > -1){
            if(i + zeros < arr.size()){arr[i + zeros] = arr[i];}   
            if(arr[i] == 0){
                zeros--;
                if(i + zeros < arr.size()){arr[i + zeros] = arr[i];}
            }
            i--;
        }
    }
};