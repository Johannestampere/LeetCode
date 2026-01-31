class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set()

        for n in nums1:
            s.add(n)

        res = []
        for n in nums2:
            if n in s:
                res.append(n)
                s.remove(n)

        return res