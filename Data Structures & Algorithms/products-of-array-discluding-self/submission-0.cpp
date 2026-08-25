class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
  vector<int> return_vec;
  int count = 1, after_count = 1;
  for (int i = 0; i < nums.size(); i++) {
    return_vec.push_back(count);
    count = count * nums[i];
  }
  for (int i = return_vec.size() - 1; i >= 0; i--) {
    return_vec[i] = return_vec[i] * after_count;
    after_count = after_count * nums[i];
  }
  return return_vec;

    }
};
