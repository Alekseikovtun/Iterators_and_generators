class List:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.main_slider = 0
        self.nested_slider = 0
        self.len_of_list = len(self.nested_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.nested_slider == len(self.nested_list[self.main_slider]):
            self.main_slider += 1
            self.nested_slider = 0
            if self.main_slider == self.len_of_list:
                raise StopIteration
        item = self.nested_list[self.main_slider][self.nested_slider]
        self.nested_slider += 1
        return item


# nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
# for item in List(nested_list):
#     print(item)
# flat_list = []
# for item in List(nested_list):
#     flat_list.append(item)
# print(flat_list)

nested_list = [[1, 2, 'b'], [100, None, False]]
flat_list = []
exepcted = [1, 2, 'b', 100, None, False]
for item in List(nested_list):
    flat_list.append(item)
print(flat_list)
assert flat_list == exepcted