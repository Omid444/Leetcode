class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        temp_list = []
        nums_copy = nums.copy()
        for index,num in enumerate(nums):
            if num == 0:
                if -1 * nums[(index+1)] in nums:
                    temp_list.append(0)
                    temp_list.append(nums[index+1])
                    temp_list.append(-1 * nums[index+1])
                    if temp_list:
                        result.append(tuple(sorted(temp_list[:])))
                    temp_list.clear()

            if num % 2 != 0:
                if -1 * num in nums_copy and 0 in nums_copy:
                    temp_list.append(0)
                    temp_list.append(-1 * num)
                    temp_list.append(num)
                    if temp_list:
                        result.append(tuple(sorted(temp_list[:])))
                    temp_list.clear()

            else:
                if -(1/2) * num in nums_copy:
                    nums_copy.remove(int(-(1/2) * num))
                    if -(1/2) * num in nums_copy:
                        temp_list.append(num)
                        temp_list.append(int(-(1/2) * num))
                        temp_list.append(int(-(1/2) * num))
                        if temp_list:
                            result.append(tuple(sorted(temp_list[:])))
                        temp_list.clear()



        return list(set(result))


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))


