from Filtering import *

def prediction(evidence_data_add, prior, start_day, end_day):
    # you need to implement this method.

    x_prob_rain = []
    # x_prob_sunny[i] = 1 - x_prob_rain[i]
    
    #calling fiter function to retrieve first 100 observations
    x_prob_rain=filtering(evidence_data_add, prior, 100)
    
    #for 101 observation onwards, since we do not have evidence we'll use only transition model
    x = x_prob_rain[99]
    for i in range(start_day, end_day+1):
        #Since we are predicting probability of rain today based on the probability of rain yesterday
        #hence <0.7,0.3>*x + <0.3,0.7>*(1-x), where x is yesterday's prediction of rain
        #Now we only want prediction of rain so our equation is 0.7x + 0.3*(1-x) i.e. 04x+0.3
        x = 0.4*x + 0.3
        #print(x)
        x_prob_rain.append(x)

    return x_prob_rain




# following lines are main function:
evidence_data_add = "data//assign2_umbrella.txt"
start_day = 101
end_day = 150
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=prediction(evidence_data_add, prior, start_day, end_day)
with open("data//Output_Prediction.txt","w+") as file:
    for i in range(start_day, end_day+1):
        print("Day " + str(i) + ": rain " + str(x_prob_rain[i-1]) + ", sunny " + str(1 - x_prob_rain[i-1]))
        file.writelines("Day " + str(i) + ": rain " + str(x_prob_rain[i-1]) + ", sunny " + str(1 - x_prob_rain[i-1])+"\n")
    # print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))