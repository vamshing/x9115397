## Paper review - Four
####i. [An event-flow model of GUI-based applications for testing ] (http://onlinelibrary.wiley.com/doi/10.1002/stvr.364/abstract) 

***Number of Citations :*** 214

####ii. Keywords

**ii1. Event Flow model** : The Event-flow model represents the all possible sequences of events and iteractions that can be executed by on a Graphical User Interface. This is similar to the the data-flow model which represents all the possible definitions and uses of a memory location.

**ii2. Event Flow graph** : It shows all the possible event executions paths with each vertix representing the event and the
edge showing the transition of one event to another.

**ii3. Integration Tree** : A modal dialogue is one when a user at all times during interation with GUI, the interaction of events fall in one modal dialogue. An Integration tree idetifies the realtions between different modal dialogues. It is constructed  once all the modal dialogues were represented as event-flow graphs.

**ii4. Test-Oracles** :  A test oracle is a mechanicsm that determines whether a piece of software executed correctly for a 
test case. In testing, the actual output is compared with a presumably correct expected output. A test oracle may be manual or automated.

**ii5. Model Checking** : A quality assurance activity commonly used to check the correctness of the model. ***Errors*** which
are the correctness problems are discovered during the model checking, help fixing the parameters in the model such as 
operators. In the context, model checking involves whether a model allow certain invalid state to be reached from a known
valid state.

**ii6. Event-Space exploration strategy** : The ESESs use the event-flow model  in a number of ways to develop an end-to-end
GUI testing process. These strategies address more complex problems faced during the model based checking.


####iii. Artifacts

**iii1. Motivation** : The author speaks about three main areas of research which attempted at automating few aspects of GUI Testiing. They are summarized below:
- White et al.[1,2] presentd a different state-machine model for GUI test-case generation that partitions the state space into different machines based on ***user tasks***. The test designer identifies a responsibility, i.e. a user task that can be performed with the GUI. This approach was successful at partitioning the GUI into manageable functional units that can be tested separately.
**Drawback:** Large manual effort is in designing the FSM model for testing, especially when code is not available.
- Another approach is to to mimic novice users’ inputs [3]. This approach relies on an expert to first manually generate a sequence of GUI events for a given user task. A genetic algorithm technique is then used to modify and lengthen the sequence, thereby mimicking a novice user. The underlying assumption is that novice users often take indirect paths through GUIs, whereas expert users take shorter, more direct paths.
**Drawback:**This technique requires a substantial amount of manual effort, and cannot be used to generate other types of test cases.
- Other tools used for GUI testing require programming each GUI test case. These tools include extensions of JUnit such as JFCUnit, Abbot, Pounder, and Jemmy Module. 
**Drawback:** The tester should manually program the event interactions to test, and also specify expected GUI behaviour.
 
**iii2. Checklists:** : 

The components required to obtain the ***Event-flow model*** include:

- [x] ***Construction of the event-flow graphs and integration tree:*** 
     The construction of the event-flow graphs and integration tree is based on the identification of modal dialogues and, the identification of modal and modeless windows and their invokes relationships. A classification of GUI events is used to identify modal and modeless windows. The classification of events is used by an algorithm (given below) to construct event-flow graphs for a GUI. The algorithm computes the set of follows for each event. These sets are then used to create the edges of the event-flow graph.

