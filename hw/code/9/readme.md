## Comparing  Optimizers: Differential Evolution, Simulated annealing and MaxWalkSat

**By :** Guduguntla Vamshi & Sattwik Pati

####Abstract

This paper presents the results of implementing a standard Genetic Algorithm on multi-objective functions computed over multiple decisions.The algorithm is modeled after biological phenomena of evolution, natural selection and survival of the fittest mechanisms.This paper presents our implementation of algorithm, the methods and machinery used to generate results while testing the its performance.

####i. Introduction

Genetic algorithm generates as population of “candidates”, as an anticipated solution to optimize the objective(s). The candidates are scored initially with “function value” or the fitness(in genetic terms) indicating the closeness to the objective. The algorithm makes use of generating multiple "candidates" and scoring them using the "function value" The initial population is treated as “parents”. The parents are "crossed-over" at random to generate children. At some proportion, and using the "function value" or fitness the children and parents are retained to maintain the population."Mutation" is introduced to the children at random to give a little "fizz" to the children candidates. 

A “generation” of new population is produced by selecting the best parents from current generation and children. "Cross-over" of the more fit individuals makes good use of search space. As candidates of a population evolve over generations, they move towards a optimal solutions. Though, Genetic algorithms do not provide sufficient confidence to the the global optima, but they explore the space and gravitate towards optima quickly.

The rest of the paper is organized as follows - Section ii discusses the algorithm approach. Section iii has the experimental details the parameter choices made. Section iv provides a summary of the results obtained when GA was tested against DTLZ 1, 3, 5, 7. Section v talks about the threats to the validity of our implementation while Section vi is about the Future scope of the implementation. Section vii is references.

We will be testing the performance of our implementation of GA on 20 repeats of DTLZ 1, 3, 5, 7 models.

####ii. Understanding the Algorithm

**ii1. Genetic Algorithm** : 

Pseudo code:

```
1. Initialization of the model to optimize and its parameters
2. Set the number of lives
3. Generate the baseline frontier of "candidates"
4. Crossover step: Select a pair of parents in the frontier at random and cross-over to produce children
5. Selection step: score the children and select them into the new frontier
6. Mutate with some probability (change a small amount of the newly born babies randomly)
7. Penalize the lives if the new frontier is not better than previous, else award lives.
7. go back to 2. repeat until maximum generation is reached or early termination criteria is met.
```

**ii1. Cross-over** : The cross-over step is initially performed among the randomly chosen parents. The single point cross-over enables us to generate two children with a given pair of parents. The illustration is given in the figure below.

