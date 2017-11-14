import heapq


def check_unique(arr):
    seen_before = set()
    length = len(arr)
    for i in range(length):
        if arr[i] in seen_before:
            return False
        else:
            seen_before.add(arr[i])
    return True


def find_substring(s, substr):
    s_len = len(s)
    subst_len = len(substr)
    if subst_len > s_len:
        return False
    for i in range(s_len - subst_len):
        if s[i:i + subst_len - 1] == substr:
            return True
    return False


def rotate_array(inputr, col, rows, flag):
    output = [[0] * col for i in range(rows)]
    for i in range(rows):
        for j in range(col):
            output[i][j] = inputr[j][rows - i - 1]
    return output


def contains_duplicate(arr):
    seen_before = set()
    length = len(arr)
    for i in range(length):
        if arr[i] in seen_before:
            return True
        else:
            seen_before.add(arr[i])
    return False


def find_substr(st, subst):
    st_len = len(st)
    subst_len = len(subst)
    if subst_len > st_len:
        return False
    for i in range(st_len - subst_len):
        if st[i:i + subst_len] == subst:
            return True
    return False


def rotate_1D(nums, k):
    result = []
    length = len(nums)
    for i in range(length - k, length):
        result.append(nums[i])
    for j in range(length - k):
        result.append(nums[j])
    return result


def two_sum(nums, target):
    seen_before = {}
    length = len(nums)
    for i in range(length):
        complement = target - nums[i]
        if complement in seen_before:
            return (seen_before[complement], i)
        else:
            seen_before[nums[i]] = i


def single_number(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


def calc_distance(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    return (x**2 + y**2)**0.5


def largest_k(nums, k):
    min_index = 0
    for i in range(k, len(nums)):
        for j in range(k):
            if calc_distance(nums[j]) < calc_distance(nums[min_index]):
                min_index = j
            if calc_distance(nums[min_index]) < calc_distance(nums[i]):
                temp = nums[min_index]
                nums[min_index] = nums[i]
                nums[i] = temp
        return nums[:k]


def largest_k2(nums, k):
    distances = {}
    result = []
    for i in range(len(nums)):
        distances[(calc_distance(nums[i]))] = nums[i]
    dist_values = distances.keys()
    dist_values.sort(reverse=True)
    for i in range(k):
        result.append(distances[dist_values[i]])
    return result


def largest_k3(nums, k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])
    for i in range(k, len(nums)):
        if calc_distance(nums[i]) > calc_distance(heap[0]):
            heapq.heapreplace(heap, nums[i])
        return heap

# move_zeros is a good array manipulation problem.
# need some more practice with 2D array manipulation.

# tomorrow: recursion. linked lists. trees.


def bin_search(nums, target, low, high):
    if high < low:
        return -1
    mid = low + (high - low) / 2
    if(nums[mid] == target):
        return mid
    if(nums[mid] > target):
        return bin_search(nums, target, low, mid - 1)
    if(nums[mid] < target):
        return bin_search(nums, target, mid + 1, high)


def find_pivot(nums, low, high):
    if high < low:
        return 0
    pivot = low + (high - low) / 2
    if pivot == 0 or nums[pivot] < nums[pivot - 1]:
        return pivot
    if nums[pivot] > nums[0]:
        return find_pivot(nums, pivot + 1, high)
    else:
        return find_pivot(nums, low, pivot - 1)


def search_arr(nums, target):
    return bin_search(nums, target, 0, len(nums) - 1)


def search_shifted_arr(nums, target):
    pivot1 = find_pivot(nums, 0, len(nums) - 1)
    if pivot1 == 0:
        return bin_search(nums, target, 0, len(nums) - 1)
    if nums[0] <= target:
        return bin_search(nums, target, 0, pivot1 - 1)
    else:
        return bin_search(nums, target, pivot1 + 1, len(nums) - 1)


def find_biggest_smaller(bst_root, num):
    answer = -1
    if bst_root is None:
        return answer
    curr = bst_root
    while curr is not None:
        if num > curr.key:
            answer = curr.key
            curr = curr.right
        else:
            curr = curr.left
    return answer


# def reverse_linked_list(llist)

# def insert_at(llist, k)

# upcoming: graphs. searching. memoization.


matrix = [[3, 2, 1], [2, 2, 5]]
example1 = [3, 5, 9, 12, 20]
example2 = [3, 5, 9, 3, 20]
sorted1 = [9, 15, 19, 28, 33]
shifted1 = [28, 33, 9, 15, 19]
tuples = [(2, 2), (8, 15), (2, 1), (0, 0), (0, 2)]
str1 = "Hello, my name is Giorgio."
str2 = "Fatso"
str3 = "is"
str4 = "Giorgio"
str5 = "dxdddxzzdx"

print(largest_k3(tuples, 3))
print(search_arr(sorted1, 28))
print(search_shifted_arr(shifted1, 19))
# print(two_sum(example1, 14))
# print(rotate_1D(example1, 3))
# print(find_substr(str1, str3))
# print(find_substr(str1, str4))
