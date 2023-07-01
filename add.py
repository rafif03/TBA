# add.py

def add():
    masuk1 = input()
    awal = "BBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    akhir = "BBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    masuk1 = awal + masuk1 + akhir
    masuk2 = "B" * len(masuk1)
    masuk3 = masuk2
    index1, index2, index3 = 28, 28, 28
    tape1 = list(masuk1)
    tape2 = list(masuk2)
    tape3 = list(masuk3)
    state = "q0"
    print(tape1[index1-6:index1 + 10])
    print(tape2[index2-6:index2 + 10])
    print(tape3[index3-6:index3 + 10])
    print("state : " + state)
    dict1 = {
        "q0" : [["0BB", "BB0", "RSR", "q0"], ["1BB", "BB1", "RSR", "q0"], ["+BB", "BBB", "RSS", "q1"]],
        "q1" : [["0BB", "B0B", "RRS", "q1"], ["1BB", "B1B", "RRS", "q1"], ["BBB", "BBB", "LLL", "q2"]],
        "q2" : [["B10", "BBB", "SLL", "q2"], ["B01", "BBB", "SLL", "q2"], ["BB0", "0BB", "LSL", "q2"], ["BB1", "1BB", "LSL", "q2"], ["B1B", "1BB", "LLS", "q2"], ["B0B", "0BB", "LLS", "q2"], ["B11", "B11", "SSS", "q3"], ["B00", "B00", "SSS", "q3"]],
        "q3" : [["B11", "1XX", "LSS", "q3"], ["B00", "0YY", "LSS", "q3"], ["BYY", "0BB", "LLL", "q2"], ["BXX", "1BB", "LLL", "q2"]]
        }




    while (1):
        i = 0
        while (i < len(dict1[state])):
            #print(i)
            if(tape1[index1] + tape2[index2] + tape3[index3] == dict1[state][i][0]):
                tape1[index1] = dict1[state][i][1][0]
                tape2[index2] = dict1[state][i][1][1]
                tape3[index3] = dict1[state][i][1][2]
                cek = [tape1[index1], tape2[index2]]
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
                state = dict1[state][i][3]
                print(tape1[index1-6:index1 + 10])
                print(tape2[index2-6:index2 + 10]) 
                print(tape3[index3-6:index3 + 10])
                print("state : " + state)
                break  
            i += 1
            if state == "q2" and i >= len(dict1[state]):
                exit("Diterima, hitung jumlah 0/1 (0 positif, 1 negatif)")
            if i >= len(dict1[state]):
                exit("Tolak")