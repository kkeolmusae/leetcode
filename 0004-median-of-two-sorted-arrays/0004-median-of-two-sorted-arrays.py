class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        
        a_idx = 0
        b_idx = 0
        a_len = len(nums1)
        b_len = len(nums2)
        while a_len > a_idx and b_len > b_idx:
            if nums1[a_idx] < nums2[b_idx]: 
              nums.append(nums1[a_idx])
              a_idx += 1 
            elif nums1[a_idx] > nums2[b_idx]: 
              nums.append(nums2[b_idx])
              b_idx += 1
            else:
              nums.append(nums1[a_idx])
              nums.append(nums2[b_idx])
              a_idx += 1
              b_idx += 1 
        
        if len(nums1[a_idx:]) != 0:
          nums = nums + nums1[a_idx:]
        elif len(nums2[b_idx:]) !=0:
          nums = nums + nums2[b_idx:]

        
        
        # 배열 길이가 짝수가 아니면 정중앙 값 리턴
        if len(nums) % 2 != 0:
            return float(nums[len(nums) // 2])
        else: 
            a_idx = len(nums) // 2
            return float((nums[a_idx - 1 ] + nums[a_idx]) / 2)
        