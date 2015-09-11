# Summary

## (i)Reference:
[D. Amalfitano, A. Fasolino, S. Carmine, A. Memon,
and P. Tramontana. Using GUI ripping for automated
testing of Android applications. *In Proceedings of 27th
Intl. Conf. on Automated Software Engineering
(ASE)*, 2012](http://dl.acm.org/citation.cfm?id=2351717)

## (ii)Keywords:
######(ii1)Testing Tools:
The purpose of a testing tool is to run a piece of software through a suite of testcases for the purpose of discovering flaws in the design or bugs in the code.
The testing tool being discussed in the paper is *AndroidRipper*.
######(ii2)Android:
Android is an Operating System(OS) developed by Google primarily for touchscreen mobile devices. 
######(ii3)Testing Automation:
The process of using a software to conduct the execution of a suite of test cases on another software is called test automation. The testing software also compares the actual outcomes of a test case with the predicted outcomes.
######(ii4)GUI Tree:
An intuitive represenation of the structure extracted during ripping. The nodes of the tree represent the individual User-Interfaces(screens) in the App, while the edges between them show the transition as a hierarchial relationship. Each node encapsulates the state of User-Interface,its objects and its properties.
######(ii5)Ripping:
A dynamic process in which the Graphic-User-Interface(of software or app) is automatically traversed by opening all the windows(or screens) and then extract all the widgets' properties and values. This extracted information is verified and used by the test designer to generate multiple test cases. GUI ripping helps to understand both structural and execution behaviour of the GUI.
######(ii6)Bugs:
Errors which produce undersirable outcome during app usage, also responsible for app malfunction. Popularly, andriod bugs are *Activity*-based which arise due to incorrect implementation of activity protocol, *Event*-based which arise when the app performs a wrong action for an incoming event, and *Dynamic*-based which come up due to runtime exceptions.

##(iii)Features:
######(iii1)Motivation:
Given the increasing popularity of Android applications, detecting and fixing bugs has become imperative. With the numbers in PlayStore soaring,there is a push for testing these apps at lower cost by focusing on automating the testing process.Even though developed on a Java Platform, Android applications(developed on Android Development Framework) differs greatly from the Java client-server framwork. This gap in understanding from the developer's standpoint leaves room for defect injection. Thus, the chief motivation of *Amalfitano et. al* is to develop an automated testing software that is capable of testing Android applications via their GUI. Introducing *AndroidRipper*. AndroidRipper analyzes the GUI dynamically, introducing new test cases as and when new events are encountered.

######(iii2)Related Work:
* The work of *Hu et al.*(Cuixiong Hu and Iulian Neamtiu. 2011. Automating GUI testing for Android applications) wrote about  classification of Android bugs into Activity,Event,Dynamic types was very important. This paper also focussed on a Android-based test case generation technique.
* The authors also looked at *Monkey*-an android application that generates a sequence of random events(clicks,touches etc)
* Another work that looked at the automatic testing approach was that of *Amalfitano et al.*(D. Amalfitano, A. R. Fasolino and P. Tramontana, A GUI Crawling-Based Technique for Android Mobile Application Testing). In this proposed approach,a GUI tree model is constructed by simulating various user actions on the GUI.The nodes of the tree represents the user inerfaces and edges the various event based transitions between the interfaces. This established a structure for generating test cases automatically.
* Liu et al.(Zhifang Liu, Xiaopeng Gao and Xiang Long. 2010. Adaptive Random Testing of Mobile Application) proposed a model that combined parts of the event based testing and random testing. In this method of testing various user events and context events(GPS,chat freinds etc) are taking into account and random test cases are generated by aid of the *Monkey*. The paper states that this method is superior to earlier practice of pure random test case generation.

######(iii3)Study Instruments:
Inorder to test their tool - *AndroidRipper*, they made it go through the paces on an Android application called *Wordpress*, an application that manages blogs by saving them onto a server.

######(iii4)Baseline Results:
The authors tested their tool *AndroidRipper* on an Android application called *Wordpress*. It turned out that AndroidRipper was extremely effective and went on to reveal four bugs in less than five hours previously undocumented. The below table shows the data retrieved by AndroidRipper after 3 rounds of testing(R1,R2,R3) and the data retrieved by testing using a Monkey tool(RM)

![screen shot 2015-09-09 at 8 03 33 pm](https://cloud.githubusercontent.com/assets/8950958/9777246/896837f0-572f-11e5-899c-f1e0215b1585.png)

*Reference:- D. Amalfitano, A. Fasolino, S. Carmine, A. Memon,and P. Tramontana. Using GUI ripping for automated testing of Android applications(Table 2)*

##(iv)Improvements:
######(iv1)The paper lacks a Future Work section. Hence, nothing was mentioned about its scope and about how the authors intend to extending their work.
######(iv2)In the paper, the test results of only one application- *WordPress* is specified. It would have been nice to see how *AndroidRipper* performs on other different types of applcations. Will the test cases generted differ then?
######(iv3)In the comparison chart, *AndroidRipper* has been compared to just the Random Monkey model of testing. The paper also alludes to a testing method developed by Liu et al.(Zhifang Liu, Xiaopeng Gao and Xiang Long. 2010. Adaptive Random Testing of Mobile Application) and it is specifically mentioned that this method is superior to the random form of testing. It would have been a good idea to include the test results of this model in the comparison chart. 