class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cache = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            cache[key].append(s)
        
        return list(cache.values())
