import os

def ejemplo ():
    os.system("cls")

    notas=[89, 94, 78, 87, 91, 100, 96, 55]
    for i in range(1,11,1):
        print("🙀"*i)

    for j in notas:
        print(f"Nota{notas.index(j)+1}: {j}")

def main():
   print("")


main()