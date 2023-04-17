import ctypes
import math
import multiprocessing

from src.Edge import Edge


def parallelMergesortEdges(data: list[Edge], processNum: int) -> list[Edge]:
    data = multiprocessing.RawArray(ctypes.py_object, data)
    pool = multiprocessing.Pool(processNum)
    partitionSize = int(math.ceil(float(len(data)) / processNum))
    partitions = [(data, i * partitionSize, (i + 1) * partitionSize) for i in range(processNum)]
    pool.starmap(mergesortEdges, partitions)
    #while len(partitions) > 1:
    #    extra = partitions.pop() if len(partitions) % 2 == 1 else None
    #    subtasks = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    #    data = pool.map(merge, data) + ([extra] if extra else [])
    return list(data)


def mergesortEdges(data: list[Edge], left: int, right: int) -> None:
    if left >= right:
        return
    middle = (left + right) // 2
    mergesortEdges(data, left, middle)
    mergesortEdges(data, middle + 1, right)
    merge(data, left, middle, right)


def merge(data: list[Edge], left: int, middle: int, right: int) -> None:
    left_data = data[left:middle + 1]
    right_data = data[middle + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_data) and j < len(right_data):
        if left_data[i].weight < right_data[j].weight:
            data[k] = left_data[i]
            i += 1
        else:
            data[k] = right_data[j]
            j += 1
        k += 1
    while i < len(left_data):
        data[k] = left_data[i]
        i += 1
        k += 1
    while j < len(right_data):
        data[k] = right_data[j]
        j += 1
        k += 1
