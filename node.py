class Node():
    def __init__(self, name):
        self.name = name
        self._parents = []
        self._children = []
        self._temp_parent = None

    def get_name(self):
        return self.name

    def get_children(self):
        return self._children
    
    def get_parents(self):
        return self._parents
    
    def add_temp_parent(self, parent):
        self._temp_parent = parent

    def get_temp_parent(self):
        return self._temp_parent

    def add_child(self, node):
        self._children.append(node)
        node._parents.append(self)
