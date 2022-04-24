import numpy as np

# array_to_check = [2., 1.]

# list_np_arrays = np.array([[0, 0]])

# list_np_arrays = np.append(list_np_arrays, [[3, 4]], axis=0)
# list_np_arrays = np.array([[1., 1.], [1., 2.]])
# array_to_check = np.array([1., 2.])

# is_in_list = np.any(np.all(array_to_check == list_np_arrays, axis=1))
# print(list_np_arrays)
# print(is_in_list)
# print(is_in_list == False)

first = np.array([[1, 2]])
second = [[5, 5], [4, 3]]
third = [5, 2]
first = np.append(first, second, axis=0)
# first += second
# first += third
print(len(first))
