class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result=[]
        phone={
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def recall(i,curr):
            if i==len(digits):
                result.append(curr)
                return
            letters=phone[digits[i]]
            for letter in letters:
                recall(i+1,curr+letter)
        recall(0,"")
        return result