![Computing follows for a vertex v](https://cloud.githubusercontent.com/assets/10588000/10717904/bdf68e06-7b3b-11e5-906a-09476adcf93f.png)

The set of follows(v) can be determined using the algorithm in Figure above for each vertex v.

- [x] ***Partially create operators from the event-flow graphs:*** 
      The integration tree can be represented as preconditions and effects.This information is retrieved and used to partially create the operators automatically. The test designer ses an iterative process to code the operators. It involves coding a set of operators for a group of related events followed by model checking,. As errors are discovered during model checking, the operators are fixed and rechecked. This happens iteratively

- [x] ***Reverse-Engineering:*** 
      The GUI Ripper[4], a tool to automatically obtain event-flow graphs and the integration tree is used to Reverse Engineer.During ‘GUI Ripping’, the GUI application is executed automatically; the application’s windows are opened in a depth-first manner. The GUI Ripper extracts all of the widgets and their properties from the GUI. During the reverse-engineering process, in addition to widget properties, additional key attributes of each widget are recovered . These attributes are used to construct the event-flow graphs and integration tree.

**iii3. Baseline Results:**

***Mock Experiment***:The usage the event-flow model and tools for experimentation is compared with manual testing. 

***Goal***:The goal of this mock experiment is to determine how the test cases generated compared with those created manually by using capture/replay tools

***Test***: ESES algorithms.

***Control***: The human tester was then given 100 tasks, i.e. activities that they could complete by using the application. They had to devise five different ways to complete each task; the capture tool recorded the user interaction as a test case. The tasks were chosen carefully so that they covered most of the functionality of the applications- 500 test cases were obtained in this way. Then the testers were asked to interact with the software without using tasks, but were asked to cover most of the applications’ windows- 500 additional test cases were generated in this way. In all, 1000 test cases were obtained per application. Each tester took 10–14 days to complete this process.

***The results***:

![Comparison - Number of faults detected](https://cloud.githubusercontent.com/assets/10588000/10717966/94cf2fa4-7b3d-11e5-9aa2-c59449c937fb.png)

**iii4. Scripts:**
All of the tools described in this paper have been packaged into a software called [GUITAR](http://www.cs.umd.edu/~atif/GUITAR-Web/index.html.old). GUITAR has been downloaded more than 10,000 times since it was first made available in 2002.Several practitioners in industry provided continuous feedback that drives bug-fixes and enhancements.

####iv. Scope for Improvement

**ii1. Scalability** : 
The event-flow model is scalable,as discussed, the size of the model grows linearly with the number of events in the GUI. The biggest challenge that this model currently poses is controlling the size of the space of all possible event interactions. If this can be achieved, scalability issue would be largely address. As observed,the number of event sequences that can be executed on the GUI grows exponentially with length.

**ii2. Reduce space via Abstraction** : 
The author has demonstrated some success with reducing the space via abstractions for instance using modal dialogues. Additional abstractions created in such framework will help to further reduce the space. This could potentially save a lot of space.

**ii3. More path traversal** :  
New ESESs could be designed to traverse the event space in more intelligent ways in lesser time and space.


####**References:**

1. [White L, Almezen H. Generating test cases for GUI responsibilities using complete interaction sequences. Proceedings
of the International Symposium on Software Reliability Engineering, 8–11 October 2000. IEEE Computer Society Press:
Piscataway, NJ, 2000; 110–121.](http://barbie.uta.edu/~mehra/23_Generating%20Test%20Cases%20for%20GUI%20Responsibilities%20Using%20Complete%20Interaction.pdf)

2. [White L, Almezen H, Alzeidi N. User-based testing of GUI sequences and their interaction. Proceedings of the
International Symposium on Software Reliability Engineering, 8–11 November 2001. IEEE Computer Society Press:
Piscataway, NJ, 2001; 54–63.](http://ieeexplore.ieee.org/xpl/abstractAuthors.jsp?tp=&arnumber=989458&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D989458)

3. [Kasik DJ, George HG. Toward automatic generation of novice user test scripts. Proceedings of the Conference on Human
Factors in Computing Systems: Common Ground, New York, 13–18 April 1996. ACM Press: New York, 1996; 244–251](http://www.sigchi.org/chi96/proceedings/papers/Kasik/djk_txt.htm)

4. [Memon AM, Banerjee I, Nagarajan A. GUI ripping: Reverse engineering of graphical user interfaces for testing.
Proceedings of the 10th Working Conference on Reverse Engineering, November 2003. IEEE Computer Society Press:
Piscataway, NJ, 2003; 260–269.](http://dl.acm.org/citation.cfm?id=951350)
