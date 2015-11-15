## Paper review -Nine
####i. [EvoDroid: Segmented Evolutionary Testing of Android Apps] (http://dl.acm.org/citation.cfm?id=2635896) 

***Year :*** 2014

####ii. Keywords

**ii1. Evolutionary Testing** :  Evolutionary testing is a form of search-based testing, where an individual corresponds to a test case, and a population comprised of many individuals is evolved according to certain heuristics to maximize the code coverage.

**ii2. Program Analysis** :  A technique to model the app behaviour by analyzing the source code of the application.Approaches which uses program analysis obtain a more complete model of the app’s behavior.

**ii3.System Reliability** : In system reliability analysis we are concerned with the construction of a model (life distribution) that represents the times-to-failure of the entire system based on the life distributions of the components, subassemblies and/or assemblies ("black boxes") from which it is composed.

**ii4. Application development framework** :  It allows the programmers to extend the base functionality of the platform using a well-defined API. It also also provides a container to manage the lifecycle of components comprising an app and facilitates the communication among them.

####iii. Artifacts

**iii1. Related Work** :

The authors are inspired from the work done by researches if different areas.Below are the references listed:

- [K. Inkumsah and T. Xie. Improving structural testing of object-oriented programs via integrating evolutionary testing and symbolic execution]: 

   Showed Evolutionary testing to be effective when sequences of method invocation are important for obtaining high code coverage. The work is limited to unit level. However, when applied at the system level, it cannot effectively promote the genetic makeup of good individuals in the search.

- [L. Ciortea, C. Zamfir, S. Bucur, V. Chipounov, and
G. Candea. Cloud9: A software testing service]: 

  EXSYST approach uses evolutionary algorithm in conjunction with GUI crawling techniques. This represents test suites as individuals and tests as genes.It generates tests that correspond to random walks on the GUI model.However, using EXSYST, the overall coverage is no better than the initial population.
  
  Two other references, which the authors related the work to evolutionary algorithms in conjunction with GUI crawling techniques are:

- [F. Gross, G. Fraser, and A. Zeller. Search-based system testing: High coverage, no false alarms. In Proceedings of the 2012 International Symposium on Software Testing and Analysis, ISSTA 2012, pages 67–77, 2012.]: 

- [ I. Alsmadi, F. Alkhateeb, E. Maghayreh, S. Samarah, and I. A. Doush. Effective generation of test cases using genetic algorithms and optimization theory.]: 

**iii2. Checklists:** : 

The authors presented the Evodriod tool by describing in the form of an Evolutionary aproach.The goal of EvoDroid is to find a set of test cases that maximize code coverage which summarized as : Representation,Crossover,Mutation and Fitness

- [x] ***Representation:***  An individual is represented as a vector.Each index in the vector contains a gene.The number of input genes is fixed, as the input values are changed, i.e., by mutating the existing input genes. The number of event genes is variable to handle the situations in the app.

- [x] ***Crossover:*** This process selects two individuals from the current population and creates a new individual by mixing their genetic makeup.EvoDroid uses a multi-point probabilistic crossover strategy. There is at least one, and potentially multiple, crossover points between the two selected individuals.The segment crossover probability is calculated as follows:

![screen shot 2015-11-14 at 7 09 38 pm](https://cloud.githubusercontent.com/assets/10588000/11166500/4488b602-8b03-11e5-8f56-85db93f27030.png)

 e - constant to achieve a decay factor, s - index of the current segment being searched, and c - index of a prior segment between 1 and s. 

- [x] ***Mutation:*** Mutation changes parts of the genetic makeup of the newly created individual. Only the current segment genes are mutated with a probability threshold that is configurable.The authors mutated in two passes, where the length of the overall individual can change as a result.

- [x] ***Fitness:*** In each generation, individuals are assessed for their fitness with respect to the search objective to be selected to pass on their genes. The fitness value ranges from 0 to 1.The fitness of an individual i is determined as follows:

![screen shot 2015-11-14 at 7 11 42 pm](https://cloud.githubusercontent.com/assets/10588000/11166510/90362562-8b03-11e5-8f95-69e6583ea972.png)

x - the number of covered nodes in the path to the destination segment, n - the total number of nodes in the path to the destination segment, and u(i) - the uniqueness function of the individual 


**iii3. Baseline Results** :

**Comments:** The authors made a baseline study of the proposed Evodriod approach. Evodriod is compared with Monkey, and Dynodriod along the lines of Complexity, Contraint satisfaction and ordered sequence length. The results are as follows:

This summary below lists the baseline results of all three factors taking the Monkey results as baseline approach.

![screen shot 2015-11-14 at 7 18 06 pm](https://cloud.githubusercontent.com/assets/10588000/11166516/75fdf78c-8b04-11e5-8a55-3a355979d80b.png)

**iii4. New Results :** : 

For the purpose of analysis of the best practices to handle new results, the following points are suggested are the best ways to address. They are proposed as:

1. An Automated technique to generate abstract models of the app’s behavior to support automated testing

2. A segmented evolutionary testing technique that preserves and promotes the genetic makeup of individuals in the search process

3. A scalable system-wide testing framework that can be executed in parallel on the cloud.

####iv. Scope for Improvement

**ii1. Input conditions** :  Reasoning about the inputs is something the authors could better deal with.This is a known limitation of search based algorithms in general practice, such as evolutionary testing.

**ii2. Scaling to apps with native code** :  The algorithm proposed does poorly on the codes written using thrid party libraries. This could be one the area where authors could improve.

