from Product import *


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def execute_container(self):
        pass

    @abstractmethod
    def execute_leaf(self):
        pass


class TreeStrategy(Strategy):
    def __init__(self):
        self.product = TreeProduct()

    def execute(self):
        return self.product

    def execute_container(self):
        self.product.set_container()

    def execute_leaf(self):
        self.product.set_leaf()


class RectangleStrategy(Strategy):
    def __init__(self):
        self.product = RectangleProduct()

    def execute(self):
        return self.product

    def execute_container(self):
        self.product.set_container()

    def execute_leaf(self):
        self.product.set_leaf()


class Context:
    def __init__(self, strategy: Strategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self):
        if self._strategy is None:
            raise ValueError("Strategy not set")
        self._strategy.execute_container()
        self._strategy.execute_leaf()
        return self._strategy.execute()
