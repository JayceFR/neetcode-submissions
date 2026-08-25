class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
          map<int, int> frequency; 
  for (auto &i : nums){
    if(frequency.count(i)){
      frequency[i] ++;
    }
    else{
      frequency[i] = 0;
    }
  }
  vector<int> bucket[nums.size()]; 
  vector<int> ret_nums;
  for (auto &i : frequency){
    bucket[i.second].push_back(i.first);
  }
  int start = nums.size() - 1;
  while(k){
    vector<int> numbers = bucket[start];
    for (auto &i : numbers){
      if (k > 0){
        ret_nums.push_back(i);
        k--;
      }
    }
    start --; 
  } 
  return ret_nums;
    }
};
