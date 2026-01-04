class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_num = {}
        for index, num in enumerate(nums):
            second_number = target - num
            if second_number in seen_num:
                if second_number != num:
                    seen_num[num] = index
                    return [seen_num[second_number],seen_num[num]]
                else:
                    seen_num[num] = index +1
                    return []
            seen_num[num] = index





list_to_check = Solution()

result = list_to_check.twoSum([1,2,3,4,5,6,7,8],9)

print(result)