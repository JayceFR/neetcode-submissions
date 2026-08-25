class Solution {
public:

    string encode(vector<string>& strs) {
          string encoded = "";
  for (auto &i: strs){
    encoded += to_string(i.length()) + "#" + i;
  }
  return encoded;
    }

    vector<string> decode(string s) {
          vector<string> stuff; 
  while(s.length() > 0){
    int hash_pos = s.find_first_of('#');
    int length_of_string_ahead = stoi(s.substr(0, hash_pos));
    string substr = s.substr(hash_pos + 1, length_of_string_ahead);
    stuff.push_back(substr);
    for (int x = 0; x <= hash_pos + length_of_string_ahead; x++){
      s.erase(s.begin());
    }
  }
  return stuff;
    }
};
