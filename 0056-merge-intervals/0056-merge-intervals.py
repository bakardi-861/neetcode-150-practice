class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: sort by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            prev = merged[-1]

            if current[0] <= prev[1]:  # overlap
                # merge by updating end
                prev[1] = max(prev[1], current[1])
            else:
                merged.append(current)

        return merged