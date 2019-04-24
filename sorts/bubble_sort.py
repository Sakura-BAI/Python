from __future__ import print_function


def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    
    >>> bubble_sort([-23,0,6,-4,34])
    [-23,-4,0,6,34]
    """

    """
    冒泡排序,就不断的两个相近的比较,外层循环一个大的数据长度次数.
    for i in range(3) ,循环3次.
    range(3)生成的序列是从0开始小于3的整数[0,1,2]
     if not swapped: break   
    IF not TRUE ,  swapped =TRUE 两个比较有大于前面的.需要排序
    还有一个精妙的地方,大概就是它的循环次数设置.  数据列4 ,外循环3 ,内循环也是3.将最大的排序到最后,就少一次.
    """

    length = len(collection)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped: break  # Stop iteration if the collection is sorted.
    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    user_input = raw_input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted), sep=',')
