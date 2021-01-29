class QuickSort:
    def partition(self, arr, low, high):
        i = (low-1)
        pivot = arr[high]

        for j in range(low, high):

            if arr[j].lower() <= pivot:

                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:

            partitioning_index = self.partition(arr, low, high)

            self.quickSort(arr, low, partitioning_index-1)
            self.quickSort(arr, partitioning_index+1, high)
