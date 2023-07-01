#sqr.py

def sqr():
    masuk1 = input()
    awal = "B"*100
    akhir = "B"*100
    masuk1 = awal + masuk1 + akhir
    masuk2 = "B" * len(masuk1)
    masuk3 = masuk2
    masuk4 = masuk2
    masuk5 = masuk2
    index1, index2, index3, index4, index5 = 100, 100, 100, 100, 100
    tape1 = list(masuk1)
    tape2 = list(masuk2)
    tape3 = list(masuk3)
    tape4 = list(masuk4)
    tape5 = list(masuk5)
    state = "q0"
    print(tape1[index1-30:index1 + 5])
    print(tape2[index2-30:index2 + 5])
    print(tape3[index3-30:index3 + 5])
    print(tape4[index4-30:index4 + 5])
    print(tape5[index5-30:index5 + 5])
    print("state : " + state)
    dict1 = {
        "q0" : [["1BBBB", "1BBB1", "SSSSS", "q1"]],
        "q1" : [["1BBB1", "11BB1", "SRSSL", "q1"], ["1BBBB", "1CBBB", "SRSSR", "q2"]],
        "q2" : [["1BBB1", "11BB1", "SRSSR", "q2"], ["1BBBB", "1CBBB", "SLSSS", "q3"]],
        "q3" : [["11BBB", "111BB", "SLRSS", "q3"], ["1BBBB", "1CBBB", "SLLSS", "q4"]],
        "q4" : [["111BB", "1111B", "SSLRS", "q4"], ["11BBB", "11BBB", "SRLSS", "q5"], ["1B1BB", "1B1BB", "SRSLS", "q6"]],
        "q5" : [["111BB", "1111B", "SSRRS", "q5"], ["11BBB", "11BBB", "SLLSS", "q4"], ["1B1BB", "1B1BB", "SRSLS", "q6"]],
        "q6" : [["1111B", "1111B", "SSLSS", "q6"], ["11B1B", "11B1B", "SSRSS", "q7"]],
        "q7" : [["1111B", "110BB", "RSSLS", "q7"], ["111BB", "111BB", "LSSLS", "q8"], ["B111B", "B1111", "SSSSL", "q10"], ["B11BB", "B11BB", "SSSSS", "q11"]],
        "q8" : [["11BBB", "100BB", "LRRLS", "q8"], ["11BBB", "1C0BB", "LRRLS", "q8"], ["01BBB", "00BBB", "RRSRS", "q9"]],
        "q9" : [["111BB", "000BB", "SRRSR", "q9"], ["1BBBB", "1BBB1", "SSSSS", "q0"]],
        "q10" : [["B1111", "B1110", "SSSSS", "q10"]],
        "q11" : [[]]
        }

    while (1):
        i = 0
        while (i < len(dict1[state])):
            #print(i)
            if(tape1[index1] + tape2[index2] + tape3[index3] + tape4[index4] + tape5[index5] == dict1[state][i][0]):
                tape1[index1] = dict1[state][i][1][0]
                tape2[index2] = dict1[state][i][1][1]
                tape3[index3] = dict1[state][i][1][2]
                tape4[index4] = dict1[state][i][1][3]
                tape5[index5] = dict1[state][i][1][4]
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
                if(dict1[state][i][2][4] == "R"):
                    index5 += 1
                elif(dict1[state][i][2][4] == "L"):
                    index5 -= 1
                state = dict1[state][i][3]
                print(tape1[index1-30:index1 + 5])
                print(tape2[index2-30:index2 + 5]) 
                print(tape3[index3-30:index3 + 5])
                print(tape4[index4-30:index4 + 5])
                print(tape5[index5-30:index5 + 5])
                print("state : " + state)
                if state == "q11":
                    exit("Diterima, hitung jumlah 0 di tape 4")
                break  
            i += 1 
            if i >= len(dict1[state]):
                exit("Tolak")