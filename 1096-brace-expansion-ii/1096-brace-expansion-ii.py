class Solution:
    def braceExpansionII(self, expression: str):
        
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == ',':
               
                    result.update(current)
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    i += 1

                    temp, i = parse(i)

                    
                    next_set = set()

                    for a in current:
                        for b in temp:
                            next_set.add(a + b)

                    current = next_set

                else:
                    # Lowercase letter
                    ch = expression[i]

                    next_set = set()

                    for word in current:
                        next_set.add(word + ch)

                    current = next_set

                    i += 1

            
            result.update(current)

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        ans, _ = parse(0)

        return sorted(ans)