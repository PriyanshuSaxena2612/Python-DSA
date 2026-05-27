class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        max_index = {}
        count = 0
        for index, value in enumerate(word):
            if value.islower():
                max_index[value] = index
            else:
                if value not in max_index:
                    max_index[value] = index
        for char, max_idx in max_index.items():
            if char.islower():
                if char.upper() in max_index:
                    if max_index[char.upper()] > max_index[char]:
                        count += 1
        return count
