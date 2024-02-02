"""
Lehká varianta: Babylonská věž (zjednodušená)

    Babylonská věž (hlavolam): hlavolam obsahující celkem 35 kuliček o 6 různých barvách (5 barev má 6 kuliček, 1 barva má pouze 5), které jsou uspořádány v 6×6 poli. Cílem hlavolamu je srovnat kuličky tak, aby každý sloupec obsahoval pouze kuličky jedné barvy a nebo prázdné místo.

        Chybějící kulička umožňuje přesun sousední kuličky na prázdné místo.
        Věž je cyklická v horizontálním směru. To znamená, že lze rotovat celým řádkem. To umožňuje posunutí vlevo či vpravo všech kuliček v jednom řádku.

    Babylonská věž (v ALP):

        Stejný problém, avšak ne pro věž o rozměrech 6×6, ale menší a také nečtvercové.
        Reprezentována 2D maticí.
        Kuličky jedné barvy mají stejný odstín. Není třeba je ve sloupci třídit dle odstínu jako tomu je u některých verzí Babylonské věže.

    Úkol:

        Napište program babylon.py, který najde řešení zmenšené Babylónské věže v nejmenším počtu kroků.

    Vstup:

        Babylonská věž reprezentována 2D maticí o rozměrech M x N, které reprezentují:
            M: počet kuliček jedné barvy,
            N: počet barev.
        Hodnoty v matici reprezentují barvy kuliček na dané pozici takto:
            0: prázdné místo,
            1, 2, …, N: barva kuličky.
        Matice bude programu předána v argumentu programu, využijte tedy sys.argv[1].
        Příklad věže 3×3 (tedy 3 barvy, každá po 3 kuličkách, krom barvy 3, která má kuličky pouze 2):

        1 2 3
        1 2 0
        2 1 3


    Povolené akce:

        Pro zjednodušení v ALP je v každém stavu věže (neboli uspořádání kuliček) možné využít pouze těchto 4 akcí:
            Rotace řádku vpravo: posun všech kuliček n-tého řádku o 1 doprava.
                Značení: r n 1 (rotace řádku s indexem n o 1 vpravo)
            Rotace řádku vlevo: posun všech kuliček n-tého řádku o 1 doleva.
                Značení: r n -1 (rotace řádku s indexem n o 1 vlevo)
            Přesun kuličky nahoru do prázdného místa.
                Značení: m -1 (posun kuličky pod prázdným místem nahoru)
                Pozor: lze aplikovat pouze pokud prázdné místo není ve spodní řadě
            Přesun kuličky dolů do prázdného místa.
                Značení: m 1 (posun kuličky nad prázdným místem dolů)
                Pozor: lze aplikovat pouze pokud prázdné místo není v horní řadě

"""
import copy
from queue import Queue

class State:
    def __init__(self, state, action = None, parent = None):
        self.state = copy.deepcopy(state)
        self.parent = parent
        self.action = action

    def nextState(self):
        nextTower_lst = []

        rowTow = len(self.state)
        for row in range(rowTow):

            next = right(self, row)
            nextTower_lst.append(next)

            next = left(self, row)
            nextTower_lst.append(next)

        next = up(self)
        nextTower_lst.append(next)

        next = down(self)
        nextTower_lst.append(next)

        return nextTower_lst


def right(orgTower, row):
    tower = copy.deepcopy(orgTower)

    tower.state[row] = tower.state[row][-1:] + tower.state[row][:-1]
    return tower


def left(orgTower, row):
    tower = copy.deepcopy(orgTower)

    tower.state[row] = tower.state[row][1:] + tower.state[row][:1]
    return tower


def up(orgTower):
    tower = copy.deepcopy(orgTower)
    # for row in tower[:-1]:
    #     for col in row:
    #         if col == 0:

    for r in range(len(tower.state)-1):
        for c in range(len(tower.state[0])):
            if tower.state[r][c] == 0:
                tower.state[r][c], tower.state[r+1][c] = tower.state[r+1][c], tower.state[r][c]
                return tower
    return tower


def down(orgTower):
    tower = copy.deepcopy(orgTower)

    for r in range(1, len(tower.state)):
        for c in range(len(tower.state[0])):
            if tower.state[r][c] == 0:
                tower.state[r][c], tower.state[r-1][c] = tower.state[r-1][c], tower.state[r][c]
                return tower
    return tower


def solved(curTow):

    row = len(curTow)
    col = len(curTow[0])

    for c in range(col):
        sameChk = True
        for r in range(row):
            if curTow[r][c] == 0:
                continue

            if sameChk:
                same = curTow[r][c]
                sameChk = False

            elif same != curTow[r][c]:
                return False

    return True


def BFS(strSta):

    queue = Queue()
    queue.put(strSta)

    visited = {}
    visited[str(strSta.state)] = True

    while not queue.empty():

        curSta = queue.get()

        if solved(curSta.state):
            print("SOLVED")

            return curSta.state

        for next in State.nextState(curSta):
            if not str(next.state) in visited:

                visited[str(next.state)] = True
                queue.put(next)


org_tower = [[1, 2, 3],
         [1, 2, 0],
         [2, 1, 3]]

print("Original tower:")
print()

for row in org_tower:
    for col in row:
        print(col, end=" ")
    print()
print()

orgState = State(org_tower)


print("Right:", end="\n\t")

tower = right(orgState, 1)

for row in tower.state:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()

print("Left:", end="\n\t")

tower = left(orgState, 1)

for row in tower.state:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()

print("Up:", end="\n\t")

tower = up(orgState)

for row in tower.state:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()

print("Down:", end="\n\t")

tower = down(orgState)

for row in tower.state:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()
print()

slv_tower = BFS(orgState)
