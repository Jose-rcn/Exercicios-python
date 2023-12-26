from itertools import zip_longest
word1 = 'aceghiiii'
word2 = 'bdfiiiiiiiii'
class Solution:
    def mergeAlternately(word1: str, word2: str) -> str:
        # result = ''
        # larger = max(len(word1), len(word2))
        # for index in range(0, larger):
        #     try:
        #         result += word1[index]
        #     except IndexError:
        #         ...
        #     try:
        #         result += word2[index]
        #     except IndexError:
        #         ...
        # return result
        return "".join(a+b for a,b in zip_longest(word1,word2, fillvalue=""))
print(Solution.mergeAlternately(word1, word2))
