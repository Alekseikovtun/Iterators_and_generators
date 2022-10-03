def join_list(list_of_lists):
    for current_list in list_of_lists:
        for item in current_list:
            yield item


nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
flat_list = []
for item in join_list(nested_list):
    flat_list.append(item)
print(flat_list)

test_list = [['a'], [True], [1], [False]]
expected = ['a', True, 1, False]
flat_test_list = []
for item in join_list(test_list):
    flat_test_list.append(item)
print(flat_test_list)
assert flat_test_list == expected
