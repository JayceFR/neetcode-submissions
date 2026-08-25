class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> smp;
  if (s.length() != t.length()){
    return false;
  }
  for (int i = 0; i < s.length(); i++){
    if (smp.count(s[i])){
      smp[s[i]] += 1;
    }
    else{
      smp[s[i]] = 1;
    }
  }
  for (int i = 0; i < t.length(); i++){
    if (smp.count(t[i])){
      smp[t[i]] -= 1;
    }
    else{
      return false;
    }
  }
  for (auto i : smp){
    if (i.second != 0){
      return false;
    }
  }
  return true;
    }
};
