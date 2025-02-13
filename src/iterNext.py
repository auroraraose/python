class nested_iterator:
    def __init__(self, nested_list):
        self.flattened = self._flatten(nested_list)
        self.index = 0
    def _flatten(self, nested_list):
        for sublist in nested_list:
            for item in sublist:
                yield item
 
    def __iter__(self):
        return self
 
    def __next__(self):
        try:
            value = next(self.flattened)
            return value
        except StopIteration:
            raise StopIteration
nested_list = [[1, 2], [3, 4], [5]]
iterator = nested_iterator(nested_list)
 
for num in iterator:
    print(num,"", end="")