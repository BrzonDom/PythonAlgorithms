"""
Dekódování zprávy

    Dekódujde zprávu ze standardního vstupu pomocí zásobníku:
        Písmeno znamená push znaku na zásobník
        Hvězdička znamená pop znaku ze zásobníku na výstup
        Mezery se ignorují

    Dekódujte následující vstup

        TE*A*QYS***SEU****NI*O**

"""

coded = "TE*A*QYS***SEU****NI*O**"
decoded = ""

decode_stack = []
stack_log = []
i = 1

print()
print(f"Coded:   {coded}")

for char in coded:

    # print(f"{i:2}: {decode_stack}")
    stack_log.append(f"{i:2}: {decode_stack}")
    i += 1

    if char == '*':
        # print(decode_stack.pop(), end="")
        decoded += decode_stack.pop()
    else:
        # decode_stack.insert(0, char)
        decode_stack.append(char)

print(f"Decoded: {decoded}")

print("\nStack log:")

for line in stack_log:
    print(f"\t{line}")

