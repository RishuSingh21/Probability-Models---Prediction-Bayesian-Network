def smoothing(evidence_data_add, prior, total_day):
    # you need to implement this method.
    smoothed_x = []
    for i in range(100):
        smoothed_x.append(0.0)
    return smoothed_x




# following lines are main function:
evidence_data_add = "data//assign2_umbrella.txt"
total_day = 100
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

smoothed_x=smoothing(evidence_data_add, prior, total_day)
for i in range(100):
    print("Day " + str(i+1) + ": rain " + str(smoothed_x[i]) + ", sunny " + str(1 - smoothed_x[i]))