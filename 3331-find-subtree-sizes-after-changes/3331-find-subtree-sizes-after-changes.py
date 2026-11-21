class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(parent)
        adj=[[] for _ in range(n)]
        for i in range(1,n):
            adj[parent[i]].append(i)
        new=[-1]*n
        last={}
        def dfs(node):
            c=s[node]
            p=last.get(c,-1)
            new[node]=p if p != -1 else parent[node]
            last[c]=node
            for child in adj[node]:
                dfs(child)
            if p==-1:
                del last[c]
            else:
                last[c]=p
        dfs(0)
        adj=[[] for _ in range(n)]
        for i in range(1,n):
            adj[new[i]].append(i)
        ans=[1]*n
        def calc(node):
            for child in adj[node]:
                ans[node]+=calc(child)
            return ans[node]
        calc(0)
        return ans