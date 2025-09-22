class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # parties: radiant, dire
        # rights: ban 1 senator's rights, announce victory

        # senate "RD", skip senators that have lost rights
        # assume each senator will ban senator rights of adjacent opposing senators
        # array is circular (last guy can ban first guy)

        # d_q = [i if s == "D" for i,s in enumerate(len(senate))]
        # r_q = [i if s == "R" for i,s in enumerate(len(senate))]
        d_q,r_q = deque(),deque()
        n = len(senate)

        # append indices to each q - practice shorthand
        for i,s in enumerate(senate):
            if s == "D":
                d_q.append(i)
            else:
                r_q.append(i)

        while d_q and r_q:
            if d_q[0] < r_q[0]:
                r_q.popleft()
                next_index = d_q.popleft() + n
                d_q.append(next_index)
            else:
                d_q.popleft()
                next_index = r_q.popleft() + n
                r_q.append(next_index)
        return "Radiant" if r_q else "Dire"

        
