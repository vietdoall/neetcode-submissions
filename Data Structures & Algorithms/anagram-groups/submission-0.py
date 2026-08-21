class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            groups = defaultdict(list)
            for word in strs:
            # chuẩn hóa bằng cách sort ký tự
                key = ''.join(sorted(word))
                groups[key].append(word)
        
            return list(groups.values())