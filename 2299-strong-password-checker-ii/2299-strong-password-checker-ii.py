class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        specials="!@#$%^&*()-+"
        if len(password)<8:
            return False
        for i in range(len(password)):
            if i<len(password)-1:
                if password[i]==password[i+1]:
                    return False
            ch=password[i]
            if ch.islower():
                has_lower=True
            if ch.isupper():
                has_upper=True
            if ch.isdigit():
                has_digit=True
            if ch in specials:
                has_special=True

        return has_upper and has_lower and has_digit and has_special  