class Solution:

    def twoSum(self, nums:list[int], target:int)->list[int]:
        length = len(nums)
        dic = {}
        for i in range(length):
            dic[int(nums[i])] = i

        for i in range(length):
            pair = target - int(nums[i])
            if pair in dic and i != dic[pair]:
                return [i, dic[pair]]

        return []


if __name__ == '__main__':
    nums = input().split(',')
    target = int(input())
    solution = Solution()
    print(solution.twoSum(list(nums), target))