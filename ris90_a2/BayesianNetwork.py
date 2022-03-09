import numpy as np

def get_p_b_cd():
     
    #freq is a dictionary of type {bcd:freq}, where bcd is a code for elements b,c,d and of type string
    #bcd takes different values depending on 
    freq={}
    # you need to implement this method.
    #This will create matrix of 3X3X2
    p_b_cd = np.zeros((3,3,2),dtype = np.float)
    with open(data_add,"r") as file:
        doc = file.readlines()
        for i in range(1, len(doc)):
            data = doc[i].split("\t")
            temp = data[2]+data[3]+data[4]
            if temp not in freq.keys():
                freq[temp]=1
            else:
                freq[temp] += 1    
    
    #To Populate Matrix
    for c in range(3):
        for d in range(2):
            count_cd = 0
            for b in range(3):
                bcd = str(b+1)+str(c+1)+str(d+1)
                if bcd in freq.keys():
                    #Calculate Frequency of (b,c,d)
                    count_bcd = freq.get(bcd)
                    p_b_cd[b,c,d]=count_bcd
                    #Summation Frequency of (c,d) over b
                    count_cd =  count_bcd + count_cd
                else: p_b_cd[b,c,d]=0
            #Initially we have just assigned the frequency of (b,c,d), now we'll assign the probability to it
            if (count_cd != 0):
                for b in range(3):
                    p_b_cd[b,c,d] = p_b_cd[b,c,d]/count_cd
    return (p_b_cd)

def get_p_a_be():

    #freq is a dictionary of type {abe:freq}, where abe is a code for elements b,c,d and of type string
    freq={}
    # you need to implement this method.
    #This will create matrix of 2X3X2
    p_a_be = np.zeros((2,3,2),dtype = np.float)
    with open(data_add,"r") as file:
        doc = file.readlines()
        for i in range(1, len(doc)):
            data = doc[i].split("\t")
            e_val = data[5].strip()
            temp = data[1]+data[2]+e_val
            if temp not in freq.keys():
                freq[temp]=1
            else:
                freq[temp] += 1    
    #To Populate Matrix
    for b in range(3):
        for e in range(2):
            count_be = 0
            for a in range(2):
                abe = str(a+1)+str(b+1)+str(e+1)
                if abe in freq.keys():
                    #Calculate Frequency of (a,b,e)
                    count_abe = freq.get(abe)
                    p_a_be[a,b,e]=count_abe
                    #Summation Frequency of (b,e) over a
                    count_be =  count_abe + count_be
                else: p_a_be[a,b,e]=0
            #Initially we have just assigned the frequency of (a,b,e), now we'll assign the probability to it
            if (count_be != 0):
                for a in range(2):
                    p_a_be[a,b,e] = p_a_be[a,b,e]/count_be
    return (p_a_be)


# following lines are main function:
data_add = "data//assign2_BNdata.txt"

# probability distribution of b.
p_b_cd=get_p_b_cd()
with open("data/Output_BN.txt","w+") as file:
    for c in range(3):
        for d in range(2):
            for b in range(3):
                print("P(b=" + str(b+1) + "|c=" + str(c+1) + ",d=" + str(d+1) + ")=" + str(p_b_cd[b][c][d]))
                file.writelines("P(b=" + str(b+1) + "|c=" + str(c+1) + ",d=" + str(d+1) + ")=" + str(p_b_cd[b][c][d]) + "\n")

# probability distribution of a.
p_a_be=get_p_a_be()
with open("data/Output_BN.txt","a+") as file:
    for b in range(3):
        for e in range(2):
            for a in range(2):
                print("P(a=" + str(a+1) + "|b=" + str(b+1) + ",e=" + str(e+1) + ")=" + str(p_a_be[a][b][e]))
                file.writelines("P(a=" + str(a+1) + "|b=" + str(b+1) + ",e=" + str(e+1) + ")=" + str(p_a_be[a][b][e]) + "\n")
