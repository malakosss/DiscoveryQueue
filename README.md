# DiscoveryQueue

Improve your Spotify playlists through this rapid method of song discovery -- Happy hunting!

## Overview

At a basic level, this program will interface with your Spotify active device and modify (add to) your queue. 

DiscoveryQueue works by having you provide a Starting Artist and then it adds the top songs from the Related Artists of your designated Starting Artist to your queue. I frequently utilized this method of song discovery (by sifting through related artists) and really wanted to find a way to automate the process. DiscoveryQueue is just that! Although I may be a bit biased, I have found that DiscoveryQueue has made my playlists much more unique, deep, and enjoyable. All while requiring me to put in less work than I previously did for similar results.

I hope that you find it equally as useful and easy to use!

## Key Considerations for Getting Started

From my testing with some friends of mine, I have found that there are some common pitfalls that may prove to be obstacles:

*(1)* **Keep in mind that your browser or anti-virus will most likely think whichever .zip you download is a virus.** For what it's worth, I can tell you that it is not. Please see "Program Walkthrough" to see screenshots of the program in action and the DiscoveryQueue.py file to see the exact lines that will be run by the .exe.

*(2)* **I'd recommend that you export the Windows or macOS .zip to a folder that includes the .exe file.** The .exe file will produce a user.cache file that will house your permission token (that gives the program permission to alter your queue).

*(3)* **Don't be alarmed if/when the program kicks you out to your browser and asks you to login to your Spotify account.** It will ask you to allow the program to modify your queue. You must provide permission so that the program can do its thing.

*(4)* **It is critical that you have a device (i.e., phone or laptop) actively playing music on Spotify to allow the program to work properly.** This essentially sets your "Active Device" which the program will coordinate with to add to your queue. If you don't have music playing, then the program won't be able to modify your queue. *(THIS IS THE MOST COMMON ISSUE)*

*(5)* **Be sure to fullscreen the application so you can make the most of the logo/title.** :)

## Program Walkthrough

**(1)**  
![stepOne](https://github.com/malakosss/DiscoveryQueue/blob/main/images/StepOne.JPG)
Start off by choosing your Starting Artist. Make sure that you type in the name that would appear on Spotify (capitals and such included).

**(2)**
![stepTwo](https://github.com/malakosss/DiscoveryQueue/blob/main/images/StepTwo.JPG)
Next, you choose the number of songs you want added to your queue from the top 10 of each Related Artist (in this case, I chose to include the top 2 most played songs of each Related Artist). Also, you will have the option to choose the country by which the top 10 songs are defined. So, by choosing "US" the program will base the Related Artists' top 10 from their most listened to songs in the US.

**(3a)**
![stepThree](https://github.com/malakosss/DiscoveryQueue/blob/main/images/StepThree_NoChooseRelatedArtists.JPG)
If you decide to say "no", you will be asked to input the number (from 1 to 20) of Related Artists that you would like to use to produce your queue. In this case, I chose 5 Related Artists and will have a queue produced out of the top songs of the 5 *immediately* Related Artists to the Starting Artist. *DONE!*


**(3b) - Picking Your Related Artists**
![stepThreeYes](https://github.com/malakosss/DiscoveryQueue/blob/main/images/StepThree_ChooseRelatedArtists.JPG)
If you decide to say "yes", then the twenty Related Artists will be printed for your viewing. They are numbered for your convienence when choosing your subsection to use for forming your queue.


![stepFourIndex](https://github.com/malakosss/DiscoveryQueue/blob/main/images/Artist_Index.JPG)

First, define the index (number) of the Related Artist that you would like to start your subsection with. In this case, I chose to include the 10th Related Artist and to exclude those previouse Related Artists (1 throught 9). Next, define the index (number) of the Related Artist that you would like to end your subsection with. In this case, I chose to end the subsection with the 14th Related Artist.

As a result of these inputs, a queue will be produced with the top songs from the 10th, 11th, 12th, 13th, and 14th Related Artist. *DONE!*


## Coding Schtuff

*I'd recommend that you reference the DiscoveryQueue.py file for the cold, hard code.*

I referenced and made use of only the "spotipy" module when making DiscoveryQueue. It is a Python implementation of the Spotify API. You can see the spotipy documentation at **[THIS LINK](https://spotipy.readthedocs.io/en/2.17.1/)**. Also, Spyder IDE was used for programming *(it has a very nice way of viewing variables that made navigating the lists within dictionaries within dictionaries quite easy)*.

Once the DiscoveryQueue.py file was created and validated in the Spyder IDE. I utilized "pyinstaller" in the Windows *Command Prompt* and macOS *Terminal* to produce the .exe that is available for download. You can learn how to use "pyinstaller" at **[THIS LINK](https://realpython.com/pyinstaller-python/)**. In a highlevel overview, I navigated to the folder on my Desktop that included cli.py *(see link for why this was necessary)* and DiscoveryQueue.py with the *cd* command. Then to produce the .exe, I utilized the line *pyinstaller cli.py --onefile --name DiscoveryQueue*.

