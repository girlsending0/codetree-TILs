### Queue


from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()
    
    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq[0]
    
    def show(self):
        return list(self.dq)  # Convert deque to list and return it




# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
q = Queue()
results = []
new_q = Queue()


for num in range(1, n+1):
    q.push(num)


while q.size() >= 1:
    for _ in range(k-1):
        q.push(q.front())
        q.pop()    
    results.append(q.pop())

for i in results:
    print(i, end=" ")