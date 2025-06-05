from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        sortedHashMap = defaultdict(list)

        for s in strs:
            sortedHashMap[tuple(sorted(s))].append(s)
        
        strGroups = []

        for k, v in sortedHashMap.items():
            strGroups.append(v)

        return strGroups