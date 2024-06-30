class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        oldx = x
        newx = 0
        while x != 0:
            newx = newx * 10 + (x % 10)
            x //= 10

        return oldx == newx


if __name__ == '__main__':
    x = int(input())
    solution = Solution()
    print(solution.isPalindrome(x))