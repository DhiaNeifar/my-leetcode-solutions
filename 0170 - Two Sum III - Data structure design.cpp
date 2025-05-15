class TwoSum {

private:
    unordered_set<int> numbers;
    unordered_set<int> sums;

public:
    TwoSum() {
    }
    
    void add(int number) {
        for(auto& num: numbers)
            sums.insert(num + number);
        numbers.insert(number);
    }
    
    bool find(int value) {
        if(sums.contains(value))
            return true;
        return false;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */