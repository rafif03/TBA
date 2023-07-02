#fac.py

def fac():
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
        "q0" : [["0BBB", "000B", "RRRS", "q1"], ["!BBB", "1BB0", "SSSS", "q11"]],
        "q1" : [["0BBB", "0B0B", "SSRS", "q2"], ["!BBB", "1BB0", "SSSS", "q11"]],
        "q2" : [["0BBB", "0BBB", "SLLS", "q3"]],
        "q3" : [["000B", "0000", "SRSR", "q3"], ["0B0B", "0B0B", "SLSS", "q4"], ["00BB", "00BB", "RSSS", "q5"]],
        "q4" : [["000B", "000B", "SLSS", "q4"], ["0B0B", "0B0B", "SRLS", "q3"]],
        "q5" : [["!0BB", "!0BB", "SSSS", "q11"], ["00BB", "00BB", "SSSS", "q6"]],
        "q6" : [["00BB", "0BBB", "SRSS", "q6"], ["0BBB", "0BBB", "SSSL", "q7"]],
        "q7" : [["0BB0", "00BB", "SRSL", "q7"], ["0BBB", "0BBB", "SSSS", "q8"]],
        "q8" : [["0BBB", "0B0B", "SSSS", "q9"]],
        "q9" : [["0B0B", "0B0B", "SSRS", "q9"], ["0BBB", "0BBB", "SLSS", "q10"]],
        "q10" : [["00BB", "00BB", "SLSS", "q10"], ["0BBB", "0BBB", "SRLS", "q3"]],
        "q11" : [[]]
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
                if state != "q0":
                    print("Diterima, hitung jumlah 0 di tape 4")
                break  
            i += 1 
            if i >= len(dict1[state]):
                print("Tolak")
                return