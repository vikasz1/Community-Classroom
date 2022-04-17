K = {}
K[1] = [",","@"]
K[2] = ["A","B","C","a","b","c",2]
K[3] = ["D","E","F","d","e","f",3]
K[4] = ["G","H","I","g","h","i",4]
K[5] = ["J","K","L","j","k","l",5]
K[6] = ["M","N","O","m","n","o",6]
K[7] = ["P","Q","R","S","p","q","r","s",7]
K[8] = ["T","U","V","t","u","v",8]
K[9] = ["W","X","Y","Z","w","x","y","z",9]
buffer = ""
big = []
for _ in range(1):
    # patt = input()
    patt = "22255599"
    digi = patt[0]
    start = 0
    end = 0
    i = 0
    while i<len(patt):
        if patt[i]!=digi:
            # print("hello")
            end = i
            big.append(patt[start:end])
            start = end
            digi = patt[i+1]
        print(digi)
        i+=1
            

        
    print(big)
    