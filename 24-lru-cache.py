class DoubleNode:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.pre = None
        self.nex = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maxlen = capacity
        self.curlen = 0
        self.m = {}
        self.head = None
        self.back = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.m:
            cur_node = self.m[key]
            if self.head != cur_node:
                cur_node.pre.nex = cur_node.nex
                if self.back == cur_node:
                    self.back = cur_node.pre
                else:
                    cur_node.nex.pre = cur_node.pre
                cur_node.pre = None
                cur_node.nex = self.head
                self.head.pre = cur_node
                self.head = cur_node
            return cur_node.v
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #print(self.m, key, value)
        if key in self.m:
            self.m[key].v = value
            self.get(key)
            return
        new_node = DoubleNode(key, value)
        self.m[key] = new_node
        if self.head == None:
            self.head = new_node
            self.back = new_node
            self.curlen += 1
            return
        else:
            new_node.nex = self.head
            self.head.pre = new_node
            self.head = new_node
            if self.curlen == self.maxlen:
                key_to_delete = self.back.k
                self.back.pre.nex = None
                self.back = self.back.pre
                del self.m[key_to_delete]
            else:
                self.curlen += 1
            return
