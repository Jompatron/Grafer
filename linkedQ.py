class LinkedQ:

    class Node:
        #Bestämmer vart de olika pekarna pekar
        def __init__(self, element, _next):
            self._next = _next
            self.element = element

    #Bestämmer ordningen på noderna
    def __init__(self):
        self._first = None
        self._last = None
        self.size = 0

    #Returnerar storleken på den länkade listan
    def __len__(self):
        return self.size

    #Tar bort det element som är först i listan
    def dequeue(self):
        result = self._first.element
        self._first = self._first._next #ändrar pekaren till att nästa element blir det första
        self.size -= 1
        if self.isEmpty():
            self._last = None
        return result

    # Lägger till det element som varit först i listan sist istället
    def enqueue(self, element):
        new = self.Node(element, None)  # Skapar ny nod med element pekar på None
        if self.isEmpty():
            self._first = new  # om kön är tom blir nya noden första noden
        else:
            self._last._next = new  # om det finns i kön läggs noden till sist
        self._last = new
        self.size += 1

    #Kollar om kön är tom
    def isEmpty(self):
        return self.size == 0