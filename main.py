from linkedQ import LinkedQ

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinTree:
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):
        return finns(self.root, value)

    def write(self):
        skriv(self.root)
        print("\n")


def putta(rot, newvalue):
    if rot is None:
        return Node(newvalue)
    elif newvalue < rot.data:
        rot.left = putta(rot.left, newvalue)
    elif newvalue > rot.data:
        rot.right = putta(rot.right, newvalue)
    return rot


def finns(node, newvalue):
    if node is None:
        return False
    elif node.data == newvalue:
        return True
    elif node.data < newvalue:
        return finns(node.right, newvalue)
    elif node.data > newvalue:
        return finns(node.left, newvalue)


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


def makechilder(startord):
    """
    Byter ut en bokstav i taget: startord -> slutord
    :param startord: ord med tre bokstäver
    :return:en lista med alla barn till startordet
    """
    start = ["startord"]
    alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l","m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
    words = [] #alla orden man får genom att bara byta en bokstav från startordet dvs stardordets barn
    for i in range(len(alfa)):
        x = startord.replace(startord[0], alfa[i], 1)
        y = startord.replace(startord[1], alfa[i], 1)
        z = startord.replace(startord[2], alfa[i], 1)
        if x not in words:
            words.append(x)
        if y not in words:
            words.append(y)
        if z not in words:
            words.append(z)
    words.remove(startord)
    return words

def makechildern(word, q):
    pass


def main():
    svenska = BinTree()
    gamla = BinTree()
    print("Här skrivs dubletterna i svenska ut: ")
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet in svenska:
                pass #gamla.put(ordet)
            else:
                svenska.put(ordet)
    print("startord:")
    startord = input().strip()
    #print("slutord:")
    #slutord = input().strip()
    words = makechilder(startord)
    for i in words:
        if i in svenska:
            print(i)
        else:
            gamla.put(i)
    print("\n")
    #q = LinkedQ
    #q.enqueue(startord)
    #while not q.isEmpty():
     #   word = q.dequeue()
      #  makechilder(word, q)

if __name__ == '__main__':
    main()