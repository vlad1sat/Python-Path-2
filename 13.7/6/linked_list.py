from typing import Any, Optional


class Node:

    def __init__(self, value: Optional[Any] = None, next_node: Optional['Node'] = None) -> None:
        self.__value = value
        self.__next = next_node

    @property
    def value(self):
        return self.__value

    @property
    def next(self) -> Optional['Node']:
        return self.__next

    @next.setter
    def next(self, value: Any) -> None:
        self.__next = value

    def __str__(self):
        return 'Node [{}]'.format(str(self.__value))


class LinkedList:

    def __init__(self) -> None:
        self.__head: Optional[Node] = None
        self.__length = 0

    def append(self, element: Any) -> None:
        new_node = Node(element)
        if self.__head is None:
            self.__head = new_node
            return

        last = self.__head
        while last.next:
            last = last.next
        last.next = new_node
        self.__length += 1

    def remove(self, index: int) -> None:
        cur_node = self.__head
        cur_index = 0
        if self.__length <= 0 or self.__length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.__head = cur_node.next
                self.__length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.__length -= 1

    def __str__(self) -> str:
        if self.__head is not None:
            current = self.__head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append((str(current.value)))
            return '[{}]'.format(' '.join(values))
        return '[]'

    def get(self, index: int) -> Any:
        cur_node = self.__head
        cur_index = 0
        if self.__length <= 0 or index > self.__length:
            raise IndexError

        while cur_node is not None:
            if cur_index == index:
                return cur_node.value
            cur_index += 1
            cur_node = cur_node.next
