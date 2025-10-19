T = int(input())
for _ in range(T):
    dragonDSA, dragonTOC, dragonDM = map(int, input().split())
    slothDSA, slothTOC, slothDM = map(int, input().split())

    dragonTotal = dragonDSA + dragonTOC + dragonDM
    slothTotal = slothDSA + slothTOC + slothDM

    if dragonTotal > slothTotal:
        print("Dragon")
    elif slothTotal > dragonTotal:
        print("Sloth")
    elif dragonDSA > slothDSA:
        print("Dragon")
    elif slothDSA > dragonDSA:
        print("Sloth")
    elif dragonTOC > slothTOC:
        print("Dragon")
    elif slothTOC > dragonTOC:
        print("Sloth")
    else:
        print("Tie")
