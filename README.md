# Probability-Models---Prediction-Bayesian-Network
Objective: It consists of two tasks: (1) to implement the filtering and prediction algorithm, and (2) to extract  the Bayesian Network probability distribution from data.

Task 1: filtering and prediction inference on Hidden Markov Model (HMM).
The famous umbrella & weather task is considered demonstrate this algorithm.
It says that a secret guard living in the underground installation wants to know whether it’s raining today by observing the director 
coming in the office with or without an umbrella. 
It is a hidden Markov model. Observed evidence variable E represents whether or not the 
director takes an umbrella. Hidden state variable X represents the weather, which can be 
raining or sunny.
Transition model  today rain      today sunny
yesterday rain      0.7               0.3
yesterday sunny     0.3               0.7
Sensor model      take umbrella   no umbrella
rain                0.9               0.1
sunny               0.2               0.8
Weather prior probability is <0.5, 0.5>

Filtering inference on HMM.
Filtering.py is used to implement this task
A forward algorithm is implemented to do filtering inference, i.e., identify the current state 
probability distribution given all evidence to date. 
100 days of the director’s behavior data (with/without an umbrella) is given in assign2_umbrella.txt. Objective is to produce the filtering inference based weather probability distribution from day 1 to day 100. 

Prediction inference on HMM.
Prediction.py is used for this task.
In this task we'll predict probability of rain from 101 day to 150. In filtering task we were using two models Tranform and Sensory model. Since sendory model is dependent on the evidence and here in prediction we do not have evidence we'll predict solely on the basis of transform model.
- Take day 101 for an example, after knowing evidence data from day 1 to day 100, and 
prior probability distribution at day 0, P(X0), your algorithm should give weather 
probability distribution prediction inference of day 101.
- Take day 145 for another example, after knowing evidence data from day 1 to day 100, 
and prior probability distribution at day 0 P(X0), your algorithm should give weather 
probability distribution of day 145.

Task 2: Extract the Bayesian Network probability distribution from data.
BayesianNetwork.py is used for this task implementation
Joint probability: P(a,b,c,d,e)=P(a|b,e)P(b|c,d)P(c)P(d)P(e)
a has 2 values
b has 3 values
c has 3 values
d has 2 values
e has 2 values

