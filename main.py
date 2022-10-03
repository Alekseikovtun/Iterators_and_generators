class List:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.current_list_index = 0
        self.item_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_list = self.nested_list[self.current_list_index]
        if self.item_index == len(current_list):
            self.current_list_index += 1
            if self.current_list_index == len(self.nested_list):
                raise StopIteration
            current_list = self.nested_list[self.current_list_index]
            self.item_index = 0
        item = current_list[self.item_index]
        self.item_index += 1
        return item


nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
for item in List([nested_list]):
    print(item)
