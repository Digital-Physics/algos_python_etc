from __future__ import annotations


class FlattenAndIterate:
    def __init__(self, nested_l: list[int | list]) -> None:
        # could also left pop in constant time with "from collection import deque"
        self.stack_of_items = nested_l[::-1]
        self.next_item = None
        print("initialized stack", self.stack_of_items)

    def next(self) -> int | None:
        print("next() called")
        return self.next_item

    def hasNext(self) -> bool:
        print("hasNext() called")
        if self.stack_of_items:
            self.next_item = self.stack_of_items.pop()
            if isinstance(self.next_item, int):
                return True
            else:
                print("append elements of nested list in reverse order")
                print(self.next_item[::-1])
                for item in reversed(self.next_item):
                    self.stack_of_items.append(item)
                print("stack now", self.stack_of_items)
                return self.hasNext()
        else:
            return False


class FlattenAndIterate2:
    def __init__(self, nested_l: list[int | list]) -> None:
        """this algorithm treats the list as a string of symbols"""
        self.list_str = str(nested_l)
        self.next_item = None
        print("initialized stack #2", self.list_str)

    def next(self) -> int | None:
        print("next() called")
        return self.next_item

    def hasNext(self) -> bool:
        print("hasNext() called")
        if self.list_str:
            print("string has length")
            self.next_item, self.list_str = self.list_str[0], self.list_str[1:]
            print("next item and remaining string", self.next_item, self.list_str)
            try:
                self.next_item = int(self.next_item)
                print("no ValueError :)")
                return True
            except ValueError:
                print("must have been a comma, space, or parenthesis")
                return self.hasNext()
        else:
            return False


test_list = [1, [2, [[3, 4], [5, 6]]]]

iterator = FlattenAndIterate(test_list)
iterator2 = FlattenAndIterate2(test_list)

res = []
while iterator.hasNext():
    res.append(iterator.next())

print(res)

res2 = []
while iterator2.hasNext():
    res2.append(iterator2.next())

print(res2)
