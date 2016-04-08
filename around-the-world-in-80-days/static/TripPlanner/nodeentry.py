class NodeEntry:
    """Class to hold a node and its predecessor."""

    def __init__(self, node, pred):
        """Create new NodeEntry."""
        self._node = node
        self._pred = pred

    def __str__(self):
        """Convert NodeEntry to a string (allows printing)."""
        return "<NodeEntry: node: %s pred: %s>" % (self._node, self._pred)

    def get_node(self):
        """Return node."""
        return self._node

    def get_predecessor(self):
        """Return predecessor."""
        return self._pred

    def get_edge(self):
        """Return edge from predecessor to node."""
        return (self._pred, self._node)

def nodes_equal(n1, n2):
    """Returns true if the nodes of two NodeEntry objects are equal."""
    return n1.get_node() == n2.get_node()

class NodeEntryList:
    """
    Class to hold a list of NodeEntry objects.  Useful for the visited
    list.
    """

    def __init__(self):
        """Create a new NodeEntryList."""
        self._list = []

    def insert(self, ndentry):
        """Insert a NodeEntry."""
        self._list.append(ndentry)

    def has_node(self, node):
        """Check if node is a member of the NodeEntryList."""
        for ndentry in self._list:
            if node == ndentry.get_node():
                return True
        return False

class RAC:
    """
    Abstract base class for a Restricted Access Container.
    You cannot create any useful objects of this class.  You
    should create subclasses that inherit from RAC to create
    specific types of restricted access containers (such as
    stacks, queues, and priority queues).
    """

    def insert(self, item):
        """Insert item.  Kick out any duplicates."""
        raise NotImplementedError

    def remove(self):
        """Remove item."""
        raise NotImplementedError

    def clear(self):
        """Remove all items from the container."""
        raise NotImplementedError

    def __len__(self):
        """Return number of items in the container."""
        raise NotImplementedError
 
#############################################################################
# All modifications to this file should be below this line
#############################################################################

# TODO: fill out the class definitions needed for Problem 1a and 1b below.
# Use the documentation style shown in the class definitions above

#############################################################################
# Problem 1a: Definition of class NodeEntryStack 
#############################################################################

class NodeEntryStack(RAC):
    
    def __init__(self):
        """Create a new NodeEntryStack"""
        self._stack=[]
        
    def __len__(self):
        """Return number of elements in stack"""
        return len(self._stack)
    
    def clear(self):
        """Clear all elements in stack i.e empty stack"""
        self._stack=[]
     
    def insert(self,A):
        """Push an element of type NodeEntry onto top of stack"""
        for i in self._stack:
            if i.get_node()==A.get_node():
                self._stack.remove(i)
        self._stack.append(A)
    
    def remove(self):
        """Pops off topmost element form stack"""
        if len(self._stack)>0:
            return self._stack.pop()
        return False #Return Fail
#############################################################################
# Problem 1b: Definition of class NodeEntryQueue
#############################################################################

class NodeEntryQueue(RAC):

    def __init__(self):
        """Creates a new queue"""
        self._queue=[]

    def __len__(self):
        """Return number of elements in queue"""
        return len(self._queue)

    def clear(self):
        """Clear all elements in queue i.e empty queue"""
        self._queue=[]

    def insert(self,A):
        """Push an element of type NodeEntry onto end of queue"""
        self._queue.append(A)

    def remove(self):
        """Pops off topmost element form queue (FIFO)"""
        if len(self._queue)>0:
            return self._queue.pop(0)
        return False
        
#############################################################################
# Problem 4a: Definition of class DistNodeEntry
#############################################################################

class DistNodeEntry(NodeEntry):

    def __init__(self, node, pred,g,f):
        """Create new DistNodeEntry."""
        self._node = node
        self._pred = pred
        self._g=g
        self._f=f
    
    def __str__(self):
        """Convert DistNodeEntry to a string (allows printing)."""
        return "<NodeEntry: node: %s pred: %s g cost: %s f cost: %s>" % (self._node, self._pred, self._g, self._f)
        
    def get_g(self):
        """Get the g cost associated with the node"""
        return self._g
     
    def get_f(self):
        """Get the f cost (h+g) associated with the node"""
        return self._f    

#############################################################################
# Problem 4b: Definition of class DistNodeEntryPQ
#############################################################################

class DistNodeEntryPQ(RAC):

    def __init__(self):
        """Creates a new DistNodeEntryPQ"""
        self._PQ=[]
    
    def __len__(self):
        """Return number of elements in priority queue"""
        return len(self._PQ)
        
    def clear(self):
        """Clear all elements in queue i.e empty priority queue"""
        self._PQ=[]
        
    def prioritize(self):
        """Sort the elements in queue by their f-value (g+h)"""
        for i in range(len(self._PQ)-1):
            for j in range(i,len(self._PQ)):
                if self._PQ[i].get_f()>self._PQ[j].get_f():
                    #Swap
                    tmp=self._PQ[i]
                    self._PQ[i]=self._PQ[j]
                    self._PQ[j]=tmp
        # print [i.get_node() for i in self._PQ]
        
    def insert(self,A):
        """Push an element of type NodeEntry onto end of priority queue"""
        flag=True
        for i in range(len(self._PQ)):
            if self._PQ[i].get_node()==A.get_node():
                if self._PQ[i].get_g()>A.get_g():
                    self._PQ[i]=A
                flag=False
        if flag == True:
            self._PQ.append(A)
        self.prioritize() 
        
    def remove(self):
        """Pops off topmost element form queue"""
        if len(self._PQ)>0:
            return self._PQ.pop(0)
        return False