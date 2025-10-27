class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split('/')
        stack = []
        
        for c in split_path:
            if c == '..':
                if stack:
                    stack.pop()
            elif c and c != '.': 
                stack.append(c)
        return '/' + "/".join(stack)