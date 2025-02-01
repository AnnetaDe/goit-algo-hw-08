# heapq.heappush(heap, item)	Inserts item into the heap
# heapq.heappop(heap)	Removes & returns smallest item
# heapq.heapify(iterable)	Converts a list into a heap
# heapq.heappushpop(heap, item)	Pushes item and pops smallest
# heapq.nlargest(n, iterable)	Returns n largest elements
# heapq.nsmallest(n, iterable)	Returns n smallest elements

import heapq


class PriorityQueue:
    def __init__(self):
        self.queque=[]
    def enqueue(self, task, priority):
        heapq.heappush(self.queque,(-priority,task) )
    def dequeue(self):
        return heapq.heappop(self.queque)[1]
    def is_empty(self):
        return not bool(self.queque)
        
        
