
class ALP_Queue:
    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.insert(0, item)

    def get(self):
        return self.items.pop()

    def empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

"""
Queue
    Tato fronta implementována jako pole, tj. lze do ní vkládat prvky různých
    datových typů
"""

queue = ALP_Queue()
queue.put("first")
queue.put("2")
queue.put(3.0)

while not queue.empty():
    print(queue.get())

