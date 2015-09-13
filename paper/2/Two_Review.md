## Paper review -Two
####i. [Zhifang Liu, Xiaopeng Gao and Xiang Long. 2010. Adaptive Random Testing of Mobile Application. In Proceedings of the 2nd International Conference on Computer Engineering and Technology (ICCET ’10), IEEE Computer Society, Washington, DC, USA, 2, 297-301.](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5485442)

####ii. Keywords

**ii1. Adaptive Random Testing** : It is an improved version of Random testing for test case generation. ART realizes the fact that the input failure regions of an app cluster together. So, it tries to spread the test case generation as evenly as possible, to detect the first failure. ART is 40-50% more quicker than Random testing to detect the first failure of an app.

**ii2. Test Case generation** : Test cases are the actions formed by a set of events. The set of events form a action to be tested on a mobile app so as to observe the output. The primary aim is to look for where apps malfuncion against a given test case.

**ii3. Black Box View** : of a mobile application is an approach which looks at the apps by observing input and output data. The input could be ***user-based*** such as text,touch input, or ***context-based*** such as GPS information,sensors,activity by the chat,social network etc.The app generates multiple possibilities of output like graphics,audio,vibration,etc based on the combinations of the changing input sequence.

**ii4. Random Technique** : This technique generates random test cases for mobile app testing.It is a fully automatic,non-intrusive and takes a pure random approach in simulaiton events from a random pool.There is chance that new event generated might be closer to the one generated in the previos event sequence set.

####iii. Notes

**iii1. Motivation** : 
In Black box view, inputs are user-based and context-based. Memon et al. proposed to model GUI applications by Event-flow graphs. Their model accepts a pre-defined set of user inputs and system-generated events which produces a deterministic output. This does not take into account the non-determinism caused by dynamic context-based inputs. Michele Sama et al. proposed adaptice model of apps based on effects of dynamic context-based updates which accounted for the non-determinism. However, their model could not address the super-set of the user-based and context-based triggers.

Lack of cheap and effective techniques for test-case generation is also a strong motivation of the authors. The earlier practice of record-and-replay the test script was highly subjective. The script is recroded while the tester works on manipulating the app.Then, the recorded scipt is iteratively played on the app back-and-forth.The very subjective nature of this testing process proved ineffective. While high-quality testers are always in demand, not everyone could afford them. Whoever could afford them, could churn out high-quality test scripts encompassing all the test action. This was indeed expensive and detrimental to scaling.The authors wanted to address these two problems by an automated and adaptive approach of testing.

**iii2. Commentary** : One of the novel aspects, we found about the study is the usage of short-hand notation to represent an Event. The figure below gives the illustration. The sequence of events is denoted by the combination of alpha-numeric characters.This helps in selection the events for test-case generation, by applying Levenshien distance to select the farthest event-sequence.

![](https://cloud.githubusercontent.com/assets/10588000/9839341/d66d0b26-5a44-11e5-9f56-fa3d1505ab2d.png)

**iii3. Future work:** : The Adaptive Random testing technique could be further extended to testing for games based on TV. Any event driven software, which has all the events of different kinds would benefit hugely in reducing the number of test cases. Video-games with sensor driven arms would benefit hugely by:

- Reducing the number of test cases needed to arrive at the first fault.
- Finding faults with the different combinations of sensor evets.

The authors performed ART for set-top boxes, and claim to have got the time reduced to find the first fault by 40%.

####iv. Scope for Improvement

**ii1. Choice of  Testing Apps** : The The authors' claim that thier technique encompasses both user-input and context-based events.However, their choice of apps to be tested has been limited to trivial apps, which required a user input and basic User Interface operations. The study could be more comprehensive, if the choice of apps included more sensors like viration,accelerometer,GPS and Bluetooth. For instance, certain food apps pushes restaurant suggestions by vibrating the phone in a short burst. These apps respond to the vibration,light and also the touch instantly to generate an output information.Another instance, is the GPS navigation apps which takes cue from the gravity sensor signals from the phone.The logical mix of events in these apps could be lot more diverse rather than limiting to similar cluster of apps like Dialer and SMS. 

**ii2. Distance calculation metric** : A further enquiry into the distance calculation between the two test cases. The authors used the mean of normalized sequence distance and value distance. However, equal weight allocaiton for both the components might vary depending on the app. For apps, which have multi-input features may have the weights for value component more than sequence distance. So, any empirical study in convergence(here, the F-score) could be useful to give a distribution of weights for different app/app-categories.

**ii3. Clustering of apps** : In an evolutionary space, we would like to collect the cases where success was achieved, and use them to be more successful in future. So, it is imperative to have the test cases where the apps failed so that these test-cases could be used iteratively in similar apps. The mobile industry is far ahead in clustering of apps(refer [xyo - the app recommender which uses clustering](https://play.google.com/store/apps/details?id=net.xyo.app.search&hl=en)).So, testing the successfull test-cases on similar apps could bring down the run-time of the testing effort.





