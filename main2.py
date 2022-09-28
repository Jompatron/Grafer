from linkedQ import LinkedQ


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent

    def write_chain(self, parent):
        if self.parent is not None:
            ParentNode.write_chain(self.parent, self.parent.parent)
            print(self.word)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# Klassen hämtad från labbinstruktionen
class BinTree:

    def __init__(self):
        self.root = None

    def put(self, newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):
        # True om value finns i trädet, False annars
        return finns(self.root, value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


# Placerar ut noden
def putta(rot, newvalue): #newvalue kommer från svenska/engelska.put
    # Placerar ut noden utefter bokstavsordning
    if rot is None:
        return Node(newvalue) #roten är en nod, inte en int, kalla på klaseen Node (skapar rotnod)
    elif newvalue < rot.data:
        rot.left = putta(rot.left, newvalue)
    elif newvalue > rot.data:
        rot.right = putta(rot.right, newvalue)
    return rot


# Kollar om newvalue existerar i trädet, returnerar true eller false (används i searches)
def finns(node, newvalue):
    if node is None:
        return False
    elif node.data == newvalue:
        return True
    elif node.data < newvalue: #om newvalue > värdet vi är på, kommer vi gå åt höger, kollar nod till höger
        return finns(node.right, newvalue) #skickar in värdet till höger rekursivt
    elif node.data > newvalue:
        return finns(node.left, newvalue) #skickar in värdet till vänster, rekursivt


# Skriver ut trädet i ordning
def skriv(nod):
    if nod is not None:
        skriv(nod.left)
        print(nod.data)
        skriv(nod.right)


def make_tree():
    tree = BinTree()
    data = input().strip()
    while data != "#":
        print(data)
        tree.put(data)
        data = input().strip()
    return tree


def searches(tree):
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()


def makechildren(startord, q, gamla):
    lista = []
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            lista.append(ordet)

    alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l","m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]

    for i in range(len(alfa)):
        x = startord.word.replace(startord.word[0], alfa[i], 1)
        y = startord.word.replace(startord.word[1], alfa[i], 1)
        z = startord.word.replace(startord.word[2], alfa[i], 1)
        if x != startord and x in lista:
            if x not in gamla:
                q.enqueue(ParentNode(x, startord))
                gamla.put(x)
        if y != startord and y in lista:
            if y not in gamla:
                q.enqueue(ParentNode(y, startord))
                gamla.put(y)
        if z != startord and z in lista:
            if z not in gamla:
                q.enqueue(ParentNode(z, startord))
                gamla.put(z)


def main():
    svenska = BinTree()
    gamla = BinTree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet not in svenska:
                svenska.put(ordet)
    print("Ange startord: ")
    startord = input().strip()
    start = ParentNode(startord)
    gamla.put(startord)
    q = LinkedQ()
    makechildren(start, q, gamla)
    print("Ange slutord:")
    slutord = input().strip()
    slut = ParentNode(slutord)
    while not q.isEmpty():
        word = q.dequeue()
        makechildren(word, q, gamla)
        if word.word == slutord:
            print("Det finns en väg till", slutord, "från", startord + ".")
            print(startord)
            ParentNode.write_chain(word, start)
            exit()
    print("Det finns ingen väg till", slutord, "från", startord + ".")


if __name__ == '__main__':
    main()