class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # parties: radiant, dire
        # rights: ban 1 senator's rights, announce victory

        # senate "RD", skip senators that have lost rights
        # assume each senator will ban senator rights of adjacent opposing senators
        # array is circular (last guy can ban first guy)

        d_q = deque([i for i, s in enumerate(senate) if s == "D"])
        r_q = deque([i for i, s in enumerate(senate) if s == "R"])
        n = len(senate)

        while d_q and r_q:
            if d_q[0] < r_q[0]:
                r_q.popleft()
                d_q.append(d_q.popleft() + n)
            else:
                d_q.popleft()
                r_q.append(r_q.popleft() + n)
        return "Radiant" if r_q else "Dire"

        
