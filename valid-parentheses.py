class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'{' : '}', '[' : ']', '(' : ')'}

        stacked_brackets = []

        for bracket in s:
            #check if open
            if bracket in brackets:
                stacked_brackets.append(bracket)
            elif len(stacked_brackets) == 0 or bracket != brackets[stacked_brackets.pop()]:
                return False

        if len(stacked_brackets) == 0:
            return True
        else:
            return False
