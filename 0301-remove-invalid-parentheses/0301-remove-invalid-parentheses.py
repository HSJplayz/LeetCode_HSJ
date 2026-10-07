class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string):
            count=0
            for ch in string:
                if ch=='(':
                    count+=1
                elif ch==')':
                    count-=1
                    if count<0:
                        return False
            return count==0
        queue=deque([s])
        visited={s}
        while queue:
            level_size=len(queue)
            result=[]
            for _ in range(level_size):
                current=queue.popleft()
                if isValid(current):
                    result.append(current)
                if result:
                    continue
                for i in range(len(current)):
                    if current[i] not in "()":
                        continue
                    
                    if i>0 and current[i]==current[i-1]:
                        continue
                    new_string=current[:i]+current[i+1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)
            if result:
                return result
        return[""]

