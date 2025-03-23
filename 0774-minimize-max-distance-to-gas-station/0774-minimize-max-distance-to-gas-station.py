class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def condition(mid):
            count = k
            for i in range(len(stations)-1):
                count -= (stations[i+1]-stations[i])//mid
                if count < 0:
                    return False
            return True

        l,r = 0, max(stations)+1
        x = 10**-6
        while l < r:
            mid = (l+r)/2
            if condition(mid):
                r = mid-x
            else:
                l = mid+x
        return l