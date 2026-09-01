struct state
{
    int row;
    int col;
    int energy;
    int mask;
};

class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) 
    {
        int r = classroom.size();
        int c = classroom[0].size();

        int rs, cs;

    
        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
            {
                if(classroom[i][j] == 'S')
                {
                    rs = i;
                    cs = j;
                }
            }
        }

        
        int litterCount = 0;

        vector<vector<int>> litterId(r, vector<int>(c, -1));

        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
            {
                if(classroom[i][j] == 'L')
                {
                    litterId[i][j] = litterCount;
                    litterCount++;
                }
            }
        }

        
        if(litterCount == 0)
            return 0;

        
        int allMask = (1 << litterCount) - 1;

        queue<state> q;

        state start;
        start.row = rs;
        start.col = cs;
        start.energy = energy;
        start.mask = 0;

        q.push(start);

        // visited[row][col][energy][mask]
        vector<vector<vector<vector<bool>>>> visited(
            r,
            vector<vector<vector<bool>>>(
                c,
                vector<vector<bool>>(
                    energy + 1,
                    vector<bool>(1 << litterCount, false)
                )
            )
        );

        visited[rs][cs][energy][0] = true;

        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        int moves = 0;

        while(!q.empty())
        {
            int size = q.size();

            
            while(size--)
            {
                state curr = q.front();
                q.pop();

                int row = curr.row;
                int col = curr.col;
                int en = curr.energy;
                int mask = curr.mask;

                
                for(int k = 0; k < 4; k++)
                {
                    int nr = row + dr[k];
                    int nc = col + dc[k];

                    
                    if(nr < 0 || nr >= r || nc < 0 || nc >= c)
                        continue;

                    
                    if(classroom[nr][nc] == 'X')
                        continue;

                
                    if(en == 0)
                        continue;

                    
                    int newEnergy = en - 1;

                    
                    if(classroom[nr][nc] == 'R')
                        newEnergy = energy;

                    
                    int newMask = mask;

            
                    if(classroom[nr][nc] == 'L')
                    {
                        int id = litterId[nr][nc];

                        newMask = mask | (1 << id);
                    }

                    
                    if(newMask == allMask)
                        return moves + 1;

                    
                    if(!visited[nr][nc][newEnergy][newMask])
                    {
                        visited[nr][nc][newEnergy][newMask] = true;

                        q.push({
                            nr,
                            nc,
                            newEnergy,
                            newMask
                        });
                    }
                }
            }

            moves++;
        }

        return -1;
    }
};