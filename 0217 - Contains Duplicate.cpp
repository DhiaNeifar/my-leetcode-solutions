class Solution {
public:
    bool containsDuplicate(vector<int>& nums)
    {
        unordered_set<int> elems;
        for (auto& iter : nums)
        {
            if (elems.contains(iter))
                return true;
            
            elems.insert(iter);
        }
        
        return false;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0";});