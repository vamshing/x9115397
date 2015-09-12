## Paper review -Two
####i. [Zhifang Liu, Xiaopeng Gao and Xiang Long. 2010. Adaptive Random Testing of Mobile Application. In Proceedings of the 2nd International Conference on Computer Engineering and Technology (ICCET ’10), IEEE Computer Society, Washington, DC, USA, 2, 297-301.](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5485442)

####ii. Keywords

**ii1. Adaptive Random Testing** : It is an improved version of Random testing for test case generation. ART realizes the fact that the input failure regions of an app cluster together. So, it tries to spread the test case generation as evenly as possible, to detect the first failure. ART is 40-50% more quicker than Random testing to detect the first failure of an app.

**ii2. Test Case generation** : 

**ii3. Black Box View** : of a mobile application is an approach which looks at the apps by observing input and output data. The input could be ***user-based*** such as text,touch input, or ***context-based*** such as GPS information,sensors,activity by the chat,social network etc.The app generates multiple possibilities of output like graphics,audio,vibration,etc based on the combinations of the changing input sequence.

**ii4. Random Technique** : 

####iii. Keywords

**iii1. Motivation** : 
In Black box view, inputs are user-based and context-based. Memon et al. proposed to model GUI applications by Event-flow graphs. Their model accepts a pre-defined set of user inputs and system-generated events which produces a deterministic output. This does not take into account the non-determinism caused by dynamic context-based inputs. Michele Sama et al. proposed adaptice model of apps based on effects of dynamic context-based updates which accounted for the non-determinism. However, their model could not address the super-set of the user-based and context-based triggers.

Lack of cheap and effective techniques for test-case generation is also a strong motivation of the authors. The earlier practice of record-and-replay the test script was highly subjective. The script is recroded while the tester works on manipulating the app.Then, the recorded scipt is iteratively played on the app back-and-forth.The very subjective nature of this testing process proved ineffective. While high-quality testers are always in demand, not everyone could afford them. Whoever could afford them, could churn out high-quality test scripts encompassing all the test action. This was indeed expensive and detrimental to scaling.The authors wanted to address these two problems by an automated and adaptive approach of testing.
