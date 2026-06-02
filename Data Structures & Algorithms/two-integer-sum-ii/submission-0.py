class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while target - numbers[right] != numbers[left]:
            if target - numbers[right] > numbers[left]:
                left += 1
            elif target - numbers[right] < numbers[left]:
                right -= 1
        return [left + 1, right + 1]