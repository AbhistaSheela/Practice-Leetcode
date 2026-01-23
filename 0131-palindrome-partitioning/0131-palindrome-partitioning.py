class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def ispalindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        def bt(start):
            if start==len(s):
                res.append(path[:]) 
                return 
            for end in range(start,len(s)):
                if ispalindrome(start,end):
                    path.append(s[start:end+1])
                    bt(end+1)   
                    path.pop()
        bt(0)
        return res