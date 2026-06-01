class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {('c','a','t'):["cat","act"]}
        anagramGroups = defaultdict(list)
        
        for st in strs:
            chars=[0]*26
            for c in st:
                chOrd = ord(c) - ord('a')
                chars[chOrd] +=1
            anagramGroups[tuple(chars)].append(str(st))
        return (list(anagramGroups.values()))
