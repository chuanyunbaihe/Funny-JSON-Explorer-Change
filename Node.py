from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def add_child(self, child):
        pass

    @abstractmethod
    def draw(self, level, is_first, is_last, parent_is_last, icon):
        pass


class Leaf(Component):  # 表示树中各个项目的叶子节点
    def add_child(self, child):
        pass

    @abstractmethod
    def draw(self, level, is_first, is_last, parent_is_last, icon):
        pass


class TreeLeaf(Leaf):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        indent = ""
        for i in range(level - 1):
            if parent_is_last[i]:
                indent += "    "
            else:
                indent += "│   "

        connector = "└─" if is_last else "├─"
        line = f"{indent}{connector}{icon.get_leaf_icon()}{self.name}"
        if self.value is not None:
            line += f": {self.value}"
        print(line)


class RectangleLeaf(Leaf):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        indent = ""
        flag = True
        for i in range(level - 1):
            if not parent_is_last[i]:
                flag = False
            indent += "│   "
        if flag and is_last:
            indent = '└───'
            for i in range(level - 2):
                indent += '───'
        connector = "┴─" if flag and is_last else "├─"
        subfix = '┘' if flag and is_last else '┤'

        if self.value is not None:
            prefix = indent + connector + icon.get_leaf_icon()
            print(f"{prefix}{self.name}: {self.value} " + '─' * (43 - len(prefix) - len(self.name) - len(self.value)) + subfix)
        else:
            prefix = indent + connector + icon.get_leaf_icon()
            print(f"{prefix}{self.name} " + '─' * (45 - len(prefix) - len(self.name)) + subfix)


class Container(Component):  # 在树中表示分支的容器构件
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    @abstractmethod
    def draw(self, level, is_first, is_last, parent_is_last, icon):
        pass


class TreeContainer(Container):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        indent = ""
        for i in range(level - 1):
            indent += "│   " if not parent_is_last[i] else "    "

        connector = "└─" if is_last else "├─"
        print(f"{indent}{connector}{icon.get_container_icon()}{self.name}")
        parent_is_last.append(is_last)
        for i, child in enumerate(self.children):
            child.draw(level + 1, i == 0, i == len(self.children) - 1, parent_is_last, icon)
        parent_is_last.pop()


class RectangleContainer(Container):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        indent = ""
        for i in range(level - 1):
            indent += "│   " if not parent_is_last[i] else "    "
        connector = "┌─" if level == 1 and is_first else "├─"
        subfix = '┐' if level == 1 and is_first else '┤'
        prefix = indent + connector + icon.get_container_icon()
        print(f"{prefix}{self.name} " + '─' * (45 - len(prefix) - len(self.name)) + subfix)
        parent_is_last.append(is_last)
        for i, child in enumerate(self.children):
            child.draw(level + 1, i == 0, i == len(self.children) - 1, parent_is_last, icon)
        parent_is_last.pop()
