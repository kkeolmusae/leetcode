class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for idx in range(n):
            nums1[idx + m] = nums2[idx]
        nums1.sort()
            
        