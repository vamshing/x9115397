## Paper review - Five
####i. [Automating GUI Testing for Android Applications, 2011 Cuixiong Hu Iulian Neamtiu](http://dl.acm.org/citation.cfm?id=1982612)
***Number of Citations :*** 30

####ii. Keywords

**ii1. Reliability** : In testing activities, one of the primary objectives is to obtain a life distribution that describes the times-to-failure of a component, subassembly, assembly or system. This analysis is based on the time of successful operation or time-to-failure data of the item (component), either under use conditions or from accelerated life tests.

**ii2. Test automation** : Its a process of automatically testing the applications with minimal or no human intervention. It has been an active research topic since the advent of Desktop/Web application. Now, with more than 1.1 million apps in popular markets, test automation has garned a a lot of attention.

**ii3. Empirical bug studies** : The bug recording study of the most popular and most diversely used mobile apps since the 
       Andriod OS came into exitence. The studies are focused on the apps which have a long life time, a detailed bug history
       reported by the developers and users. The reports should consist of broad range of representative bugs.

**ii4. Tracing** : Tracing is the processo f loggin the details of each test case into a trace file. In this paper, the tracing
       activity is carried out while the application is tested against the test cases in the Virtual Machine.Tracing captures 
       three kinds of events: Graphical User Interface (GUI) based, method calls and exceptions.


####iii. Artifacts

**iii1. Related Work** : 

1. [A. Chaudhuri. Language-based security on android. In PLAS ’09](https://www.cs.umd.edu/~avik/projects/lbsa/paper.pdf)      
They wrote about Andriod Verification.They presented a formal study of Android security. Their work included reasoning about their data flow security properties.The appraoch is deployed at the OS level and focus on security.

2. [A. Kervinen, M. Maunumaa, T. Pa ̈a ̈kko ̈nen, and
M. Katara. Model-based testing through a gui. In Formal Approaches to Software Testing, volume 3997, pages 16–31. 2006.](http://link.springer.com/chapter/10.1007%2F11759744_2) 
They presented a formal model and architecture for testing concurrently running applications.     

3. [X. Yuan and A. M. Memon. Generating event sequence-based test cases using gui runtime state feedback. IEEE Trans. on Software Engineering, 36:81–95, 2010.](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5306073&tag=1)  
They proposed a model-based approach for testing GUI-based applications which can generate test cases automatically using a strucural event generation graph.      

4. [A. Kumar Maji, K. Hao, S. Sultana, and S. Bagchi. Characterizing failures in mobile oses: A case study with android and symbian. In Software Reliability Engineering (ISSRE), 2010 IEEE 21st International Symposium on, pages 249–258.](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5635045) 
They performed a failure characterization study on two mobile platforms, Android and Symbian. The study is focused on bug location and the fix.

 
**iii2. Checklists:** : 

- [x] ***Test Case Generation:*** consists of three testings.Initial condition testing tests whether the activity is created properly. GUI testing tests whether the activity performs according to the GUI specification.State management testing tests whether the application can properly enter and exit a state.

- [x] ***Automatic Event Generation:*** To generate GUI events, the authors used Monkey event generator, which comes with the Android SDK. Random sequences are generated by Monkey, and fed the sequences to the application under test.
      
- [x] ***Trace Generation:*** This step is  loggin the details of each test case into a trace file. This is used to detect application bugs that cause the Virtual Machine to shut down prematurely.

- [x] ***Log File Analysis and Bug Detection:*** With the log file , patterns are used to find potential bugs.Also,log files are also useful in debugging, since the log file contains method and event traces, leading to the bug. Detecting Activity bugs,Event Bugs and Type Errors are found at this stage.
      
**iii3. Baseline Results:**

The authors reported the number of bugs found using the approach. For each class of bugs, the re-discovered bugs reported in the Old column as well as new bugs -the New column is shown as the baseline study.

![old (re-discovered) bugs and new (discoverd) bugs.](https://cloud.githubusercontent.com/assets/10588000/10747397/ff8b0078-7c2a-11e5-9b92-58022a418d9a.png)


**iii4. Sampling procedures:**

The samples are the apps which are used to run the testing on. The authors made a more diverse choice of apps with reasoning. 
They made sure that the apps are long running in the market with a decent bug history. The ten apps are free in Android Market, have high download counts, and cover most of application categories to encompass all the bug categoreis.Few of them include Opensudoku,Skylight1,CMIS,DealDroid,MonolithAndroid.


####iv. Scope for Improvement

**ii1. Robustness** : The study has be limited to ten Andriod applications with known bug history. However, no such connection has been established in terms of providing robustness for the framework. There are questions to be address as to how the framework would make bug discovery more reliabl on lesser-popular, lesser-reported applications.

**ii2. Extending to testing concurrent applications** : The proposed model is sequential rather than concurrent. As specified 
in the related literature, extending this framework to test concurrency would make it easier to discover more new bugs.

**ii3. Platform dependency** :  The study is limited to Andriod platform. There is a significant share of mobile phones which
use Symbian as the OS. Extending the work to the Symbian platform would ensure that the testing framework can be generalized.

**ii4. Bug Fixes** :  The authors  rovide an  testing framework that can be used to discover activity bugs, event bugs and type errors. However, since the process uses extensive logging operation, the solution can be improved by proposing the bug fixes by invoking the bug locations in the source code. It is already demonstrated by Maji et al about the patterns in the 
bug defect densities, using the knowledge of bug fixes, would further add to the insights of the paper. 
