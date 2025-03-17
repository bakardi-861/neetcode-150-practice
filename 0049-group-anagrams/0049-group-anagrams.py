class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group sorted letter combinations together in a hashmap
        s_map = defaultdict(list)
        for s in strs:
            s_map[tuple(sorted(s))].append(s)
        return [s_map[s] for s in s_map]