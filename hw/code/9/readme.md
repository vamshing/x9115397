## Comparing  Optimizers: Differential Evolution, Simulated annealing and MaxWalkSat

**By :** Guduguntla Vamshi & Sattwik Pati

####Abstract

This paper presents the results of implementing a standard Genetic Algorithm on multi-objective functions computed over multiple decisions.The algorithm is modeled after biological phenomena of evolution, natural selection and survival of the fittest mechanisms.This paper presents our implementation of algorithm, the methods and machinery used to generate results while testing the its performance.

####i. Introduction

Genetic algorithm generates as population of “candidates”, as an anticipated solution to optimize the objective(s). The candidates are scored initially with “function value” or the fitness(in genetic terms) indicating the closeness to the objective. The algorithm makes use of generating multiple "candidates" and scoring them using the "function value" The initial population is treated as “parents”. The parents are "crossed-over" at random to generate children. At some proportion, and using the "function value" or fitness the children and parents are retained to maintain the population."Mutation" is introduced to the children at random to give a little "fizz" to the children candidates. 

A “generation” of new population is produced by selecting the best parents from current generation and children. "Cross-over" of the more fit individuals makes good use of search space. As candidates of a population evolve over generations, they move towards a optimal solutions. Though, Genetic algorithms do not provide sufficient confidence to the the global optima, but they explore the space and gravitate towards optima quickly.

The rest of the paper is organized as follows - Section ii discusses the algorithm approach. Section iii has the comparison operators listed, section iv is about experimental details the parameter choices made. Section v provides a summary of the results obtained when GA was tested against DTLZ 1, 3, 5, 7. Section vi talks about the threats to the validity of our implementation while Section viii is about the Future scope of the implementation. Section viii is references.

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

DTLZ: models built specifically to test the optimization algorithms. See DTLZ1,3,5,7. They are  designed in such a way that the number of decisions and objectives can be dynamically configured to generate function value vectors.

**iv2. Apparatus:**

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

**iv3. Choice of parameters:**

- Number of candidates every generation: 100
- % weight to the children in the generation after cross-over(scored,sorted): 80%
- % weight to the parents in the generation after cross-over(randomly chosen): 20%
- Parameter for the a12 comparison:  0.4

**iv4. Choice evualuation metrics: Hypervolume**

Hypervolume measures the volume of the dominated portion of the objective space.The metric to grade the algorithm is hypervolume. For each model, decision and objective combination, the GA is run for 20 times and the Hypervolume for each of these runs is recorded. 

**Output** Mean and Standard deviation for the GA for 20 times simulated over the model,decisions,objective combination


####v. Summary of Results: 

Evualuation metrics: **Hypervolume**

**DTLZ1**

|Objectives\Decisions|10|20|40|
|:---:|---|---|---|
|2|Mean = 0.9919<br/>SD = 0.0140815482103|Mean = 0.98365<br/>SD = 0.0250285337165|Mean = 0.9793<br/>SD = 0.0258864829593|
|4|Mean = 0.9881<br/>SD = 0.0198844160085|Mean = 0.9792<br/>SD = 0.0267069279401|Mean = 0.9713<br/>SD = 0.0275755326331|
|6|Mean = 0.99675<br/>SD = 0.00436892435274|Mean = 0.9824<br/>SD = 0.0205095099893|Mean = 0.9757<br/>SD = 0.0198924608835|
|8|Mean = 0.9966<br/>SD = 0.00483114893167|Mean = 0.9879<br/>SD = 0.0176773866847|Mean = 0.9615<br/>SD = 0.0353305816539|

**DTLZ3**

|Objectives\Decisions|10|20|40|
|:---:|---|---|---|
|2|Mean = 0.3387<br/>SD = 0.302344191279|Mean = 0.22655<br/>SD = 0.250911234304|Mean = 0.43455<br/>SD = 0.30678387751|
|4|Mean = 0.90795<br/>SD = 0.11492017882|Mean = 0.90045<br/>SD = 0.129176420062|Mean = 0.8639<br/>SD = 0.0820157911624|
|6|Mean = 0.92695<br/>SD = 0.109076796341|Mean = 0.95525<br/>SD = 0.0452104799798|Mean = 0.9307<br/>SD = 0.0858819538669|
|8|Mean = 0.9838<br/>SD = 0.0361643470838|Mean = 0.9427<br/>SD = 0.0661529288845|Mean = 0.9736<br/>SD = 0.023253816891|

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

Interpreting the results:

- Hypervolume is good enough on DTLZ1,3, but sparser on DTLZ5,7.
- Hypervolume on DTLZ3 increases as number of objectives & decisions increase.
- performance (measured by hypervolumn) decreases as number of objectives increase.

####vi. Threats to validity: 

- **Early termination**: may prevent optimizers to reach a globally optimum solution. However for efficency reasons, early termination may be required.
- **Different Search spaces**: these optimizers should be evaluated in according to the search space each of them has explored.
- **Early convergence* on some models was noticed. This could be controlled by both  mutation probability and the proportion of child -parent selection mix.In our algorithm, the mutation rate is a constant throughout the run.
- **Aggregating Objectives**: By objective function values to a point form and performing operations, we fail to recognize the accuracy on results. I have used the aggregation over the domination score for faster computation of the solutions space. However, this can be viewed as a threat as functions cannot always be aggregated. Domination score is preferred for accurate results.
-  **Slow convergence** leads to more computing power demand. Hence, some of the hacky ways like **Aggregating Objectives** was used to work around this problem. 

####vii. Scope of future work:

**Tuning the parameters **: There are number of parameters which can be tuned to stop early and slow convergence/termination. We have noticed that the hypervolume for early terminations are quite low. Tuning some the magic parameters ensured that the termination is delayed, hence more exploration of the search space. Few of them are mutation probability, number of candidates, a12 test criteria, proportion of parent-child selection.

**Boolean domination **: Boolean domination has its own drawbacks and hence the idea of continuous domination as a part of the select procedure could be explored.

**Aggregation of function vector **: Improve the aggregation method of function vector by trying out different strategies such as weighted-sum approach and target vector optimization methods[2]

- **Different Search spaces**: 
- **Early convergence* 
- **Aggregating Objectives**: 
-  **Slow convergence** 


####viii. Reference: 

1. [A12 comparison implementation](https://github.com/txt/mase/blob/master/src/doc/sk.py)   

2. Zitzler, Eckart, and Lothar Thiele. "Multiobjective evolutionary algorithms: a comparative case study and the strength Pareto approach." evolutionary computation, IEEE transactions on 3.4 (1999): 257-271.
