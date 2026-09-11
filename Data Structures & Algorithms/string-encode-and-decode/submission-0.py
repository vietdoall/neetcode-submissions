class Solution:

    def encode(self, strs: List[str]) -> str:
        #length#string
        return ''.join(f"{len(s)}#{s}" for s in strs)
        #   5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # tìm dấu #
            j = s.find('#', i) # j=1
            length = int(s[i:j])  # lấy độ dài
            word = s[j+1:j+1+length]  # cắt đúng số ký tự
            res.append(word)
            i = j + 1 + length
        return res