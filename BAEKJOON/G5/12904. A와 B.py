S = input()
T = input()

while True:
    if T[-1] == "A":
        T = T[:-1]
    else:
        T = T[:-1][::-1]

    if len(S) == len(T):
        break

if S == T:
    print(1)
else:
    print(0)