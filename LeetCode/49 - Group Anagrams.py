class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for n in strs:
            key = "".join(sorted(n))
            freq[key].append(n)
        return list(freq.values())
