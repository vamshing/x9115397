## Paper review -Eight
####i. [Dynodroid: An Input Generation System for Android Apps] (http://cercs.gatech.edu/tech-reports/tr2012/git-cercs-12-09.pdf) 

***Number of Citations :*** 22

***Year :*** 2013

####ii. Keywords

**ii1. Observe-Select-Execute cycle** : The tool presented runs on this principle where it first ***observes*** which events are relevant to the app in the current state, then ***selects*** one of those events and ***executes*** the selected event to yield a new state iin which the process is iterated.

**ii2. Black Box View** :  of a mobile application is an approach which looks at the apps by observing input and output data. The input could be user-based such as text,touch input, or context-based such as GPS information,sensors,activity by the chat,social network etc.

**ii3.Random Technique** : This technique generates random test cases for mobile app testing.It is a fully automatic,non-intrusive and takes a pure random approach in simulation events from a random pool.There is chance that new event generated might be closer to the one generated in the previos event sequence set.

**ii4. Test automation** :  Its a process of automatically testing the applications with minimal or no human intervention. It has been an active research topic since the advent of Desktop/Web application.

####iii. Artifacts

**iii1. Motivation** :

The motivation behind the authors work has been driven by the three testing method & its drawbacks:

- [UI/Application Exerciser Monkey](http://developer.android.com/tools/help/monkey.html): 

   **Fuzz-Testing** generates a sequence of random UI events.Fuzz testing is a black-box approach, it is easy to implement robustly, it is fully automatic, and it can efficiently generate a large number of simple inputs.
  
  **Drawback**: Monkey only generates UI events, not system related events. It would be challenging to randomly generate system events given the large space of possible such events and highly structured meta-data.

- [S. Anand, M. Naik, H. Yang, and M. Harrold. Automated concolic testing of smartphone apps. In Proceedings of ACM Conf. on Foundations of Software Engineering (FSE), 2012.](http://dl.acm.org/citation.cfm?id=2393666): 

  **Systematic-Testing** automatically partitions the domain of inputs such that each partition corresponds to a unique program behavior. Thus, it avoids generating redundant inputs and can generate highly specific inputs.
  
  **Drawback**: In this approach,it is difficult to scale due to the notorious path explosion problem. Moreover, symbolic execution is not black-box and requires heavily instrumenting the app in addition to the framework.

- [ GUITAR: A model-based system for automated GUI testing.](http://guitar.sourceforge.net/.): 

   **Model-based testing** harnesses human and framework knowledge to abstract the input space of a program’s GUI, and thus reduce redundancy and im- prove efficiency program behavior. Thus, it avoids generating redundant inputs and can generate highly specific inputs.
  
  **Drawback**: In this approach, the tool predominantly target UI events as opposed to system events.

**iii2. Baseline Results** :

**Comments:** The authors made a baseline study of the proposed tool with the Monkey tool. Dynodroid uses fixed parameter values for UI events whereas Monkey uses random values. It gives superior ability to exercise custom widgets. In terms of the total code covered for each app, Dynodroid outperforms Monkey, achieving higher coverage for 30 of the 50 apps.

This summary below lists the baseline results of the Code coverage taking the Monkey results as baseline approach.

![The Code coverage comparison of techniques](https://cloud.githubusercontent.com/assets/10588000/11007098/9e464cb4-8495-11e5-94eb-19108d50165f.png)



**iii3. Informative visualizations:** : 

The visualizatiobn below shows the  minimum number of events that were needed by each automated approach Monkey, and Dynodroid using each of the selection strategies to achieve peak code coverage for each of the 50 apps authors selected.

![fig](https://cloud.githubusercontent.com/assets/10588000/11007256/acb7e84c-8496-11e5-9791-a8ca4bfa5f73.png)


**iii4. Patterns:**

For the purpose of analysis of the best practices to perform this kind of testing, the following questions are the best way to address the performance of Dynodriod. They are proposed as:

1. **Robustness:** Does the system handle real-world apps?
   The authors applied Dynodriod to a suite of 50 diverse, real- world open-source apps, and compared its performance to two state-of-the-art input generation approaches.

2. **Black-box:** Does the system forgo the need for app sources and the ability to decompile app binaries?
Dynodriod operates on unmodified app binaries, it can generate both UI inputs and system inputs, and it allows combining inputs from human and machine.

3. **Automated:** Does the system reduce manual effort?
    The authors showed that Dynodroid can significantly automate testing tasks that users consider tedious.

4. **Efficient:** Does the system generate concise inputs, i.e., avoid generating redundant inputs?
    The authors showed that Dynodroid can significantly generate more concise input sequences than ***Monkey***


####iv. Scope for Improvement

**ii1. Speed** :  The tool Dynodroid developed by the authors is 5X slower than Monkey. The reason for the slowdown is the ViewServer service in Android, is slow due to heavy use of reflection. It can be imporoved by introducing a new commands that makes ViewServer run 20X-40X faster as shown in these [android-app-testing-patches](http://code.google.com/p/android-app-testing-patches/)

**ii2. OS Support** : Dynodroid currently supports only the Gingerbread version of Android. This may hinder its adoption for a fast-evolving platform like Android. This problem, however, is solved by the fact that Dynodroid instruments the SDK at the source-code level, and a patch could be created to use it in other Andriod versions.

**ii3. Non-determinism** :  in programs is problematic for any dynamic analysis. One simple way to alleviate non-determinism would be to treat all asynchronous operations synchronously.

**ii4.In App Communication** : Dynodroid restricts apps from communicating with other apps and reverts to the app under test upon observing such communication. However, many Android apps use other apps for shared functionality(ex.browsing). The authors could have addresses this problem since there are lot of dependencies.

