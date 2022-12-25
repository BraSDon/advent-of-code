from typing import List
from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass


class File(Element):
    def __init__(self, size):
        self.size = size

    def get_size(self) -> int:
        return self.size


class Directory(Element):
    def __init__(self, parent):
        self.parent = parent
        self.children = dict()
        self.size = None

    def add_children(self, children):
        self.children.update(children)

    def move_up(self):
        if self.parent is None: raise ValueError("Already in root")
        return self.parent

    def move_down(self, dir_name):
        return self.children[dir_name]

    def get_size(self) -> int:
        if self.size is None: self.size = sum(map(lambda x: x.get_size(), self.children.values()))
        return self.size


def get_dir_sizes(root: Directory) -> List[int]:
    sizes = [root.get_size()]
    for child in root.children.values():
        if isinstance(child, File): continue
        sizes = sizes + get_dir_sizes(child)
    return sizes


with open("inputs/day07.txt") as f:
    lines = f.readlines()

root = Directory(None)
current = root
children = dict()
for line in lines[1:]:
    words = line.split()
    key = words[1]
    match words[0]:
        case "$":
            if words[1] != "cd": continue
            current.add_children(children)
            children = dict()
            if words[2] == "..":
                current = current.move_up()
            else:
                current = current.move_down(words[2])
        case "dir":
            children[key] = Directory(current)
        case _:
            children[key] = File(int(words[0]))

dir_sizes = get_dir_sizes(root)
cumsum = sum(filter(lambda x: x <= 100000, dir_sizes))
print(f"Task 1: {cumsum}")

to_be_freed = 30000000 - (70000000 - root.get_size())
print(f"Task 2: {min(filter(lambda x: x >= to_be_freed, dir_sizes))}")


