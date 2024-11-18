import math 

def generalized_max_product_subarrays(A: list,m:int):
    subarrays = slice_in_subarray(A)
    print(subarrays)
    return max_A(subarrays,m)

def max_A(A: list, m: int) -> list[list[int]]:
    """Exercise 2: Generalized Max. Product Subarray (7 Points)
    Given an integer array A of length n, and an integer m (where m ≤ n). The goal is to find the
    maximum product that can be obtained by selecting exactly m non-overlapping contiguous subarrays.
    Note that each subarray should be non-empty. The following is an example:
    Let A = [1, -2, 3, -4, 5, -6, 0, 7, 8, 9, 0] and m = 3.
    The maximum product can be achieved by choosing the subarrays [3, -4, 5, -6], [7], and [8, 9] with a
    total product of 3 × -4 × 5 × -6 × (7) × (8 × 9) = 181440.
    Give a polynomial time algorithm that achieves our goal. Argue correctness and run time."""
    
    if m == 0 or A == []:
        x = 1
    else:
        x = max(max_A(A[:-1],m), list_product(A[-1]) * max_A(A[:-1], m-1))
    return x

def list_product(A):
    return  [math.prod(A)]

def slice_in_subarray(A:list): 
    if A == []:
        return []
    negatives = [x for x in A if x < 0]
    if len(negatives) % 2 == 0:
        largest_negative = max(negatives)
        index = A.index(largest_negative)
        A[index] = 0

    subarray = []
    array = []
    for a in A:
        if a == 0 or (a < 1 and a > 0) :
            if subarray == []:
                continue
            array.append(subarray)
            subarray = []
        else:
            subarray.append(a)
    if len(subarray) > 0:
        array.append(subarray)
    return array






if __name__ == "__main__":
    A = [1,-2,3,-4,5,-6,0,7,8,9,0]
    print(generalized_max_product_subarrays(A,3))

