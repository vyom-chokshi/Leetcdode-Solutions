class Solution {
public:
    struct state
    {
        int a;
        int b;    
    };

    bool canMeasureWater(int x, int y, int target) 
    {
        if(target > x + y)
            return false;

        queue<state> open;
        set<pair<int,int>>visited;
        state start={0,0};
        visited.insert({0,0});
        open.push(start);

        while(!open.empty())
    {
        state current=open.front();
        open.pop();

        if(current.a==target || current.b==target || current.a+current.b == target)
        {
            
            return true;
        }
        state next;

        next.a=x;
        next.b=current.b;
        if(visited.find({next.a,next.b})==visited.end())
        {
            visited.insert({next.a,next.b});
           
            open.push(next);
        }

        next.a=current.a;
        next.b=y;
        if(visited.find({next.a,next.b})==visited.end())
        {
            visited.insert({next.a,next.b});
           
            open.push(next);
        }

        next.a=0;
        next.b=current.b;
        if(visited.find({next.a,next.b})==visited.end())
        {
            visited.insert({next.a,next.b});
            
            open.push(next);
        }

        next.a=current.a;
        next.b=0;
        if(visited.find({next.a,next.b})==visited.end())
        {
            visited.insert({next.a,next.b});
            
            open.push(next);
        }

        
        int a1=min(current.a,y-current.b);
        next.a=current.a-a1;
        next.b=current.b+a1;
        if(visited.find({next.a,next.b})==visited.end())
        {
            visited.insert({next.a,next.b});
           
            open.push(next);
        }
        

        int x1=min(current.b,x-current.a);
        next.a=current.a+x1;
        next.b=current.b-x1;
        if(visited.find({next.a,next.b})==visited.end())
        {
            visited.insert({next.a,next.b});
            
            open.push(next);
        }
        
    }
    return false;


    }
};