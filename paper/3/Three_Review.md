## Paper review -Two
####i. [Reverse Engineering Finite State Machines from Rich Internet Applications - Domenico Amalfitano°, Anna Rita Fasolino*, Porfirio Tramontana* - 2008 15th Working Conference on Reverse Engineering ] (http://ieeexplore.ieee.org.prox.lib.ncsu.edu/stamp/stamp.jsp?tp=&arnumber=4656395) 

***Number of Citations :*** 52

####ii. Keywords

**ii1. Finite State Machines** : It is a model of mathematical computation, operates by abstraction to solve problems. A FSM has finite number of states, and it can be in only one of the defined states at a point of time.A Finite State Machine is defined by the lists of its states and the triggering condition for transition between the states. Simple examples include traffic lights system, which changes stated based on the number of vehicles, sequential logic circuits, lock and key, etc. An FSM is limited on memory and tasks, and hence, has lesser computational power due to limited states.

**ii2. Abstraction** : Abstraction is the way to handle complexity(***of computation here***). It works by assigning the user, a level of complexity, hiding complex systems under the hood. For instance, the programmer would'nt be interested in the underneath binary operation which takes place while he/she tries to manipulate numbers in a program. These details are hidden from the user, by simply leaving with the features the user can work with.

**ii3. Rich Internet Application(RIA)** : The RIA's are more dynamic and are more interactive in nature compared to traditional web application. This is enabled by Ajax, a technique the browser to interact with the server without refreshing the page, thereby providing smoother and a dynamic interface to the end-user. An RIA can be considered a single-page model, where changes can be made to page components without needing to refresh it.

**ii4. Document Object Model(DOM) Interface** : DOM is a platform-based and language-neutral programming interface which presents the logical structure of the documents to be accessed and manipulated by the programs and scripts. This way, the content,structure and style of the Documents(***HTML and XML pages***) can be accessed and updated. The documents can be further processed and can be presented back into the existing page.


####iii. Artifacts

**iii1. Study Instruments** : 

The ***user-tracing*** activity has been employed by the researchers to model the RIA dynamic analysis in a controlled environment. Its main goal is to register the sequence of events, and the trigger that caused the event. These events make up the significant use-cases of the application. It is implemented in two iterative state: Event Waiting and Event Handling Completion waiting stages. When the ***user-tracing starts***, the webpage is rendered and enters the Event Waiting state until any event is triggered. At the trigger, into transition to the second state, a transition tracing activity is carried out storing all the information about the trigger and the transition. After completion of Event Handling state, the time stamps and other https listeners are captured and the process returns to the initial state. The illustration is given below

![screen shot 2015-09-27 at 3 19 42 pm](https://cloud.githubusercontent.com/assets/10588000/10124764/49ac83be-652b-11e5-9a79-1a05f55b14d4.png)

**iii2. Checklists:** : 

The components required to perform the reverse engineering of RIA's include:
- [x] ***Source of the Application:*** For abstracting the Finite State Machine model behavior, the RIA should be an open-source( or the one which enables Document Object Model configuration). One of the RIA, the authors used is: [FilmDB,a medium-sized open-source Rich Internet Application](http://sourceforge.net/projects/ajaxfilmdb/)

- [x] ***Generating and selection of Use-cases:*** Several use-cases of the RIA should be generated so that the tester chooses the specific use-cases, which he/she thinks are the most common ones. For instance, the authors selected the case of the user input into the form to narrow down the genre as one of the use-case.

- [x] ***Using the tool:*** The reverse engineering tool was employed to capture the data on tests, to help create the Finite State Machines of the Application. It generates reports for both the key steps: ***Extraction*** and ***Abstraction***.

- [x] ***Equivalence criteria:***(of nodes and edges) It is used in the clustering part of abstraction to cluster the similar nodes/edges of the Transition Graph. The engineer used both these criteria( c1 & c2) to decide which nodes are associated with meaningful states, and which ones have to be split to further logical states. These criteria influence the effectiveness of the technique and should be used accurately.

**iii3. Related Work** :
- [Testing Web applications by modeling with FSMsAnneliese A. Andrews, Jeff Offutt, Roger T. Alexander](http://search.proquest.com.prox.lib.ncsu.edu/docview/198091986?pq-origsite=summon): A technique to build the hierarchies of Finite State Machines in Web applications, that model its sub-systems. The refinement of use-cases through the sub-systems help form complete executable use-cases. The limitation of this technique being, it cannot be used to the Rich Internet Applications.
- [Reverse Engineering State Machines by Interactive Grammar Inference- Walkinshaw, N. ; Regent Court, Sheffield ; Bogdanov, K. ; Holcombe, M. ; Salahuddin, S.](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=4400167&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D4400167) explores the concept of interactive grammar inference technique to explore the state machine underneath. This was proposed for the software applications, however, with no reference to the complex RIA's.

**iii4. Patterns:** In the case study presented, the equivalence criteria (c1 & c2) for the clustering algorithm is worth taking a look. Using  c1, most nodes of the transition graph are associated with single state, and some nodes could not be associated with any states. However, c2 showed a lot of promise, and revealed that most of the nodes could be associated with the meaningful states.


####iv. Scope for Improvement

**ii1. Scalability** : As the businesses move from traditional Web to the Rich Internet Applications, the testing techniques should be able to handle the scale. The proposed technique addresses the adequacy of the approach but not the scalability. There should be more pointers on how to implement this technique quickly. In the context of FilmDB's testing, left alone the time taken for the tool to run, the engineer spent an hour each on the Concept Assignment task from the two clustering equivalence criteria. In a way, the sufficiency of data to the tester to formulate the hypothesis is justified by elaborate reports. But, it would still depend on the skill-level and the decision-making ability of the tester. However, the authors made
a note about addressing this issue by further experimentation, but I think scalability should've been one of the criteria while designing the processes.

**ii2. A metric to evaluate clustering** : The clustering of nodes is the key step in abstraction activity. As observed, there was a difference in output using the two proposed criteria. It would be an helful to have a metric like accuracy or precision after the tester made the grouping after evaluating the criteria.

**ii3. Feasibility of implementation** :  Disclosing details about the conducting the study and resources consumed would have been useful to evaluate the overall feasibility. This information could be used to compare other methods proposed by other researchers. 
