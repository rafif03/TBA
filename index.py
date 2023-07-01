from add import *
from div import *
from fac import *
from log2 import *
from mul import *
from power import *
from sub import *
from sqr import *

print("Pilih Opsi:")
print("1. Penjumlahan")
print("2. Pembagian")
print("3. Factorial")
print("4. Logaritma")
print("5. Perkalian")
print("6. Pangkat")
print("7. Pengurangan")
print("8. Akar Kuadrat")
while True:
    user_input = int(input("Enter an integer: "))
    if user_input == 1:
        print("Penjumlahan Selected")
        add()
        break
    elif user_input == 2:
        print("Pembagian Selected")
        div()
        break
    elif user_input == 3:
        print("Factorial Selected")
        fac()
        break
    elif user_input == 4:
        print("Logaritma Selected")
        log2()
        break
    elif user_input == 5:
        print("Perkalian Selected")
        mul()
        break
    elif user_input == 6:
        print("Pangkat Selected")
        power()
        break
    elif user_input == 7:
        print("Pengurangan Selected")
        sub()
        break
    elif user_input == 8:
        print("Akar Kuadrat Selected")
        sqr()
        break
    print("This number is even")