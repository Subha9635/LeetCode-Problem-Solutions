class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno",'7': "pqrs", '8': "tuv", '9': "wxyz"}

        ans = []

        def dfs(index: int, path: list[str]) -> None:
            if index == len(digits):
                ans.append(''.join(path))
                return
            for letter in digit_to_letters[digits[index]]:
                path.append(letter)
                dfs(index + 1, path)
                path.pop()

        dfs(0, [])
        return ans