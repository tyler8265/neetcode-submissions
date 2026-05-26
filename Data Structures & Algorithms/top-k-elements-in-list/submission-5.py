class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}
        for num in nums:
            h_map[num] = h_map.get(num, 0) + 1
        arr = [(key, val) for key, val in h_map.items()]
        arr = sorted(arr, key=lambda x: x[1], reverse=True)
        final_arr = [tup[0] for tup in arr]
        return final_arr[:k]
