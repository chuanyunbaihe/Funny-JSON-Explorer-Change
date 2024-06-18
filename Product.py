from Iterator import *
from Node import *


# 产品的抽象基类
class Product(ABC):
    def __init__(self):
        self._container = None
        self._leaf = None
        self._my_container = None

    @abstractmethod
    def set_container(self):
        pass

    @abstractmethod
    def set_leaf(self):
        pass

    def load_data(self, data):
        self._my_container = self._container('root', 0)
        stack = [(self._my_container, data)]
        while stack:
            current_container, current_data = stack.pop()
            for key, value in current_data.items():
                if isinstance(value, dict):
                    new_container = self._container(key, current_container.level + 1)
                    current_container.add_child(new_container)
                    stack.append((new_container, value))
                else:
                    leaf = self._leaf(key, value)
                    current_container.add_child(leaf)

    def show(self, icon, data):
        self.load_data(data)
        parent_is_last = []
        iterator_collection = JSONIteratorCollection(self._my_container)
        iter = iterator_collection.create_iterator()
        while iter.more():
            child, first, last = iter.get_next()
            child.draw(self._my_container.level + 1, first, last, parent_is_last, icon)


class TreeProduct(Product):
    def set_container(self):
        self._container = TreeContainer

    def set_leaf(self):
        self._leaf = TreeLeaf


class RectangleProduct(Product):
    def set_container(self):
        self._container = RectangleContainer

    def set_leaf(self):
        self._leaf = RectangleLeaf
