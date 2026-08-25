class Solution{
    public:
        int maxRs;
        int maxCs; 
        void islandsAndTreasure(vector<vector<int>>& grid) {
            deque<pair<int, int>> dq;

            set<pair<int, int>> visited; 

            maxRs = grid.size();
            maxCs = grid[0].size();

            // Get all locs of 0s from the grid. 
            for (int r = 0; r < maxRs; r++)
            {
                for (int c = 0; c < maxCs; c++)
                {
                    if (grid[r][c] == 0)
                    {
                        dq.push_back({r,c});
                        visited.insert({r,c});
                    }
                }
            }

            int dist = 0; 
            while (!dq.empty())
            {
                int n = dq.size();
                for (int i = 0; i < n; i++){
                    pair<int, int> p = dq.front();
                    dq.pop_front();
                    grid[p.first][p.second] = dist; 
                    int r = p.first;
                    int c = p.second;
                    
                    addToQueue(r+1, c, dq, visited, grid);
                    addToQueue(r-1, c, dq, visited, grid);
                    addToQueue(r, c+1, dq, visited, grid);
                    addToQueue(r, c-1, dq, visited, grid);
                    
                }
                dist ++; 
            }
        }

        void addToQueue(int r, int c, deque<pair<int, int>>& q, set<pair<int, int>> &visited, vector<vector<int>>& grid){
            if (min(r,c) < 0 || r == maxRs || c == maxCs || visited.find({r,c}) != visited.end() || grid[r][c] == -1){
                return;
            }  
            visited.insert({r, c});
            q.push_back({r,c});
        }
};