class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)     
    
        last = [-1] * m
        w1_idx = n - 1
        
        for w2_idx in range(m - 1, -1, -1):
            while w1_idx >= 0 and word1[w1_idx] != word2[w2_idx]:
                w1_idx -= 1
            if w1_idx >= 0:
                last[w2_idx] = w1_idx
                w1_idx -= 1
            else:
                break

        ans = []
        w2_idx = 0
        changed = False
        
        for w1_idx in range(n):
            if w2_idx == m:
                break
                
            if word1[w1_idx] == word2[w2_idx]:
                ans.append(w1_idx)
                w2_idx += 1
            elif not changed and (w2_idx == m - 1 or w1_idx < last[w2_idx + 1]):
                ans.append(w1_idx)
                w2_idx += 1
                changed = True
                
        return ans if len(ans) == m else []
