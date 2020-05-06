class List(object):

    def __init__(self,root=None):
        self.lt=[]
        self.start = 0
        if root!=None:
            self.lt.append(root)

    def size(self):
        return len(self.lt)
    def remove(self,value):
        self.lt.remove(value)

    def isEmpty(self):
        if self.size == 0:
            return True
        return  False
    # def to_list(self):
    #     return self.lt
    # def from_list(self,):
    def from_list(self,lft):
        if len(lft)==0:
            return self
        else:
            for i in lft:
                self.add_to_tail(i)
            return self


    def add_to_head(self,value):

        self.lt.insert(0, value)

    def _last_node(self):
        return self.lt[self.size()-1]

    def add_to_tail(self,value):
        self.lt.append(value)

    def str(self):
        for i in range(len(self.lt)):
            print(self.lt[i])
    def map(self,f):
        for i in range(self.size()):
            cur = self.lt[i]
            self.lt[i] = f(cur)
    def reduce(self,f,initial_state):
        state = initial_state
        for i in range(self.size()):
            cur = self.lt[i]
            state = f(state,cur)
        return state

    def findAll(self, elem):
        l = []
        for i in range(len(self.lt)):  # 遍历数组
            if self.lt[i] == elem:
                l.append(i)  # 找到就将索引添加进ret_list
        return l

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lt) == self.size():
           raise StopIteration
        tmp = self.lt[self.start]
        self.start += 1
        return tmp









