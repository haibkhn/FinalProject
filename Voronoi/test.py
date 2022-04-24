import numpy as np

array_to_check = [2., 1.]
list_np_arrays = np.array([[0, 0]])

# list_np_arrays = np.append(list_np_arrays, [array_to_check], axis=0)
# list_np_arrays = np.array([[1., 1.], [1., 2.]])
# array_to_check = np.array([1., 2.])

# is_in_list = np.any(np.all(array_to_check == list_np_arrays, axis=1))
# print(list_np_arrays)
# print(is_in_list)
print(np.isin(array_to_check, list_np_arrays))
