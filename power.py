#power.py

def power():
    masuk1 = input()
    awal = "B"*100
    akhir = "B"*100
    masuk1 = awal + masuk1 + akhir
    masuk2 = "B" * len(masuk1)
    masuk3 = masuk2
    masuk4 = masuk2
    index1, index2, index3, index4 = 100, 100, 100, 100
    tape1 = list(masuk1)
    tape2 = list(masuk2)
    tape3 = list(masuk3)
    tape4 = list(masuk4)
    state = "q0"
    print(tape1[index1-30:index1 + 5])
    print(tape2[index2-30:index2 + 5])
    print(tape3[index3-30:index3 + 5])
    print(tape4[index4-30:index4 + 5])
    print("state : " + state)
    dict1 = {
        "q0" : [["0BBB", "000B", "RRRS", "q0"], ["^BBB", "^BBB", "RLLS", "q1"]],
        "q1" : [["000B", "X00B", "SSSS", "q2"], ["B00B", "X00B", "SSSS", "q8"], ["BBBB", "BBBB", "SSSS", "q9"], ["0BBB", "0BBB", "SSSS", "q9"], ["100B", "1000", "SSSS", "q9"], ["1BBB", "1BB0", "SSSS", "q9"]],
        "q2" : [["X00B", "XX0B", "SSSS", "q3"]],
        "q3" : [["XX0B", "XXX0", "SSLR", "q3"], ["XXBB", "XXBB", "SSRS", "q4"]],
        "q4" : [["XXXB", "XX0B", "SSRS", "q4"], ["XXBB", "XXBB", "SLLS", "q5"]],
        "q5" : [["X00B", "XX0B", "SSSS", "q3"], ["XB0B", "XB0B", "RRSL", "q6"]],
        "q6" : [["0X00", "XX00", "SSSS", "q7"], ["BX00", "BX00", "SSSS", "q9"]],
        "q7" : [["XX00", "X00B", "SRSL", "q7"], ["XB00", "X00B", "SRSL", "q7"], ["XB0B", "XB0B", "SLSS", "q2"]],
        "q8" : [["X00B", "X000", "SSLR", "q8"], ["X0BB", "X0BB", "SSSS", "q9"]],
        "q9" : [[]]
        }

    while (1):
        i = 0
        while (i < len(dict1[state])):
            #print(i)
            if(tape1[index1] + tape2[index2] + tape3[index3] + tape4[index4] == dict1[state][i][0]):
                tape1[index1] = dict1[state][i][1][0]
                tape2[index2] = dict1[state][i][1][1]
                tape3[index3] = dict1[state][i][1][2]
                tape4[index4] = dict1[state][i][1][3]
                if(dict1[state][i][2][0] == "R"):
                    index1 += 1
                elif(dict1[state][i][2][0] == "L"):
                    index1 -= 1
                if(dict1[state][i][2][1] == "R"):
                    index2 += 1
                elif(dict1[state][i][2][1] == "L"):
                    index2 -= 1
                if(dict1[state][i][2][2] == "R"):
                    index3 += 1
                elif(dict1[state][i][2][2] == "L"):
                    index3 -= 1
                if(dict1[state][i][2][3] == "R"):
                    index4 += 1
                elif(dict1[state][i][2][3] == "L"):
                    index4 -= 1
                state = dict1[state][i][3]
                print(tape1[index1-30:index1 + 5])
                print(tape2[index2-30:index2 + 5]) 
                print(tape3[index3-30:index3 + 5])
                print(tape4[index4-30:index4 + 5])
                print("state : " + state)
                if state == "q9":
                    exit("Diterima, hitung jumlah 0 di tape 4")
                break  
            i += 1 
            if i >= len(dict1[state]):
                exit("Tolak")