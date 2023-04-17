import ctypes
import math
import multiprocessing

from src.Edge import Edge

shared_data = []


def init_worker(data):
    global shared_data
    shared_data = data


def parallelMergesortEdges(data: list[Edge], processes: int) -> list[Edge]:
    data = multiprocessing.Array(ctypes.py_object, data, lock=False)
    pool = multiprocessing.Pool(processes, initializer=init_worker, initargs=(data,))
    partitionSize = int(math.ceil(float(len(data)) / processes))
    partitions = [(i * partitionSize, (i + 1) * partitionSize) for i in range(processes)]
    pool.starmap(__parallelMergesortWorker, partitions)
    print(len(data), partitions)
    for _ in shared_data:
        print(_.weight, end=' ')
    print()
    # while len(partitions) > 1:
    #     unpairedSegment = partitions.pop() if len(partitions) % 2 == 1 else None
    #     partitions = [(partitions[i][0], partitions[i + 1][1]) for i in range(0, len(partitions), 2)]
    #     pool.starmap(__mergePartitionsWorker, partitions)
    #     partitions += [unpairedSegment] if unpairedSegment else []
    #     print(partitions)
    return list(data)


def mergesortEdges(data: list[Edge], left: int, right: int) -> None:
    if left >= right:
        return
    middle = (left + right) // 2
    print(left, middle, right, 'entered')
    mergesortEdges(data, left, middle)
    mergesortEdges(data, middle + 1, right)
    __merge(data, left, middle, right)
    print(left, middle, right, 'finished')


def __parallelMergesortWorker(left: int, right: int):
    if left >= right:
        return
    middle = (left + right) // 2
    print(left, middle, right, 'entered')
    mergesortEdges(shared_data, left, middle)
    mergesortEdges(shared_data, middle + 1, right)
    __merge(shared_data, left, middle, right)
    print(left, middle, right, 'finished')


def __mergePartitionsWorker(left: int, middle: int, right: int) -> None:
    left_data = shared_data[left:middle + 1]
    right_data = shared_data[middle + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_data) and j < len(right_data):
        if left_data[i].weight < right_data[j].weight:
            shared_data[k] = left_data[i]
            i += 1
        else:
            shared_data[k] = right_data[j]
            j += 1
        k += 1
    while i < len(left_data):
        shared_data[k] = left_data[i]
        i += 1
        k += 1
    while j < len(right_data):
        shared_data[k] = right_data[j]
        j += 1
        k += 1


def __merge(data: list[Edge], left: int, middle: int, right: int) -> None:
    print('Entered merge stage')
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
    print('Finished merge stage')

