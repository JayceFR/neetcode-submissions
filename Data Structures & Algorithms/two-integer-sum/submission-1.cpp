class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map <int, int> mp; 
  vector <int> return_vec; 
  int carry;
  for (int i = 0; i < nums.size(); i++){
    carry = target - nums[i];
    if (mp.count(nums[i])){
        return_vec.push_back(mp[nums[i]]);
      return_vec.push_back(i);
      return return_vec;
    }
    else{
      mp[carry] = i;
    }
  }
  return return_vec;
    }
};
