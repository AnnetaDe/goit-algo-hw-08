import heapq
from random import randint

def min_connect(cables):
    heapq.heapify(cables)
    total=0
    
    while len(cables)>1:
        first=heapq.heappop(cables)
        second=heapq.heappop(cables)
        
        cost_of_two=first+second
        total+=cost_of_two
        print(f"we joined two cables with lengths {first} and {second}")
        heapq.heappush(cables,cost_of_two)
    print(total)
    return total



if __name__=="__main__":
    promt=int(input("enter quantity of cables with random lengths-->"))
    
    cables=[randint(1,100) for _ in range(promt)]
    print(f"Here we go our cables to connect with minimal expenses\n {cables}")
    min_connect(cables)