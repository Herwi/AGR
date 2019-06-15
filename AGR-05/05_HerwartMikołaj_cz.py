import string

class Vertex:
    def __init__(self, key, tree):
        self.key = key
        self.par = None
        self.left = None
        self.right = None
        self.tree = tree

    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left:
            return 1 + self.left.height()
        elif self.right:
            return 1 + self.right.height()
        else:
            return 0
    def add(self, key):
        if key == self.key:
            print("Klucz {} jest już w drzewie.".format(key))
        elif key > self.key:
            if self.right:
                return self.right.add(key)
            else:
                v = Vertex(key, self.tree)
                self.right = v
                v.par = self
                print("Dodano klucz {}. Wysokość drzewa to: {}".format(key, self.tree.height()))
        else:
            if self.left:
                return self.left.add(key)
            else:
                v = Vertex(key, self.tree)
                self.left = v
                v.par = self
                print("Dodano klucz {}. Wysokość drzewa to: {}".format(key, self.tree.height()))

class Tree:
    def __init__(self):
        self.root = None

    def load(self, file):
        with open (file, 'r') as inp:
            tab = []
            for i in inp:
                tab = i.split()
            for i in tab:
                self.add(int(i))
    
    def add(self, key):
        if self.root is None:
            self.root = Vertex(key, self)
            print("Dodano klucz {}. Wysokość drzewa to: {}".format(key, self.height()))
        else:
            return self.root.add(key)
    def height(self):
        if self.root:
            return self.root.height()
        else:
            return 0

    def loadRemove(self, file):
        with open (file, 'r') as inp:
            tab = []
            for i in inp:
                tab = i.split()
            for i in tab:
                self.remove(int(i))

    def remove(self, key):
        par = None
        curr = self.root
        while curr and curr.key != key:
            if curr.key < key:
                par = curr
                curr = curr.right
            else:
                par = curr
                curr = curr.left
        if curr is None:
            return print("Klucz {} nie występuje w drzewie.".format(key))
        if curr.left is None and curr.right is None:
            if par.left == curr:
                par.left = None
            else:
                par.right = None
            return print("Usunięto klucz {} z drzewa. Wysokość drzewa to: {}".format(key, self.height()))
        elif curr.left and curr.right is None:
            if par.left == curr:
                par.left = curr.left
            else:
                par.right = curr.left
            return print("Usunięto klucz {} z drzewa. Wysokość drzewa to: {}".format(key, self.height()))
        elif curr.left is None and curr.right:
            if par.left == curr:
                par.left = curr.right
            else:
                par.right = curr.right
            return print("Usunięto klucz {} z drzewa. Wysokość drzewa to: {}".format(key, self.height()))
        else:
            dpar = curr
            dcurr = curr.right
            while dcurr.left:
                dpar = dcurr
                dcurr = dcurr.left
            curr.key = dcurr.key
            if dcurr.right:
                if dpar.key > dcurr.key:
                    dpar.left = dcurr.right
                elif dpar.key < dcurr.key:
                    dpar.right = dcurr.right
            else:
                if dcurr.key < dpar.key:
                    dpar.left = None
                else:
                    dpar.right = None
            return print("Usunięto klucz {} z drzewa. Wysokość drzewa to: {}".format(key, self.height()))


            
tree = Tree()
tree.load("keysInsert.txt")
print(" ")
tree.loadRemove("keysDelete.txt")