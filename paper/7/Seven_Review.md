## Paper review - Seven
####i. [Automated testing with targeted event sequence generation Casper S. Jensen, Mukul R. Prasad, Anders Møller](http://dl.acm.org.prox.lib.ncsu.edu/citation.cfm?id=248377)

***Year :*** 2013

***Citations :*** 16

####ii. Keywords

**ii1. Symbolic execution** : Symbolic analysis is applied to each event handler to produce an event handler summary characterizing its behavior. This summary  includes necessary data and control flow information about every execution path in the event handler code.

**ii2. Concolic execution** : Concolic testing enables automatic and systematictesting of programs, avoids redundant test cases and does not generatefalse warnings. Experiments on real-world software show that concolic testing can be used to effectively catch generic errors such as assertion violations, memory leaks, uncaught exceptions, and segmentation faults.

**ii3. Anchor events** : They are a small set of events,  that are responsible for setting the necessary program state for a target to be executed.Here, the target generally requires execution of a series of event handlers that mutate the program state executing the event handler that contains the target.

**ii4. Connector Events** : They are a disjoint set of events used only for connecting the initial state, the anchor events, and the target. These connector events do not affect the program state used at any anchor event or at the target.

**ii5. Sequence Generation** : The event sequence generation is a technique that starts from the target and builds a sequence of events backward until it reaches the initial state. Thus, combining individual paths from the event handler summaries compositionally.


####iii. Artifacts

**iii1. Motivational Statements:**

- Anand et al. approached  automated testing for Android applications using concolic execution. However, their approach ex- plores the application starting from the its entry point, not aiming for particular targets

- Monkey is a popular random testing tool for Android that has been shown to be effective for bug finding .Other tools like A2T2, AndroidRipper , iCrawler, and EXSYST enhance random testing by using the application GUI to guide the testing. These light-weight techniques can be a good starting point for automated testing. However, as they have a black-box view on the application code, they are generally unable to reach the challenging targets

- Tools such as  Dynodroid employ feedback-directed automated testing, which is based on random testing but prioritizing using information gathered during the testing. Such techniques can often obtain good coverage with fewer test inputs that involve symbolic execution.However, they are not suitable for the more challenging targets.

**iii2. Related Work** : 

1. [Kin-Keung Ma, Yit Phang Khoo, Jeffrey S. Foster,and Michael Hicks. Directed symbolic execution. In Proc. 18th International Static Analysis Symposium, 2011.](http://www.cs.umd.edu/~jfoster/papers/sas11.pdf)   
They wrote about line reachability for simple C programs.It consisted of an algorithm that works backward in the call graph from a given target, using traditional forward symbolic execution of each function, until it finds a feasible path from the start of the program. The authors drew inspiration from this work on how to reach a target location in the application code.

2. [Stephan Arlt, Andreas Podelski, Cristiano Bertolini, Martin Scha ̈f, Ishan Banerjee, and Atif Memon. Lightweight static analysis for GUI testing. In Proc. 23rd IEEE International Symposium on Software Reliability Engineering, 2012.](http://www2.informatik.uni-freiburg.de/~arlt/papers/issre2012.pdf)   
The presented a technique where the conventional UI model is augmented by event dependence information that for each pair of event handlers gives an indication of how much state may be written by one of them and read by the other. This information provides the basis for construction of abstract event sequences, which are subsequently extended to executable event sequences using the UI model. The authors found used the approach from this paper to address the path explosion problem encountered during the backward search of the application entry.The authors used this idea of exploiting UI models and event dependence information to narrow the search space.

3. [Patrice Godefroid, Nils Klarlund, and Koushik Sen. DART: directed automated random testing. In Proc. ACM SIGPLAN Conference on Programming Language Design and Implementation, 2005.](http://dl.acm.org/citation.cfm?id=1065036)
They wrote about a technqiue called DART: directed automated random testing.DART detects standard errors such as program crashes, assertion violations, and non-termination.The authors used DART to preprocess the application by performing con-
colic execution of each event handler to infer path conditions and symbolic states for its paths.

 
**iii3. Checklists:** : 

The authors presented the approach divided into two phases: a target agnostic symbolic summarization phase, followed by a sequence generation phase that searches for a test case for each target.

- [x] ***Symbolic summarization:***  This produces an event handler summary is a set of path summaries, one for each execution path within the event handler code.Event handler are computed by concolic execution Each iteration of concolic execution symbolically explores one path and hence computes its path summary.

- [x] ***Event sequence generation:*** The event sequence generation generates a test case for each given target, based on the event handler summaries generated in the previous phase. The algorithm which summarized the event sequence explores backward is given below:

![The event sequence generation algorithm](https://cloud.githubusercontent.com/assets/10588000/10830759/e364975e-7e57-11e5-8d6a-a2952c6377a4.png)

The input ***target*** denotes the target of interest, ***summaries*** is the set of all handler summaries produced in the symbolic summarization phase, and **model** is the UI model of the application. The algorithm either returns a ***test case*** that reaches the target, returns that it is unable to find a ***test case***, or it diverges.

- [x] ***Anchors function:*** An anchor is an execution path in an event handler that writes to some program state that the partial sequence depends on, according to its path condition.The anchors function produces a set of anchors for a partial sequence.

- [x] ***Connector Sequences:*** The ***paths*** function generates a set of possible connector sequences between the given anchor and partial sequence. These sequences has the pre-defined properties ensured by a basic graph traversal algorithm and anchor property.

- [x] ***Prioritization:*** The key part of the technique is the prioritize function that assigns priorities to newly added partial sequences. This function initially selects the priority of a new sequence as the priority of the sequence it extends.
      
**iii4. Patterns:**

For the purpose of analysis of the best practices to perform this kind of testing, the following questions are the best way to tune the finding. They are proposed as:

1. Is the algorithm able to generate test cases for challenging targets in real-world Android applications?A target is classified as being “challenging” if it cannot be reached with traditional random testing or model-based testing techniques.

2. Does the use of anchors and connectors have an effect on the the ability to reach the targets? A simple alternative would be a backward breadth-first search in the UI model.

3. Do the prioritization heuristics have an effect on the ability to reach the targets? If that mechanism is disabled, the partial sequences in the worklist will be treated in a random order.




####iv. Scope for Improvement

**ii1. Platform dependency** : The scope of this paper is limited to automated testing for Android applications that are not computationally heavy but may have complex user interaction patterns. However, extending this framwork to other platforms would present an automated solution in general. Most of the apps in the marketplace are computationally heavy with complex usages. The core problem faced these days in testing, is those kind of applications which are UI heavy. A lot of techinques are written to debug simple apps, but roubust techniques to needed to deal with apps with commplex UI. The work can be extended to testing JavaScript web applications and OS GUI applications.

**ii2. UI input requirement** : One of the limitation of this model is that it requires UI models as input. This can be corrected by integrating existing frameworks for automatic UI model construction. Such a remedy would enable a larger scale experiment in which Android applications are automatically analyzed and tested.

**ii3. Reaching other targets** : Collider, the tool discussed produces event sequences for challenging/unreachable targets. However, part of the remaining targets can also be reached using the prototype, provided that the symbolic constraint solver component is included with better support.




