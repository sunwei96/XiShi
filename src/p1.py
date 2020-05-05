

class List(object):

    def __init__(self,root=None):
        self.lt=[]
        if root!=None:
            self.lt.append(root)

    def size(self):
        return len(self.lt)

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
    def to_list(self):
        res = []
        if len(self.lt)==0:
            return res
        else:
            for i in range(len(self.lt)):
                cur = self.lt[i]
                res.append(cur.value)
            return res

    def add_to_head(self,value):

        self.lt.insert(0,  Node(value))

    def _last_node(self):
        return self.lt[self.size()-1]

    def add_to_tail(self,value):
        self.lt.append(Node(value))

    def str(self):
        for i in range(len(self.lt)):
            print(self.lt[i].value)
    def map(self,f):
        for i in range(self.size()):
            cur = self.lt[i]
            cur.value = f(cur.value)
    def reduce(self,f,initial_state):
        state = initial_state
        for i in range(self.size()):
            cur = self.lt[i]
            state = f(state,cur.value)
        return state

class Node(object):
    def __init__(self, value):
        self.value = value




