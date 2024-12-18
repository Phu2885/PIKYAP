class Unique:
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.iterator = iter(items)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.iterator)
            comp_item = item.lower() if self.ignore_case and isinstance(item, str) else item
            if comp_item not in self.seen:
                self.seen.add(comp_item)
                return item



if __name__ == '__main__':
    data = [1, 1, 2, 2, 'a', 'A', 'b', 'B']
    print(list(Unique(data, ignore_case=True)))
    print(list(Unique(data)))
