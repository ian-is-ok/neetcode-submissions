class DynamicArray:
    
    def __init__(self, capacity: int):
        self.mylist = list()
        for i in range(capacity):
            self.mylist.append(None)


    def get(self, i: int) -> int:
        return self.mylist[i]


    def set(self, i: int, n: int) -> None:
        self.mylist[i] = n

    def pushback(self, n: int) -> None:
        lastseenpos = 0
        #prespos = 0
        for i in range(len(self.mylist)):
            if self.mylist[i] != None:
                lastseenpos = i
        if self.mylist[lastseenpos] == None:
            self.mylist[lastseenpos] = n
        else:
            if (lastseenpos + 1) >= len(self.mylist):
                self.resize()
                self.mylist[lastseenpos + 1] = n
            else:
                self.mylist[lastseenpos + 1] = n

    def popback(self) -> int:
        lastseenpos = 0
        for i in range(len(self.mylist)):
            if self.mylist[i] != None:
                lastseenpos = i

        result = self.mylist[lastseenpos]
        self.mylist[lastseenpos] = None
        return result

    def resize(self) -> None:
        currentcap = len(self.mylist)
        newcap = currentcap * 2
        newlist = list()
        for i in range(newcap):
            newlist.append(None)
        for j in range(currentcap):
            newlist[j] = self.mylist[j]

        self.mylist = newlist            


    def getSize(self) -> int:
        numsize = 0
        for i in range(len(self.mylist)):
            if self.mylist[i] != None:
                numsize += 1
        return numsize
    
    def getCapacity(self) -> int:
        return len(self.mylist)
