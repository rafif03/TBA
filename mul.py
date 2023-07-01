#mul.py

def mul():
    masuk1 = input()
    awal = "B"*100
    akhir = "B"*100
    masuk1 = awal + masuk1 + akhir
    masuk2 = "B" * len(masuk1)
    masuk3 = masuk2
    index1, index2, index3 = 100, 100, 100
    tape1 = list(masuk1)
    tape2 = list(masuk2)
    tape3 = list(masuk3)
    state = "q0"
    print(tape1[index1-30:index1 + 5])
    print(tape2[index2-30:index2 + 5])
    print(tape3[index3-30:index3 + 5])
    print("state : " + state)
    dict1 = {
        "q0" : [["0BB", "00B", "RRS", "q0"], ["1BB", "11B", "RRS", "q0"], ["*BB", "*BB", "RLS", "q1"]],
        "q1" : [["00B", "000", "SLR", "q1"], ["11B", "110", "SLR", "q1"], ["01B", "011", "SLR", "q1"], ["10B", "101", "SLR", "q1"], ["0BB", "0BB", "RRS", "q2"], ["1BB", "1BB", "RRS", "q2"], ["B0B", "BOB", "SSS", "q4"], ["B1B", "B1B", "SSS", "q4"], ["BBB", "BBB", "SSS", "q4"]],
        "q2" : [["00B", "000", "SRR", "q2"], ["11B", "110", "SRR", "q2"], ["01B", "011", "SRR", "q2"], ["10B", "101", "SRR", "q2"], ["0BB", "0BB", "RSS", "q3"], ["1BB", "1BB", "RSS", "q3"], ["B0B", "BOB", "SSS", "q4"], ["B1B", "B1B", "SSS", "q4"], ["BBB", "BBB", "SSS", "q4"]],
        "q3" : [["0BB", "0BB", "SLS", "q1"], ["1BB", "1BB", "SLS", "q1"], ["BBB", "BBB", "SSS", "q4"]],
        "q4" : [[]]
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
                print(tape1[index1-30:index1 + 5])
                print(tape2[index2-30:index2 + 5]) 
                print(tape3[index3-30:index3 + 5])
                print("state : " + state)
                if state == "q4" and i >= len(dict1[state]):
                    exit("Diterima, hitung jumlah 0/1 (0 positif, 1 negatif) di tape 3")
                break  
            i += 1 
            if i >= len(dict1[state]):
                exit("Tolak")