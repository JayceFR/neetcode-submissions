class Solution {
public:
    bool canJump(vector<int>& nums) {
        int curr = 0; 
        int max_pos = 0; 
        while (curr < nums.size() && curr <= max_pos){
            max_pos = std::max(max_pos, nums[curr] + curr);
            curr += 1; 
        }
        return max_pos >= nums.size() - 1;
    }
};
