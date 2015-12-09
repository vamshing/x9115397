![screen shot 2015-12-07 at 10 32 07 pm](https://cloud.githubusercontent.com/assets/8950958/11670361/694d2624-9dcf-11e5-800b-82123ebe4f2a.png)


## Comparing  Optimizers: Differential Evolution, Simulated annealing and MaxWalkSat

####i. Abstract

The purpose of the paper is to rank the performance of each of three algorithms: Differential Evolution, Simulated annealing and MaxWalkSat.The optimizers yield a pool of possible candidate solution. Comparing all the possible solution candidates with other in   limited space & time will become expensive.These algorithm provide us a good way to find the best solution by making use of the iterations.Using these algorithms, we have picked DTL27 model to see how these perform using simple statistical tests. The statistical methods are t-knott, a12 and bootstrap are used to compare the candidate solutions. These results are compared based on the type comparators to provide a ranked output of the optimizers for this model.


**By :** Guduguntla Vamshi & Sattwik Pati

####ii. Understanding the Optimizers

**ii1. Simulated Annealing** : Simulated annealing mimicks the annealing of metals process which draws its nature from slow-cooling of metal molecules. This optimizer escapes local minima by jumping to random points initially. The temperature is minimal and increased as the process advances. 

- Started with initial best. Later, the objectives of the generated candidate is compared with the best, and if proven better, updates the best to hold the values of itself. With some random probability, the candidate jump is decided. 
- There are chances that it can jump to the less optimal solutions which will help us to avoid the local optima. The probability of jumping to the lower solution decreases with the time as the random jumping reduces over the time and we will converge on the global optima by skipping the local optima.

Simulated annealing, thus exploits  the nexus between thermo- dynamic behavior and the search for global minima for a discrete optimization problem. 

**ii2. Max Walk Sat** : Max Walk Sat works by  analyzing the landscape of the data. It inherits from Simulated Annealing by to avoid local minima by making jumps to random points. 

- Define maximum number of tries and changes, and the number of iterations for which the runs without early termination are met. Creating instances and shuffling it with the best instance to finally store the best energy seen so far is the next step.
- With a set probability checks are preformed to see if the generated random value is lesser. Then, decision is picked at random and changed which would remain unchanged or else.

MWS argues about the shape of the search space importance.

**ii3. Differential Evolution** : Differential Evolution emulates genetic algorithms,which like all of them does not guarantee an optimal solution always. 

- It solves tries by iteratively trying to improve the candidate solution with respect to function value of the solution. 
- In every iteration, the candidates are created from crossing over the candidates created from the previous generation. 
- Replacement is done, if the new child  is has lower energy/close to objective than the previous one. The process continues until a threshold is reached.

DE has the advantaghe of giving good solutions quickly compared to other algorithms.

####iii. Statistical Machinary used

**iii1. Scott-knott:**

Scott-Knott uses a cluster analysis, where, starting from the whole group of observed mean effects, it divides, and keeps dividing the subgroups in such a way that the intersection of any of the two formed groups remains empty. Using the partition the sample treatment means in a balanced design to show how a corresponding likelihood ratio test gives a method of judging the significance of the difference among groups obtained.

**iii2. Type 1:**

This comparator is used to compare two candidate solutions. Used when the optimizers are comparing pairs of candidates as each of the optimizers generate solutions.

**iii3. Type 2:**

This comparator is used to compare two candidate solutions. Used when the optimizers are comparing pairs of candidates as each of the optimizers generate solutions.

####iv. Future Work: 

This experimentation has been performed on a single model that is DTLZ7 with 2 objectives and 10 decisions. 
- This evaluation can be expanded to include more models with varying number of objectives,decisions be it continuous or discrete. 
- In the future models will different kinds of requirements can be explored to give a more complete evaluation of the optimizers.
- The population size can be increased to have a larger spread of candidates.

####v. Threats to validity: 

- **Early termination**: may prevent optimizers to reach a globally optimum solution. However for efficency reasons, early termination may be required.
- **Different Search spaces**: these optimizers should be evaluated in according to the search space each of them has explored.
- **Aggregating Objectives**: By objective function values to a point form and performing operations, we fail to recognize the accuracy on results.



####vi. Reference: 

1. Jelihovschi, E.G., Faria, J.C., & Allaman, I.B.. (2014). ScottKnott: a package for performing the Scott-Knott clustering algorithm in R. TEMA (São Carlos), 15(1), 3-17.

2. [A12 comparison implementation](https://github.com/txt/mase/blob/master/src/doc/sk.py)   

3. Storn, R. (1996). "On the usage of differential evolution for function optimization". Biennial Conference of the North American Fuzzy Information Processing Society (NAFIPS). pp. 519-523.
