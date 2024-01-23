
from Queue import ALP_Queue

"""
Queue
    Standardní knihovna Pythonu nabízí modul queue
    I tato fronta umožňuje pracovat s prvky různých datových typů
"""

queue = ALP_Queue()
queue.put("first")
queue.put("2")
queue.put(3.0)

while not queue.empty():
    print(queue.get())

