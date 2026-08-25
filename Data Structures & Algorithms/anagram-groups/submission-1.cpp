class Solution {
public:
    bool isAnagram(string s, string t)
{
  map<char, int> smp;
  if (s.length() != t.length())
  {
    return false;
  }
  for (int i = 0; i < s.length(); i++)
  {
    if (smp.count(s[i]))
    {
      smp[s[i]] += 1;
    }
    else
    {
      smp[s[i]] = 1;
    }
  }
  for (int i = 0; i < t.length(); i++)
  {
    if (smp.count(t[i]))
    {
      smp[t[i]] -= 1;
    }
    else
    {
      return false;
    }
  }
  for (auto i : smp)
  {
    if (i.second != 0)
    {
      return false;
    }
  }
  return true;
}

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> gana;
  while (strs.size() > 0)
  {
    vector<string> gan = {strs[0]};
    vector<string> strs_copy = strs;
    int del_pointer = 0; 
    for (int j = 1; j < strs_copy.size(); j++)
    {
      if (isAnagram(strs_copy[0], strs_copy[j]))
      {
        gan.push_back(strs_copy[j]);
        strs.erase(strs.begin() + j - del_pointer);
        del_pointer ++; 
      }
    }
    gana.push_back(gan);
    strs.erase(strs.begin());
  }
  return gana;
    }
};
