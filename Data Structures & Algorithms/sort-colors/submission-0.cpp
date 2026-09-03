#include <map>

class Solution {
public:
    void sortColors(vector<int>& nums) {
        map<int, int> bucket; 
        for (int i = 0; i <= 2; i++){
            bucket[i] = 0;
        }
        for (int i : nums){
            bucket[i]++;
        }
        int j = 0; 
        for (int i = 0; i < nums.size(); i++){
            while (bucket[j] == 0){
                j++;
            }
            nums[i] = j;
            bucket[j]--; 
        }
    }
};