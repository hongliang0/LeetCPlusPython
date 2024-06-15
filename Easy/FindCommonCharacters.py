class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        my_dict = {}
        for i in range(len(words[0])):
            if not words[0][i] in my_dict:
                my_dict[words[0][i]] = 0
            my_dict[words[0][i]] += 1
        for word in range(1, len(words)):
            valid_dict = my_dict.copy()
            new_dict = {}
            for i in range(len(words[word])):
                if words[word][i] not in valid_dict:
                    continue
                elif words[word][i] not in new_dict:
                    new_dict[words[word][i]] = 0
                if valid_dict[words[word][i]] > new_dict[words[word][i]]:
                    new_dict[words[word][i]] += 1
            # print(new_dict)
            my_dict = new_dict
        answer = []
        # print(my_dict)
        for word in my_dict:
            for i in range(my_dict[word]):
                answer.append(word)
        return answer
