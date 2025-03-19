class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # well-formed parentheses have the same number of open and closed and are formed in the correct order
        def dfs(open, closed, combo):
            if len(combo) == n*2: # because we have n pairs, we will have 2n total parentheses
                res.append("".join(combo[::]))
                return
            
            if open < n: # since n + n == 2n, we want to have n of each open/closed
                combo.append("(")
                dfs(open+1,closed,combo)
                combo.pop()

            if open > closed: # if open > closed, this means that we can add a closed
            # when i did closed < n, 
            # it was not checking if it would be in the right order
                combo.append(")")
                dfs(open,closed+1,combo)
                combo.pop()

        dfs(0,0,[])
        return res