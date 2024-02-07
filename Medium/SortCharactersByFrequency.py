class Solution:
    def frequencySort(self, s: str) -> str:
        word_dict = {}
        for word in list(s):
            if word not in word_dict:
                word_dict[word] = 0
            word_dict[word] += 1
        sorted_dict = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
        answer = ''.join([item[0] * item[1] for item in sorted_dict])
        return answer
