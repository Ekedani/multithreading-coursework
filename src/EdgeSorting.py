from ctypes import Structure, c_int, c_double
from multiprocessing import Pool
from multiprocessing.sharedctypes import RawArray
from math import ceil
from copy import copy
from src.Edge import Edge

shared_data = []


def init_worker(data):
    """
    Helper function which initializes a process pool with shared data
    :param data: it is shared between processes
    """
    global shared_data
    shared_data = data


class HelperEdgeStructure(Structure):
    _fields_ = [('pos', c_int), ('weight', c_double)]


def parallelMergesortEdges(data: list[Edge], processes: int) -> list[Edge]:
    """
    Splits mergesort into subtasks, which are calculated by the processes using shared memory
    :param data: Array of edges to sort
    :param processes: Number of processes used by the pool
    :return:
    """
    edges_number = len(data)
    structured_data = [(idx, data[idx].weight) for idx in range(0, edges_number)]
    structured_data = RawArray(HelperEdgeStructure, structured_data)
    processes = min(processes, edges_number)
    pool = Pool(processes, initializer=init_worker, initargs=(structured_data,))

    partition_size = int(ceil(float(edges_number) / processes))
    partitions = [(i * partition_size, min(edges_number - 1, (i + 1) * partition_size - 1)) for i in range(processes)]
    pool.starmap(__parallelMergesortWorker, partitions)

    while len(partitions) > 1:
        unpaired_partition = partitions.pop() if len(partitions) % 2 == 1 else None
        if len(partitions) == processes:
            partitions = [(partitions[i][0], partitions[i][1], partitions[i + 1][1]) for i in
                          range(0, len(partitions), 2)]
        else:
            partitions = [(partitions[i][0], partitions[i][2], partitions[i + 1][2]) for i in
                          range(0, len(partitions), 2)]
        pool.starmap(__mergePartitionsWorker, partitions)
        partitions += [unpaired_partition] if unpaired_partition else []

    pool.close()
    return [data[x.pos] for x in structured_data]


def mergesortEdges(data: list, left: int, right: int) -> None:
    """
    :param data: a list of elements to be sorted
    :param left: left index of the array to be sorted
    :param right: right index of the array to be sorted
    """
    if left >= right:
        return
    middle = (left + right) // 2
    mergesortEdges(data, left, middle)
    mergesortEdges(data, middle + 1, right)
    __merge(data, left, middle, right)


def __parallelMergesortWorker(left: int, right: int) -> None:
    """
    It is used as a wrapper function, which provides to the main mergesort part of the shared memory
    :param left: left index of the partition to be sorted
    :param right: right index of the partition to be sorted
    """
    mergesortEdges(shared_data, left, right)


def __mergePartitionsWorker(left: int, middle: int, right: int) -> None:
    """
    :param left: left index of the partition to be merged
    :param middle: middle index of the partition to be merged
    :param right: right index of the partition to be merged
    """
    __merge(shared_data, left, middle, right)


def __merge(data: list, left: int, middle: int, right: int) -> None:
    """
    :param data: a list of elements to be sorted
    :param left: left index of the subarray to be merged
    :param middle: middle index of the subarray to be merged
    :param right: right index of the subarray to be merged
    """
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
