class Solution:
    def simplifyPath(self, path: str) -> str:
        #stack
        path = path.replace("/"," ")
        stack = []
        for c in path.split():
            if c in ['.',' ']:
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return "/" + "/".join(stack)
