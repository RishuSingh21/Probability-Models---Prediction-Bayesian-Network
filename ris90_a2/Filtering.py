def filtering(evidence_data_add, prior, total_day):
    # you need to implement this method.
    
    #list stores day wise evidence of umbrella
    list=[]
    with open(evidence_data_add,'r') as file:
        doc = file.readlines()
        for i in range(0,len(doc)):
            data=doc[i].split("\t")
            day = (data[0].split(" "))[1]
            evidence = data[1].strip()
            x=(day,evidence)
            list.append(x)
    
    #x_prob_rain stores probability of rain for each day
    x_prob_rain = []
    # x_prob_sunny[i] = 1 - x_prob_rain[i]
    
    #prior probability of rain is 0.5
    #x is the prediction variable
    x = prior[0]
    for i in range(total_day):
        #Since we are predicting probability of rain today based on the probability of rain yesterday
        #hence <0.7,0.3>*x + <0.3,0.7>*(1-x), where x is yesterday's prediction of rain
        #Now we only want prediction of rain so our equation is 0.7x + 0.3*(1-x) i.e. 04x+0.3
        x = 0.4*x + 0.3 
        
        #based on evidence we are calculating probability of rain
        if(list[i][1])== "take umbrella":
            x = x*0.9/((1-x)*0.2 + x*0.9)  
        else:
            x = x*0.1/((1-x)*0.8 + 0.1*x)
        x_prob_rain.append(x)  
    return x_prob_rain


# following lines are main function:
evidence_data_add = "data//assign2_umbrella.txt"

total_day = 100
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=filtering(evidence_data_add, prior, total_day)
with open("data//Output_Filtering.txt","w+") as file:
    for i in range(100):
        print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))
        file.writelines("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]) + "\n")