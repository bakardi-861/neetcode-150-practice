class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group by characters and counts of each char
        #strs = ["eat","tea","tan","ate","nat","bat"]                                i
        # {(e:1,a:1,t:1):["eat","tea","ate"],(t:1,a:1,n:1):["tan","nat"], (b:1,a:1,t:1):["bat"]}
            # [["eat","tea","ate"],["tan","nat"],["bat"]]
        ana_map = defaultdict(List[str])

        for s in strs:
            s_count = tuple(sorted(s)) #O(klogk)
            if s_count in ana_map:
                ana_map[s_count].append(s)
            else:
                ana_map[s_count] = [s]
        
        res = []
        for kv in ana_map:
            res.append(ana_map[kv])
        return res

