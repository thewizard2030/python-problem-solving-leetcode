class Solution:
    def romanToInt(self, s: str) -> int:
        romandis = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romandis[s[i]] < romandis[s[i + 1]]:
                num -= romandis[s[i]]
            else:
                num += romandis[s[i]]
        return num