![Fig 1:](https://cloud.githubusercontent.com/assets/10588000/11675381/5fb54fe2-9df7-11e5-90a0-86a0f103cd19.png)

**ii2. Selection step** : 

Once the children population is generated, the child candidates are score according to an aggregate function. An aggregated function can be expressed in two ways:
- **Aggregate function**: to check the sum of the function vector returned by the model(DTLZ1,3,5,7 here) when the candidates are passed to the scoring.
- **Domination score**: to calculate the scores of the candidates based on the number of binary domination value. For instance, a candidate which dominates 20 other candidates in the pool has the domination score assigned as  20.

Post calculation of the scores mentioned above, sort the candidates(children here) by the score and perform the selection of those in children pool and the parent pool by giving weights to them.

**ii3. Mutation** : With a random probability, the children are mutated by adding a little "fizz" to it. This could be done by changing the candidate along a dimension, taking the nearest neighbour or to generate a close by candidate.

**ii4. Termination** : 

After 100 generations, the algorithm begins evaluates the frontier to determine the case of ealy termination. 
- Once the GA terminates, in order to evaluate the performance of the algorithm, we compute the hypervolume indicator. The population of the final generation is assumed to be the pareto frontier.Then:
- Compare the candidates in this set with the rest of the population, that belong to previous frontier. If the candidates of the final   frontier dominate the candidates of previous frontier, they are allowed to stay and the there is no penlization of the lives.

####iii. Experimental Design

**iii1. Models used:**

DTLZ: models built specifically to test the optimization algorithms. See DTLZ1,3,5,7. They are  designed in such a way that the number of decisions and objectives can be dynamically configured to generate function value vectors.

**iii2. Apparatus:**

- Genetic Algorithm on 4 different models: DTLZ1,3,5,7
- Number of candidates: 100
- Number of maximum generations: 1000
- Number of decision: 10, 20, 40
- Number of objectives:  2, 4, 6, 8
- Crossover: one point two children
- Mutation probability: 0.05
- Repeat 20 times for each
- Early termination: life = 5, each new generation, if not better, life=life-1; else, award 5 lives
- Terminate when life = 0

**iii3. Choice of parameters:**

- Number of candidates every generation: 100
- % weight to the children in the generation after cross-over(scored,sorted): 80%
- % weight to the parents in the generation after cross-over(randomly chosen): 20%
- Parameter for the a12 comparison:  0.4

**iii4. Choice evualuation metrics: Hypervolume**

Hypervolume measures the volume of the dominated portion of the objective space.The metric to grade the algorithm is hypervolume. For each model, decision and objective combination, the GA is run for 20 times and the Hypervolume for each of these runs is recorded. 

**Output** Mean and Standard deviation for the GA for 20 times simulated over the model,decisions,objective combination


####iv. Summary of Results: 

Evualuation metrics: **Hypervolume**

**DTLZ1**

|Objectives\Decisions|10|20|40|
|:---:|---|---|---|
|2|Mean = 0.995274<br/>SD = 0.000746|Mean = 0.995741<br/>SD = 0.000963|Mean = 0.997400<br/>SD = 0.000815|
|4|Mean = 0.995776<br/>SD = 0.001137|Mean = 0.995550<br/>SD = 0.000773|Mean = 0.997280<br/>SD = 0.000778|
|6|Mean = 0.995050<br/>SD = 7.46e-05|Mean = 0.996299<br/>SD = 0.001378|Mean = 0.997431<br/>SD = 0.000945|
|8|Mean = 0.995254<br/>SD = 0.000502|Mean = 0.995826<br/>SD = 0.001129|Mean = 0.997483<br/>SD = 0.000549|

**DTLZ3**

|Objectives\Decisions|10|20|40|
|:---:|---|---|---|
|2|Mean = 0.995274<br/>SD = 0.000746|Mean = 0.995741<br/>SD = 0.000963|Mean = 0.997400<br/>SD = 0.000815|
|4|Mean = 0.995776<br/>SD = 0.001137|Mean = 0.995550<br/>SD = 0.000773|Mean = 0.997280<br/>SD = 0.000778|
|6|Mean = 0.995050<br/>SD = 7.46e-05|Mean = 0.996299<br/>SD = 0.001378|Mean = 0.997431<br/>SD = 0.000945|
|8|Mean = 0.995254<br/>SD = 0.000502|Mean = 0.995826<br/>SD = 0.001129|Mean = 0.997483<br/>SD = 0.000549|

**DTLZ5**

|Objectives\Decisions|10|20|40|
|:---:|---|---|---|
|2|Mean = 0.995274<br/>SD = 0.000746|Mean = 0.995741<br/>SD = 0.000963|Mean = 0.997400<br/>SD = 0.000815|
|4|Mean = 0.995776<br/>SD = 0.001137|Mean = 0.995550<br/>SD = 0.000773|Mean = 0.997280<br/>SD = 0.000778|
|6|Mean = 0.995050<br/>SD = 7.46e-05|Mean = 0.996299<br/>SD = 0.001378|Mean = 0.997431<br/>SD = 0.000945|
|8|Mean = 0.995254<br/>SD = 0.000502|Mean = 0.995826<br/>SD = 0.001129|Mean = 0.997483<br/>SD = 0.000549|

**DTLZ7**

|Objectives\Decisions|10|20|40|
|:---:|---|---|---|
|2|Mean = 0.995274<br/>SD = 0.000746|Mean = 0.995741<br/>SD = 0.000963|Mean = 0.997400<br/>SD = 0.000815|
|4|Mean = 0.995776<br/>SD = 0.001137|Mean = 0.995550<br/>SD = 0.000773|Mean = 0.997280<br/>SD = 0.000778|
|6|Mean = 0.995050<br/>SD = 7.46e-05|Mean = 0.996299<br/>SD = 0.001378|Mean = 0.997431<br/>SD = 0.000945|
|8|Mean = 0.995254<br/>SD = 0.000502|Mean = 0.995826<br/>SD = 0.001129|Mean = 0.997483<br/>SD = 0.000549|


####v. Threats to validity: 

- **Early termination**: may prevent optimizers to reach a globally optimum solution. However for efficency reasons, early termination may be required.
- **Different Search spaces**: these optimizers should be evaluated in according to the search space each of them has explored.
- **Aggregating Objectives**: By objective function values to a point form and performing operations, we fail to recognize the accuracy on results.



####vi. Reference: 

1. Jelihovschi, E.G., Faria, J.C., & Allaman, I.B.. (2014). ScottKnott: a package for performing the Scott-Knott clustering algorithm in R. TEMA (São Carlos), 15(1), 3-17.

2. [A12 comparison implementation](https://github.com/txt/mase/blob/master/src/doc/sk.py)   

3. Storn, R. (1996). "On the usage of differential evolution for function optimization". Biennial Conference of the North American Fuzzy Information Processing Society (NAFIPS). pp. 519-523.
