"""
Rozdíl dvou časových údajů

    Napište program, který vypočítá rozdíl dvou časů zadaných ve formátu: HH:MM:SS
"""

# time1 = input()
# time2 = input()

time1 = "03:45:30"
time2 = "02:30:21"

hou1 = int(time1.split(':')[0])
min1 = int(time1.split(':')[1])
sec1 = int(time1.split(':')[2])

hou2 = int(time2.split(':')[0])
min2 = int(time2.split(':')[1])
sec2 = int(time2.split(':')[2])


print(f"time1: {hou1}:{min1}:{sec1}")
print(f"time2: {hou2}:{min2}:{sec2}\n")

sec_time1 = (hou1 * 60*60) + (min1 * 60) + sec1
sec_time2 = (hou2 * 60*60) + (min2 * 60) + sec2

dif = abs(sec_time1 - sec_time2)

hours = dif // (60 * 60)

dif -= hours * (60 * 60)

print(f"hours: {hours}")

minutes = dif // 60

dif -= minutes * 60

print(f"minutes: {minutes}")

secunds = dif

print(f"secunds: {secunds}")

print(f"Difference: {hours} hours {minutes} minutes {secunds} secunds = {hours:02d}:{minutes:02d}:{secunds:02d}")
