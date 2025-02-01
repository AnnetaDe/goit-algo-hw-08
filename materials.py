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
    def display(self):
        print(self.queque)

def heap_sort(iterable):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    # Витягуємо елементи впорядковано, формуючи відсортований масив.
    return [heapq.heappop(h) for _ in range(len(h))]

# Масив для сортування
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Відсортований масив:", sorted_arr)
def heap_sort_desc(iterable):
    h = []
    # Вставляємо в купу від'ємні значення
    for value in iterable:
        heapq.heappush(h, -value)
    
    # Витягуємо елементи і міняємо знаки для відновлення оригінальних значень
    return [-heapq.heappop(h) for _ in range(len(h))]

arr = [12, 11, 13, 5, 6, 7]
sorted_arr_desc = heap_sort_desc(arr)
print("Відсортований масив (за спаданням):", sorted_arr_desc)      
pq=PriorityQueue()
pq.enqueue(("sample1.jpg", "png"), 12)  # Основний користувач
pq.display()

pq.enqueue(("premium_sample.jpg", "bmp"), 10)  # Преміум-користувач
pq.display()

pq.enqueue(("sample2.jpg", "tiff"), 1)  # Основний користувач
pq.display()
print(pq.dequeue())