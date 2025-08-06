class Codec:
    def __init__(self):
        self.index_map = {} # {index:string}

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for i in range(len(strs)):
            self.index_map[i] = strs[i]
            res.append(strs[i])
        return " ".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        for i in range(len(self.index_map)):
            res.append(self.index_map[i])
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))