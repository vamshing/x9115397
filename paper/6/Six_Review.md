## Paper review - Six
####i. [Automated testing with targeted event sequence generation](http://dl.acm.org.prox.lib.ncsu.edu/citation.cfm?id=248377)
***Year :*** 2013
***Citations :*** 16

####ii. Keywords

**ii1. Symbolic execution** : 

**ii2. Concolic execution** : Concolic testing enables automatic and systematictesting of programs, avoids redundant test cases and does not generatefalse warnings. Experiments on real-world software show that concolictesting can be used to effectively catch generic errors such as assertion violations, memory leaks, uncaught exceptions, and segmentation faults.

**ii3. Empirical bug studies** :

**ii4. Tracing** : 


####iii. Artifacts

**iii1. Related Work** : 

1. [Kin-Keung Ma, Yit Phang Khoo, Jeffrey S. Foster,and Michael Hicks. Directed symbolic execution. In Proc. 18th International Static Analysis Symposium, 2011.](http://www.cs.umd.edu/~jfoster/papers/sas11.pdf)   
They wrote about line reachability for simple C programs.It consisted of an algorithm that works backward in the call graph from a given target, using traditional forward symbolic execution of each function, until it finds a feasible path from the start of the program. The authors drew inspiration from this work on how to reach a target location in the application code.

2. [Stephan Arlt, Andreas Podelski, Cristiano Bertolini, Martin Scha ̈f, Ishan Banerjee, and Atif Memon. Lightweight static analysis for GUI testing. In Proc. 23rd IEEE International Symposium on Software Reliability Engineering, 2012.](http://www2.informatik.uni-freiburg.de/~arlt/papers/issre2012.pdf)   
The presented a technique where the conventional UI model is augmented by event dependence information that for each pair of event handlers gives an indication of how much state may be written by one of them and read by the other. This information provides the basis for construction of abstract event sequences, which are subsequently extended to executable event sequences using the UI model. The authors found used the approach from this paper to address the path explosion problem encountered during the backward search of the application entry.The authors used this idea of exploiting UI models and event dependence information to narrow the search space.

3. [Patrice Godefroid, Nils Klarlund, and Koushik Sen. DART: directed automated random testing. In Proc. ACM SIGPLAN Conference on Programming Language Design and Implementation, 2005.](http://dl.acm.org/citation.cfm?id=1065036)
They wrote about a technqiue called DART: directed automated random testing.DART detects standard errors such as program crashes, assertion violations, and non-termination.The authors used DART to preprocess the application by performing con-
colic execution of each event handler to infer path conditions and symbolic states for its paths.

 
**iii2. Checklists:** : 

- [x] ***Test Case Generation:*** 

- [x] ***Automatic Event Generation:*** 

- [x] ***Trace Generation:*** 

- [x] ***Log File Analysis and Bug Detection:*** 
      
**iii3. Baseline Results:**



**iii4. Sampling procedures:**


####iv. Scope for Improvement

**ii1. Robustness** : 

**ii2. Extending to testing concurrent applications** :

**ii3. Platform dependency** : The scope of this paper is limited to automated testing for Android applications that are not computationally heavy but may have complex user interaction patterns. However, extending this framwork to other platforms would present an automated solution in general. Most of the apps in the marketplace are computationally heavy with complex usages. The core problem faced these days in testing, is those kind of applications which are UI heavy. A lot of techinques are written to debug simple apps, but roubust techniques to needed to deal with apps with commplex UI. The work can be extended to testing JavaScript web applications and OS GUI applications.

**ii4. Bug Fixes** :  

