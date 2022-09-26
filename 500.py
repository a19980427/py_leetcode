class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        line1 = set('qwertyuiop')
        line2 = set('asdfghjkl')
        line3 = set('zxcvbnm')

        res = []

        for word in words:
            word = word.encode('utf-8')
            lower_word = str.lower(word)
            line = None
            for i in range(len(lower_word)):
                if i == 0:
                    if lower_word[i] in line1:
                        line = line1
                    if lower_word[i] in line2:
                        line = line2
                    if lower_word[i] in line3:
                        line = line3
                if lower_word[i] not in line:
                    break
                if i == len(lower_word) - 1:
                    res.append(word)
        return res


