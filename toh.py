n = int(input("Enter the number of disks in TOH : "))
disk = [i for i in range(1, n+1)]
a = []
b = []
def solveTOH(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod ", from_rod, " to rod ", to_rod)
        display(1, from_rod, to_rod)
        print('A:', disk, 'B:', a, 'C:', b)
        return
    solveTOH(n-1, from_rod, aux_rod, to_rod)
    print("Move disk ", n, " from rod ", from_rod, " to rod ", to_rod)
    display(n, from_rod, to_rod)
    print('A:', disk, 'B:', a, 'C:', b)
    solveTOH(n-1, aux_rod, to_rod, from_rod)
def display(n, from_rod, to_rod):
    if from_rod == 'A' and to_rod == 'B':
        a.append(n)
        disk.remove(n)
    elif from_rod == 'B' and to_rod == 'C':
        b.append(n)
        a.remove(n)
    elif from_rod == 'A' and to_rod == 'C':
        b.append(n)
        disk.remove(n)
    elif from_rod == 'B' and to_rod == 'A':
        disk.append(n)
        a.remove(n)
    elif from_rod == 'C' and to_rod == 'B':
        a.append(n)
        b.remove(n)
    elif from_rod == 'C' and to_rod == 'A':
        disk.append(n)
        b.remove(n)
solveTOH(n, 'A', 'C', 'B')