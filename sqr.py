#sqr.py

def sqr():
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
    print(tape1[index1-10:index1 +15])
    print(tape2[index2-10:index2 +15])
    print(tape3[index3-10:index3 +15])
    print(tape4[index4-10:index4 +15])
    print("state : " + state)
    dict1 = {
        "q0" : [["1BBB", "1111", "RSSR", "q1"]],
        "q1" : [["111B", "111B", "RSSS", "q2"], ["B11B", "B11B", "SRRS", "q4"]],
        "q2" : [["B11B", "B11B", "SRRS", "q4"], ["111B", "111B", "RSSS", "q3"]],
        "q3" : [["B11B", "B11B", "SRRS", "q3"], ["111B", "111B", "SSSS", "q5"], ["BBBB", "BBBB", "LLLS", "q3"]],
        "q4" : [[]],
        "q5" : [["111B", "111B", "LLLS", "q5"], ["1BBB", "1BBB", "LSSS", "q5"], ["BBBB", "BBBB", "RRRS", "q6"]],
        "q6" : [["111B", "111B", "RSRS", "q6"], ["11BB", "11BB", "SRLS", "q7"], ["1BBB", "1BBB", "SSSS", "q8"], ["1B1B", "1B1B", "SSRS", "q8"], ["BBBB", "BBBB", "SSSS", "q9"], ["B11B", "B11B", "SSSS", "q9"], ["B1BB", "B1BB", "SSSS", "q9"], ["BB1B", "BB1B", "SSSS", "q9"]],
        "q7" : [["111B", "111B", "RSLS", "q7"], ["11BB", "11BB", "SRRS", "q6"], ["1BBB", "1BBB", "SSSS", "q8"], ["1B1B", "1B1B", "SSRS", "q8"], ["BBBB", "BBBB", "SSSS", "q10"], ["B11B", "B11B", "SSSS", "q10"], ["B1BB", "B1BB", "SSSS", "q10"], ["BB1B", "BB1B", "SSSS", "q10"]],
        "q8" : [["1B1B", "1B1B", "SSRS", "q8"], ["1BBB", "1111", "SSSR", "q5"]],
        "q9" : [["BBBB", "BBBB", "SSSS", "q11"], ["B11B", "B11B", "SRRL", "q11"], ["B1BB", "B1BB", "SRSL", "q11"], ["BB1B", "BB1B", "SSRL", "q11"]],
        "q10" : [["BBBB", "BBBB", "SSSS", "q12"], ["B11B", "B11B", "SRRL", "q12"], ["B1BB", "B1BB", "SRSL", "q12"], ["BB1B", "BB1B", "SSRL", "q12"]],
        "q11" : [["BBBB", "BBBB", "SSSS", "q13"], ["BBB1", "BBB1", "SSSS", "q13"], ["B111", "B11B", "SSSS", "q13"], ["B1B1", "B1BB", "SSSS", "q13"], ["BB11", "BB1B", "SSSS", "q13"]],
        "q12" : [["BBBB", "BBBB", "SSSS", "q13"], ["BBB1", "BBB1", "SSSS", "q13"], ["B111", "B11B", "SSSS", "q13"], ["B1B1", "B1BB", "SSSS", "q13"], ["BB11", "BB1B", "SSSS", "q13"]],
        "q13" : [[]]
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
                print(tape1[index1-10:index1 +15])
                print(tape2[index2-10:index2 +15]) 
                print(tape3[index3-10:index3 +15])
                print(tape4[index4-10:index4 +15])
                print("state : " + state)
                if state == "q13":
                    print("Diterima, hitung jumlah 1 di tape 4")
                    return
                elif state == "q4":
                    print("Diterima, hitung jumlah 1 di tape 4")
                    return
                break
            i += 1 
            if i >= len(dict1[state]):
                print("Tolak")
                return