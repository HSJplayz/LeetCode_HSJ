class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d=dict(knowledge)
        ans=[]
        i=0
        while i<len(s):
            if s[i]=='(':
                i+=1
                key=""
                while s[i]!=')':
                    key+=s[i]
                    i+=1
                ans.append(d.get(key,"?"))
                i+=1
            else:
                ans.append(s[i])
                i+=1
        return "".join(ans)