class Solution {
public:
    int maxNumberOfBalloons(string text) {
        
        // Construct array for balloon.
        int balloon[5] = {0};
        // Letter b
        balloon[0] = 1;
        // Letter a
        balloon[1] = 1;
        // Letter l
        balloon[2] = 2;
        // Letter o
        balloon[3] = 2;
        // Letter n
        balloon[4] = 1;
        
        // Construct array to count for letters [b, a, l, o, n]
        int arr[5] = {0};
        for(auto& s: text){
            if(s == 'b')
                arr[0]++;     
            if(s == 'a')
                arr[1]++;     
            if(s == 'l')
                arr[2]++;     
            if(s == 'o')
                arr[3]++;     
            if(s == 'n')
                arr[4]++;     
        }
        // Find lowest div
        int result = arr[0] / balloon[0];
        for(int i = 1; i < 5; i++){
            result = min(result, arr[i] / balloon[i]);
        }
        return result;
    }
};