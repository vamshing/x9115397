
## Hyper-parameter Optimization of Genetic algorithm

**By :** Guduguntla Vamshi & Sattwik Pati

####Abstract

This paper presents the results of implementing a standard Genetic Algorithm by tuning the parameters using the Differential Evolution algorithm. This is done on multi-objective functions computed over multiple decisions. This paper presents our implementation of algorithm, the methods and machinery used to generate results while testing the its performance.

####i. Introduction

Genetic algorithm generates as population of “candidates”, as an anticipated solution to optimize the objective(s). The candidates are scored initially with “function value” or the fitness(in genetic terms) indicating the closeness to the objective. The algorithm makes use of generating multiple "candidates" and scoring them using the "function value" The initial population is treated as “parents”. The parents are "crossed-over" at random to generate children. At some proportion, and using the "function value" or fitness the children and parents are retained to maintain the population."Mutation" is introduced to the children at random to give a little "fizz" to the children candidates. 

A “generation” of new population is produced by selecting the best parents from current generation and children. "Cross-over" of the more fit individuals makes good use of search space. As candidates of a population evolve over generations, they move towards a optimal solutions. Though, Genetic algorithms do not provide sufficient confidence to the the global optima, but they explore the space and gravitate towards optima quickly.

The rest of the paper is organized as follows - Section ii discusses the algorithm approach. Section iii has the comparison operators listed, section iv is about experimental details the parameter choices made. Section v provides a summary of the results obtained when GA was tested against DTLZ 5. Section vi talks about the threats to the validity of our implementation while Section viii is about the Future scope of the implementation. Section viii is references.

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

**ii2. Differential Evolution** : Differential Evolution emulates genetic algorithms,which like all of them does not guarantee an optimal solution always. 

- It solves tries by iteratively trying to improve the candidate solution with respect to function value of the solution. 
- In every iteration, the candidates are created from crossing over the candidates created from the previous generation. 
- Replacement is done, if the new child  is has lower energy/close to objective than the previous one. The process continues until a threshold is reached.

DE has the advantaghe of giving good solutions quickly compared to other algorithms.

We followed the following Pseudo Code in our implementation:

At each step of the iteration from the frontier we

1. pick 3 candidate solutions at random-X,Y,Z

2. At a given *crossover factor* we will generate a new candidate solutions by the below formulation
    New = X+cf*(Y-Z)

3. If the new solution proves to be better than the current candidate solution, we replace the latter in the frontier.

**ii3. Cross-over** : The cross-over step is initially performed among the randomly chosen parents. The single point cross-over enables us to generate two children with a given pair of parents. 

**ii4. Selection step** : 

Once the children population is generated, the child candidates are score according to an aggregate function. An aggregated function can be expressed in two ways:
- **Aggregate function**: to check the sum of the function vector returned by the model(DTLZ1,3,5,7 here) when the candidates are passed to the scoring.

Post calculation of the scores mentioned above, sort the candidates(children here) by the score and perform the selection of those in children pool and the parent pool by giving weights to them.

**ii5. Mutation** : With a random probability, the children are mutated by adding a little "fizz" to it. This could be done by changing the candidate along a dimension, taking the nearest neighbour or to generate a close by candidate.

**ii6. Termination** : 

After 100 generations, the algorithm begins evaluates the frontier to determine the case of ealy termination. Compare the candidates in this set with the rest of the population, that belong to previous frontier. If the candidates of the final   frontier dominate the candidates of previous frontier, they are allowed to stay and the there is no penlization of the lives.

####iii. Comparison operators:

**iii1. Binary Domination:** Solution x is better than Solution y or Solution x dominates y is  when all the objectives of x is not worth than those of y and at least one of the objective of x is better than that of y. In such a case, we say x binary-dominates y. Binary domination is performed between candidates. The implementation is give below:

```
x objective vector,y objective vector 
        for number of objectives :
            if each of x objective vector > each of y objective vector:
                return x donot dominate y 
        return x dominates y

*comment: Minimizing the function, so the lower energy, the better
```

