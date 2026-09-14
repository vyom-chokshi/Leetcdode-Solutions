class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans=[]

        for i in s:
            if ans and i==ans[-1]:
                ans.pop()
            else:
                ans.append(i)

        sr=""

        for i in ans:
            sr+=i

        return sr