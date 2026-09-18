class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        f=[s.find(chr(97+i)) for i in range(26)]
        l=[s.rfind(chr(97+i)) for i in range(26)]
        a=[]

        for i in range(26):
            if f[i]<0: continue
            x,y=f[i],l[i]
            j=x
            while j<=y:
                c=ord(s[j])-97
                if f[c]<x: break
                y=max(y,l[c])
                j+=1
            else:
                a.append((y,x))

        a.sort()
        ans=[]
        end=-1

        for r,l in a:
            if l>end:
                ans.append(s[l:r+1])
                end=r

        return ans