**iii2. a12 test:**

For deciding early termination; i.e. if sets of candiadtes found in frontier+1 is no better that frontier.Here, we do some approximate comparisons between eras.

Krall's Bstop method:

```
For each objective do
  If any "improvement", give yourself five more lives
    Sort the values for that objective in era and era+1
      Run the fast a12 test to check for true difference ( param : .4)
  If no improvement on anything,
  Lives - 1
```

####iv. Experimental Design

**iv1. Models used:**

- DTLZ5 with 2 objections and 10 decisions

**iv2. Apparatus:**

- Genetic Algorithm on DTLZ5 with 2 objections and 10 decisions
- Number of maximum generations: 100
- Number of decision: 10
- Number of objectives:  2
- Crossover: one point two children
- Repeat 20 times for each
- Early termination: life = 5, each new generation, if not better, life=life-1; else, award 5 lives
- Terminate when life = 0
- 
**iv3. Choice of tuning parameters:**

- Number of candidates every generation: a 
- % weight to the children in the generation after cross-over: b
- % weight to the parents in the generation after cross-over: 1-b
- Probability of mutation: c

**iv4. Choice evualuation metrics: Hypervolume**

Hypervolume measures the volume of the dominated portion of the objective space.The metric to grade the algorithm is hypervolume. For each model, decision and objective combination, the GA is run for 20 times and the Hypervolume for each of these runs is recorded. 

**Output** Mean and Standard deviation for the GA for 5 times simulated over the model,decisions,objective combination


####v. Summary of Results: 

Evualuation metrics: **Hypervolume**

**DTLZ5**

|Objectives\Decisions|10|20|40|
|:---:|---|---|---|
|2|Mean = 0.995274<br/>SD = 0.000746|Mean = 0.995741<br/>SD = 0.000963|Mean = 0.997400<br/>SD = 0.000815|
|4|Mean = 0.995776<br/>SD = 0.001137|Mean = 0.995550<br/>SD = 0.000773|Mean = 0.997280<br/>SD = 0.000778|
|6|Mean = 0.995050<br/>SD = 7.46e-05|Mean = 0.996299<br/>SD = 0.001378|Mean = 0.997431<br/>SD = 0.000945|
|8|Mean = 0.995254<br/>SD = 0.000502|Mean = 0.995826<br/>SD = 0.001129|Mean = 0.997483<br/>SD = 0.000549|


Interpreting the results:


####vi. Threats to validity: 

- **Early termination**: may prevent optimizers to reach a globally optimum solution. However for efficency reasons, early termination may be required.
- **Different Search spaces**: these optimizers should be evaluated in according to the search space each of them has explored.
- **Early convergence** on some models was noticed. This could be controlled by both  mutation probability and the proportion of child -parent selection mix.In our algorithm, the mutation rate is a constant throughout the run.
- **Aggregating Objectives**: By objective function values to a point form and performing operations, we fail to recognize the accuracy on results. I have used the aggregation over the domination score for faster computation of the solutions space. However, this can be viewed as a threat as functions cannot always be aggregated. Domination score is preferred for accurate results.
-  **Slow convergence** leads to more computing power demand. Hence, some of the ways like Aggregating Objectives was used to work around this problem. 

####vii. Scope of future work:

**Boolean domination**: Boolean domination has its own drawbacks and hence the idea of continuous domination as a part of the select procedure could be explored.

**Aggregation of function vector**: Improve the aggregation method of function vector by trying out different strategies such as weighted-sum approach and target vector optimization methods[2]


####viii. Reference: 

1. [A12 comparison implementation](https://github.com/txt/mase/blob/master/src/doc/sk.py)   

2. Zitzler, Eckart, and Lothar Thiele. "Multiobjective evolutionary algorithms: a comparative case study and the strength Pareto approach." evolutionary computation, IEEE transactions on 3.4 (1999): 257-271.
