class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # first pass to find all unmatched opens, remove unmatched closed
        # keep = total opens - unmatched opens
        # second pass to find the rest of the unmatched opens and remove them

        #                 j
        # s = "lee(t(c)o)de"
        #                  i

        # ex = 0
        # total = 2
        # j = 11
        # i = 12

        # keep = 3-1 = 2
        # length = 11
        # j = 5
        # i = 5

        # O(1) space = pointers. technically O(1) space is impossible with python bc strings immutable, so the input would have to be given to us as an array of characters.
        # O(n) time
        j = 0
        total_op = 0
        extra_op = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                extra_op += 1
                total_op += 1
            elif s[i] == ")":
                if extra_op == 0:
                    continue
                extra_op -= 1
            s[j] = s[i]
            j += 1

        keep = total_op - extra_op
        length = j
        j = 0
        for i in range(length):
            if s[i] == "(":
                if keep == 0:
                    continue
                keep -= 1
            s[j] = s[i]
            j += 1
        return "".join(s[:j])
        