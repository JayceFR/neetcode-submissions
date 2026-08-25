class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
  unordered_set<char> square[3][3];
  unordered_set<char> row[9];
  unordered_set<char> column[9];
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
        if (board[i][j] != '.'){
            if (column[j].count(board[i][j]) > 0) {
        cout << "column problem" << "\n";
        return false;
      }
      column[j].insert(board[i][j]);
      if (row[i].count(board[i][j]) > 0) {
        cout << "row problem " << i << "\n";
        return false;
      }
      row[i].insert(board[i][j]);
      if (square[i / 3][j / 3].count(board[i][j]) > 0) {
        cout << "square problem" << "\n";
        return false;
      }
      square[i / 3][j / 3].insert(board[i][j]);


        }
      
    }
  }
  return true;


    }
};
