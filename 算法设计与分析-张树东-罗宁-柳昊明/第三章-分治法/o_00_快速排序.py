def quick_sort_optimized(arr, low=0, high=None):
    """
    优化的快速排序：使用三数取中法选择基准

    参数:
    arr: 待排序的列表
    low: 排序起始索引
    high: 排序结束索引

    返回:
    排序后的列表
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 使用三数取中法选择基准
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]

        # 将中间值作为基准，放到最右边
        arr[mid], arr[high] = arr[high], arr[mid]

        # 分区操作
        pi = partition(arr, low, high)

        # 递归排序
        quick_sort_optimized(arr, low, pi - 1)
        quick_sort_optimized(arr, pi + 1, high)

    return arr


def partition(arr, low, high):
    """
    分区函数：选择基准元素，将小于基准的元素放在左边，大于基准的元素放在右边

    参数:
    arr: 待分区的列表
    low: 分区起始索引
    high: 分区结束索引

    返回:
    基准元素的最终位置
    """
    # 选择最右边的元素作为基准
    pivot = arr[high]

    # 小于基准的元素的索引
    i = low - 1

    # 遍历数组，将小于基准的元素移到左边
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 将基准元素放到正确位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# 测试优化版本
test_array = [64, 34, 25, 12, 22, 11, 90]
print("优化快速排序:", quick_sort_optimized(test_array.copy()))