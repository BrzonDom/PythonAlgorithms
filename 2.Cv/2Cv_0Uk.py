"""
Napište program, který načte celé číslo udávající časový interval
ve vteřinách a vypíše kolik je to dní, hodin, minut a vteřin.

Tedy pokud bude vstup 100000 pak vypíše:
    den 1 hodin 3 minut 46 vterin 40
"""


time = int(input())
# time = 100000

org_time = time

days = time // (60 * 60 * 24)

time -= days * (60 * 60 * 24)

print(f"days: {days}")

hours = time // (60 * 60)

time -= hours * (60 * 60)

print(f"hours: {hours}")

minutes = time // 60

time -= minutes * 60

print(f"minutes: {minutes}")

secunds = time

print(f"secunds: {secunds}")

print(f"\ntime: {org_time} secunds = {days} days {hours} hours {minutes} minutes {secunds} secunds")
