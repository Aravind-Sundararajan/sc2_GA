from pickletools import uint8


def HashKey(key):
    return uint8(key)


class CHashtableNode(CMemPoolNode):
    def __init__(self):
        self.m_pNextNode = None
        self.m_key = None
        self.m_val = None

    def GetNext(self):
        return self.m_pNextNode

    def SetNext(self, next):
        self.m_pNextNode = next

    def __eq__(self, node):
        self.m_key = node.m_key
        self.m_val = node.m_val
        self.m_pNextNode = node.m_pNextNode


class CHashtable(CMemPoolNode):
    def __init__(self):
        self.m_comp = None
        self.m_fGrowThreshold = None
        self.m_fGrowFactor = None
        self.m_nSize = None
        self.m_nCount = None
        self.m_arrHashtable = None

    def FindKey(self):
        pass

    def SetAt(self):
        pass

    def ContainsKey(self):
        pass

    def RemoveKey(self):
        pass

    def Lookup(self):
        pass

    def GetIndex(self):
        pass

    def CloneTo(self):
        pass

    def GetStartPosition(self):
        pass

    def GetNextAssoc(self):
        pass

    def Grow(self):
        pass

    def Reallocate(self):
        pass

    def Size(self):
        pass

    def Count(self):
        pass

    def GetStatistics(self):
        pass

    def CalculateMemoryUsage(self):
        pass
