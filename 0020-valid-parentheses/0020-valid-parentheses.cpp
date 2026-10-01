class Solution {
public:
    bool isValid(string s) {
    stack<char> c;
    
    for(char ch:s)
    {
        if(ch=='('||ch=='['||ch=='{')
        c.push(ch);
        else
        {
            if(c.empty())
            {
                
                return false;
            }
        else if(ch==')' && c.top()=='(')
        {
            c.pop();
        }
        else if(ch==']' && c.top()=='[')
        {
            c.pop();
        }
        else if(ch=='}' && c.top()=='{')
        {
            c.pop();
        }
        else
        {
            
            return false;
        }
     }
    }
    return c.empty();
    }
};