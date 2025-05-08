class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        arr.sort(key=lambda w: int(w[-1]))
        for i in range(len(arr)):
            arr[i] = arr[i][:-1]
        return " ".join(arr)
