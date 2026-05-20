class Solution:
    def Duplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False


nums = list(map(int, input("Enter numbers: ").split()))

obj = Solution()
print(obj.Duplicate(nums))
