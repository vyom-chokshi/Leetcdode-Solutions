class Solution:
    def minimumPushes(self, word: str) -> int:
        ans=0
        seen={}
        for i in word:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        arr=[]
        for i in seen:
            arr.append(seen[i])
        arr.sort(reverse=True)
        for i in range(len(arr)):
            ans+=arr[i]*(i//8+1)
        return ans