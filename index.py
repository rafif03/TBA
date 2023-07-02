from add import *
from div import *
from fac import *
from log2 import *
from mul import *
from power import *
from sub import *
from sqr import *

while True:
    print("\nSIMPLE TURING MACHINE")
    print("Pilih Opsi:")
    print("1. Penjumlahan")
    print("2. Pembagian")
    print("3. Factorial")
    print("4. Logaritma")
    print("5. Perkalian")
    print("6. Pangkat")
    print("7. Pengurangan")
    print("8. Akar Kuadrat")
    print("9. Keluar Program")
    user_input = int(input("Enter an integer: "))
    if user_input == 1:
        print("Penjumlahan Selected")
        print("input: 0+0, 0+1, 1+1, 1+0")
        add()
    elif user_input == 2:
        print("Pembagian Selected")
        print("input: 0/0, 0/1, 1/1, 1/0")
        div()
    elif user_input == 3:
        print("Factorial Selected")
        print("input: 0!")
        fac()
    elif user_input == 4:
        print("Logaritma Selected")
        print("input: 0^n")
        log2()
    elif user_input == 5:
        print("Perkalian Selected")
        print("input: 0*0, 0*1, 1*0, 1*1")
        mul()
    elif user_input == 6:
        print("Pangkat Selected")
        print("input: 0^(0^n-1)")
        print("contoh: 2^2 -> 00^0")
        power()
    elif user_input == 7:
        print("Pengurangan Selected")
        print("input: 0-0, 0-1, 1-1, 1-0")
        sub()
    elif user_input == 8:
        print("Akar Kuadrat Selected")
        print("input: 1^n")
        sqr()
    elif user_input == 9:
        print("Terimakasih!")
        break
    else:
        print("Input salah!")
