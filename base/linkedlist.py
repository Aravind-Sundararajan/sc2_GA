class linkedlist(CMemPoolNode):
    def __init__(self):
        self.m_data = []
        self.m_pNext = None

    def GetData(self):
        return self.m_data

    def SetData(self, d):
        self.m_data = d

    def GetNext(self):
        return self.m_pNext

    def SetNext(self, n):
        self.m_pNext = n

    def InsertOrdered(self):
        pass

    def ReOrder(self):
        pass
