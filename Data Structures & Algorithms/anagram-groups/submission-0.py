class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadict = defaultdict(list)

        for s in strs:
            character_list = [0] * 26

            for l in s:
                diff = ord(l) - ord("a")

                character_list[diff] += 1
            
            anadict[tuple(character_list)].append(s)
        
        final_list = list(anadict.values())
        return final_list
        

        