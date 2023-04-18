import ctypes
import math
import multiprocessing
from multiprocessing.sharedctypes import Array
from _ctypes import Structure
from src.Edge import Edge

shared_data = []


class EdgeStructureC(Structure):
    _fields_ = [('start', ctypes.c_int), ('end', ctypes.c_int), ('weight', ctypes.c_long)]


def init_worker(data):
    global shared_data
    shared_data = data


def parallelMergesortEdges(data: list[Edge], processes: int) -> list[Edge]:
    """
    Splits mergesort into subtasks, which in calculated by the processes using shared memory
    :param data: Array of edges to sort
    :param processes: Number of processes used by the pool
    :return:
    """
    data = list(map(lambda edge: (edge.start, edge.end, edge.weight), data))
    data = Array(EdgeStructureC, data, lock=False)
    pool = multiprocessing.Pool(processes, initializer=init_worker, initargs=(data,))
    partitionSize = int(math.ceil(float(len(data)) / processes))

    partitions = [(i * partitionSize, (i + 1) * partitionSize - 1) for i in range(processes)]
    pool.starmap(__parallelMergesortWorker, partitions)
    # while len(partitions) > 1:
    #     unpairedSegment = partitions.pop() if len(partitions) % 2 == 1 else None
    # TODO: Fix middle param

    #     partitions = [(partitions[i][0], partitions[i + 1][1]) for i in range(0, len(partitions), 2)]
    #     pool.starmap(__mergePartitionsWorker, partitions)
    #     partitions += [unpairedSegment] if unpairedSegment else []
    #     print(partitions)
    return list(data)


def mergesortEdges(data: list, left: int, right: int) -> None:
    if left >= right:
        return
    middle = (left + right) // 2
    mergesortEdges(data, left, middle)
    mergesortEdges(data, middle + 1, right)
    __merge(data, left, middle, right)


def __parallelMergesortWorker(left: int, right: int):
    """
    It is used as a wrapper function, which provides to the main mergesort part of the shared memory
    :param left:
    :param right:
    """
    mergesortEdges(shared_data, left, right)


def __mergePartitionsWorker(left: int, middle: int, right: int) -> None:
    __merge(shared_data, left, middle, right)


def __merge(data: list, left: int, middle: int, right: int) -> None:
    left_data = data[left:middle + 1]
    right_data = data[middle + 1:right + 1]
    # left_data = copy.deepcopy(data[left:middle + 1])
    # right_data = copy.deepcopy(data[middle + 1:right + 1])
    i = j = 0
    k = left
    print(left_data[0].weight, right_data[0].weight)
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
    print(left_data[0].weight, right_data[0].weight)
