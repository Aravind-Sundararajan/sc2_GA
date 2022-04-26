class CVector(CMemPoolNode):
    def __init__(self):
        self.m_size = None
        self.m_capacity = None
        self.m_capacityIndex = None
        self.m_data = None
        self.m_memoryPool = None
        self.m_memoryPools = None

    def size(self):
        pass

    def capacity(self):
        pass

    def append(self):
        pass

    def push_back(self):
        pass

    def push_back_uninitialized(self):
        pass

    def insert(self):
        pass

    def clear(self):
        pass

    def erase(self):
        pass

    def capacity(self):
        pass

    def push(self):
        pass

    def pop(self):
        pass

    def pop_front(self):
        pass

    def truncate(self):
        pass

    def binarySearch(self):
        pass

    def __getitem__(self, i):
        """
        operator overloading []
        """
        return self.m_data[i]

    def data(self):
        return self.m_data

    def RemoveAllPointer(self):
        pass
