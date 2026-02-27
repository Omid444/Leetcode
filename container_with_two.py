class Solution:
    def maxArea(self, height: list[int]) -> int:
        first = 0
        last = len(height) - 1
        biggest_area = 0
        while first < last:
            y_axis = min(height[first],height[last])
            biggest_area = max(biggest_area, y_axis * (last - first))

            if height[first] < height[last]:
                first += 1
            else:
                last -= 1


        return biggest_area


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
