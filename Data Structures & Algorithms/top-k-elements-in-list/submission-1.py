class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        
        switch_list = []
        for key, value in hash_map.items():
            switch_list.append([value, key])
        switch_list.sort()

        final_list = []
        while len(final_list) < k:
            freq = switch_list.pop()[1]
            final_list.append(freq)
        return final_list




        