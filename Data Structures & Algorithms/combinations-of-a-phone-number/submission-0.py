class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        need to generate permutations
        '''
        if not digits:
            return []
        charMap = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        result = []
        len_d = len(digits)
        def backtrack(index, curr):
            if len(curr) == len_d:
                result.append(curr)
                return
            for i in charMap[int(digits[index])]:
                backtrack(index+1, curr + i)
        backtrack(0, "")
        return result


            