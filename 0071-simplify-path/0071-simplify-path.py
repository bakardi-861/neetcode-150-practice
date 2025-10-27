class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack - Meta-tagged
        # directories separated by single '/', treat multiple slashes as 1
        # delete trailing '/' unless it is root directory
        # anything not '.','..' or '/' treated as a directory name

        # Input: path = "/home/user/Documents/../Pictures"
        #                                                 i
        # ['/','home','/','user','/','Pictures']
        split_path = path.split('/')
        stack = []
        
        for c in split_path:
            if c not in ['','.','..']: 
                stack.append(c)
            elif stack and c == '..':
                stack.pop()
        return '/' + "/".join(stack)




