from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def more(self):
        pass


class IteratorNode(Iterator):
    def __init__(self, node):
        self.node = node
        self.count = 0

    def get_next(self):
        self.count += 1
        return self.node.children[self.count - 1], self.count == 1, self.count == len(self.node.children)

    def more(self):
        return self.count < len(self.node.children)


class IteratorCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass


class JSONIteratorCollection(IteratorCollection):
    def __init__(self, root):
        self.root = root

    def create_iterator(self):
        return IteratorNode(self.root)
