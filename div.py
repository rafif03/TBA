# div.py

def div():
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
    print(tape1[index1-15:index1 + 10])
    print(tape2[index2-15:index2 + 10])
    print(tape3[index3-15:index3 + 10])
    print("state : " + state)
    dict1 = {
        "q0" : [["0BB", "00B", "RRS", "q0"], ["1BB", "11B", "RRS", "q0"], ["/BB", "/BB", "RSS", "q1"]],
        "q1" : [["0BB", "0BB", "SLS", "q2"], ["1BB", "1BB", "SLS", "q2"], ["BBB", "BBB", "SSS", "q6"]],
        "q2" : [["00B", "00B", "RLS", "q2"], ["11B", "11B", "RLS", "q2"], ["01B", "01B", "RLS", "q2"], ["10B", "10B", "RLS", "q2"], ["B0B", "B0B", "LSS", "q3"], ["B1B", "B1B", "LSS", "q3"], ["BBB", "BBB", "LRS", "q6"], ["0BB", "0BB", "SSS", "q6"], ["1BB", "1BB", "SSS", "q6"]],
        "q3" : [["00B", "000", "SSR", "q4"], ["11B", "110", "SSR", "q4"], ["01B", "011", "SSR", "q4"], ["10B", "101", "SSR", "q4"]],
        "q4" : [["00B", "00B", "LLS", "q4"], ["11B", "11B", "LLS", "q4"], ["01B", "01B", "LLS", "q4"], ["10B", "10B", "LLS", "q4"], ["X1B", "X1B", "RSS", "q5"], ["XBB", "XBB", "RRS", "q5"], ["X0B", "X0B", "RSS", "q5"], ["BBB", "BBB", "LRS", "q6"], ["0BB", "0BB", "SSS", "q6"], ["1BB", "1BB", "SSS", "q6"]],
        "q5" : [["00B", "000", "SSR", "q2"], ["11B", "110", "SSR", "q2"], ["01B", "011", "SSR", "q2"], ["10B", "101", "SSR", "q2"]],
        "q6" : [["00B", "000", "SSS", "q6"], ["11B", "110", "SSS", "q6"], ["01B", "011", "SSS", "q6"], ["10B", "101", "SSS", "q6"]]
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
                print(tape1[index1-15:index1 + 10])
                print(tape2[index2-15:index2 + 10]) 
                print(tape3[index3-15:index3 + 10])
                print("state : " + state)         
                break  
            i += 1 
            if state == "q6" and i >= len(dict1[state]):
                exit("Diterima, hitung jumlah 0/1 (0 positif, 1 negatif) di tape 3")
            if i >= len(dict1[state]):
                exit("Tolak")