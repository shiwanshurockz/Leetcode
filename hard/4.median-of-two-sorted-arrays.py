#URL - https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1,nums2
        totalLen = len(A)+len(B)

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)-1

        while True:
            m = (l+r) // 2
            n = (totalLen // 2) - m -2

            Aleft = A[m] if m >= 0 else float("-infinity")
            Aright = A[m+1] if m+1 < len(A) else float("infinity")
            Bleft = B[n] if n >= 0 else float("-infinity")
            Bright = B[n+1] if n+1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if totalLen % 2:
                    return (min(Aright, Bright))
                else:
                    return ((max(Aleft,Bleft) + min(Aright, Bright)) / 2)
            elif Aleft > Bright:
                r = m-1 #Need less elements from small array A
            else:
                l = m+1 #Need more elements from small array A
