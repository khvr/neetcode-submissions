class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            encoded_string=encoded_string+str(len(s)) +"#"+s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j]!= "#":
                j+=1
            length = int(s[i:j])
            string = s[j+1:j+1+length]
            res.append(string)
            i = j+1+length
        return res
