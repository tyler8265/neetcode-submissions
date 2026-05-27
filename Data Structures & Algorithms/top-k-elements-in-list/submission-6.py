class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}
        for num in nums:
            h_map[num] = h_map.get(num, 0) + 1
        buckets = [[] for num in nums]
        for num, count in h_map.items():
            buckets[count - 1].append(num)
        output = []
        for bucket in buckets:
            output.extend(bucket)
        return output[-k:]
