import ctypes
import math
import multiprocessing
from copy import copy
from multiprocessing.sharedctypes import RawArray
from ctypes import Structure
from src.Edge import Edge

shared_data = []


def init_worker(data):
    global shared_data
    shared_data = data


class HelperEdgeStructure(Structure):
    _fields_ = [('pos', ctypes.c_int), ('weight', ctypes.c_double)]


def parallelMergesortEdges(data: list[Edge], processes: int) -> list[Edge]:
    """
    Splits mergesort into subtasks, which in calculated by the processes using shared memory
    :param data: Array of edges to sort
    :param processes: Number of processes used by the pool
    :return:
    """
    structured_data = [(idx, data[idx].weight) for idx in range(0, len(data))]
    structured_data = RawArray(HelperEdgeStructure, structured_data)
    pool = multiprocessing.Pool(processes, initializer=init_worker, initargs=(structured_data,))
    partitionSize = int(math.ceil(float(len(data)) / processes))
    partitions = [(i * partitionSize, (i + 1) * partitionSize - 1) for i in range(processes)]
    pool.starmap(__parallelMergesortWorker, partitions)
    while len(partitions) > 1:
        unpairedSegment = partitions.pop() if len(partitions) % 2 == 1 else None
        # Joining partitions by middle pivot
        if len(partitions) == processes:
            partitions = [(partitions[i][0], partitions[i][1], partitions[i + 1][1]) for i in
                          range(0, len(partitions), 2)]
        else:
            partitions = [(partitions[i][0], partitions[i][2], partitions[i + 1][2]) for i in
                          range(0, len(partitions), 2)]
        pool.starmap(__mergePartitionsWorker, partitions)
        partitions += [unpairedSegment] if unpairedSegment else []

    return [data[x.pos] for x in structured_data]


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
    :param left:Ы
    :param right:
    """
    mergesortEdges(shared_data, left, right)


def __mergePartitionsWorker(left: int, middle: int, right: int) -> None:
    __merge(shared_data, left, middle, right)


def __merge(data: list, left: int, middle: int, right: int) -> None:
    left_data = [copy(data[i]) for i in range(left, middle + 1)]
    right_data = [copy(data[i]) for i in range(middle + 1, right + 1)]
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
