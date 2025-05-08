class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        l, r = 0, len(arr) - 1

        def index(word):
            return int(word[-1]) - 1

        # In-place QuickSort with 3-way partitioning
        def quicksort(l, r):
            if l >= r:
                return

            pivot_idx = random.randint(l, r)
            pivot = index(arr[pivot_idx])
            lt, gt, i = l, r, l

            while i <= gt:
                current = index(arr[i])
                if current < pivot:
                    arr[lt], arr[i] = arr[i], arr[lt]
                    lt += 1
                    i += 1
                elif current > pivot:
                    arr[gt], arr[i] = arr[i], arr[gt]
                    gt -= 1
                else:
                    i += 1

            quicksort(l, lt - 1)
            quicksort(gt + 1, r)

        quicksort(l, r)

        # Remove the trailing digit and join
        return " ".join(word[:-1] for word in arr)
