class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        first = {}
        last = {}

        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i

        candidates = []

        i = 0

        while i < len(s):

            ch = s[i]


            if first[ch] != i:
                i += 1
                continue

            j = i
            r = last[ch]
            f = True

        
            while j <= r:

                current = s[j]

                
                if first[current] < i:
                    f = False
                    break

                
                if last[current] > r:
                    r = last[current]

                j += 1

            if f:
                candidates.append((i, r))

            i += 1

        
        candidates.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in candidates:

            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans