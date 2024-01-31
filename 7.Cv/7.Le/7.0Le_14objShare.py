
class State:
    def __init__(self, data, name):
        self.data = data
        self.name = name

    def change(self, index, newVal):
        self.data[index] = newVal

    def __repr__(self):
        return "name: " + str(self.name) + "\ndata: " + str(self.data)

log = []
data = [1, 2, 3]

for i in range(len(data)):
    log.append(State(data, i))

for line in log:
    print(line)
    print()

print()
log[0].change(2, "****")
for line in log:
    print(line)
    print()