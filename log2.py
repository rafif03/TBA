# log2.py

def log2():
    import sys
    masuk1 = input()
    awal = "BBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    akhir = "BBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    masuk1 = awal + masuk1 + akhir
    masuk2 = "B" * len(masuk1)
    index1, index2 = 28, 28
    tape1 = list(masuk1)
    tape2 = list(masuk2)
    state = "qm"
    print(tape1[index1-10:index1 + 10])
    print(tape2[index2-10:index2 + 10])
    print("state : " + state)

    dict1 = {
        "qm" : [["0B", "0M", "SR", "qs"]],
        "qs" : [["0B", "0B", "RS", "q0"]], 
        "q0" : [["0B", "00", "RS", "q0"], ["00", "00", "RR", "q0"], ["B0", "B0", "LL", "q1"], ["BB", "BB", "LL", "q1"]], 
        "q1" : [["0B", "BB", "LL", "q1"], ["00", "B0", "LL", "q1"], ["0M", "BM", "LS", "q1"], ["BM", "BM", "SR", "q8"]],
        "q8" : [["BB", "BB", "SL", "q10"], ["B0", "B0", "SL", "q9"]],
        "q9" : [["BM", "BM", "SL", "q2"]],
        "q2" : [["BX", "BX", "SL", "q2"], ["BB", "BX", "SR", "q3"]],
        "q3" : [["BX", "BX", "SR", "q3"], ["BM", "BM", "SR", "q4"]],
        "q4" : [["B0", "B0", "RR", "q4"], ["BB", "BB", "LL", "q5"]],
        "q5" : [["B0", "0B", "LL", "q6"]],
        "q6" : [["B0", "0B", "LL", "q6"], ["BM", "BM", "RR", "qs"]]
        }




    while (state != "q10"):
        i = 0
        while (i < len(dict1[state])):
            if(tape1[index1] + tape2[index2] == dict1[state][i][0]):
                tape1[index1] = dict1[state][i][1][0]
                tape2[index2] = dict1[state][i][1][1]
                cek = [tape1[index1], tape2[index2]]
                if(dict1[state][i][2][0] == "R"):
                    index1 += 1
                elif(dict1[state][i][2][0] == "L"):
                    index1 -= 1
                if(dict1[state][i][2][1] == "R"):
                    index2 += 1
                elif(dict1[state][i][2][1] == "L"):
                    index2 -= 1
                state = dict1[state][i][3]
                print(tape1[index1-10:index1 + 10])
                print(tape2[index2-10:index2 + 10]) 
                print("state : " + state)
                if state == "q10":
                    print("Diterima, hitung jumlah X")
                break  
            i += 1
            if i >= len(dict1[state]):
                sys.exit("Tolak")