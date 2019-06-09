# Welcome to the LazyBruter wiki!

## Introduction
     _                           ______                                
	| |                         (____  \             _               
	| |      ____ _____ _   _    ____)  ) ____ _   _| |_  ____  ____ 
	| |     / _  (___  ) | | |  |  __  ( / ___) | | |  _)/ _  )/ ___)
	| |____( ( | |/ __/| |_| |  | |__)  ) |   | |_| | |_( (/ /| |      
	|_______)_||_(_____)\__  |  |______/|_|    \____|\___)____)_|  
	                   (____/                                     
					
This tool is a bruter tool that is meant to crack email password. 
This tool is meant for research purposes only and any malicious usage of this tool is prohibited.

## Short Description
What is LazyBruter? LazyBruter is one of its first-kind Email Bruteforcer. Using only 2 threads, LazyBruter can bruteforce passwords 200% faster than any ordinary bruter, thanks to its 2-inverted-threads.

## Version
This is the Beta version of LazyBruter (v1.2), but we are improving day by day.

## Got any question?
Email us on: `tthebrowserpirates@gmail.com`
***

# Download and Updates in Windows (Python above 3.0)

If you are running on a Windows system with Python 3.x, type the following command from a terminal to go to LazyBrute Directory:

`C:\User\Desktop> cd LazyBruter`

Before running the program, install all the requirements by entering the following command:

`C:\User\Desktop\LazyBruter> py -m pip install requirements.txt`

After you enter the specified directory, run the program by entering the following command:

`C:\User\Desktop\LazyBruter> py lazybruter.py`

Where C:\Python37 is the path where you installed Python >= 3.0



# Download and Updates in Linux (Python above 3.0)

You can download the latest tarball by clicking [here](https://github.com/TheBrowserPirates/lazybruter.git)
Preferably, you can download LazyBruter by cloning the Git repository:

`git clone https://github.com/TheBrowserPirates/lazybruter.git`

You can update it at any time to the latest development version by running:

`py lazybruter --update`

# Features
LazyBruters can provide different features (for more information [click here](https://github.com/TheBrowserPirates/lazybruter/wiki/Technique))


* Full support of PHP vulnerable websites

It is possible to provide a single target URL, get the list of targets from Burp proxy or WebScrab proxy requests log files, get the whole HTTP request from a text file or get the list of targets. Tests provided GET parameters, POST parameters, HTTP proxies.

* 2-inverted-threads Algorithm

This algorithm excecutes 2x faster, which means passwords are crackable 2x faster than any ordinary bruter.

# Demo
Coming soon on my youtube channel.

# License

LazyBruter is (C) 2019-2020 [TheBrowserPirates](mailto:tthebrowserpirates@gmail.com)

## GNU GENERAL PUBLIC LICENSE

_ Version 3, 29 June 2007_
 _Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>_
 _Everyone is permitted to copy and distribute verbatim copies_
 _of this license document, but changing it is not allowed._


# Disclaimer

THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY!
IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT.
BY USING THIS SOFTWARE YOU AGREE WITH THESE TERMS.

# Techinque
LazyBruter is a powerful Email Provider Password Hash Cracker which uses 2 techniques of password bruting.

* Brute-Forcing (random password string generator)
LazyBruter combines all possible way of password string generating including special characters
This is the list of characters used by algorithm: `abcdefghijklmnopqrstuvwxyz1234567890!#$%&'*+-/=?^_`{|}~;`

* Dictionary (generating custom strings)
If you think that Brute-Forcing isn't that neccesary, Dictionary attack might be effectively. You can create your own wordlist or simply download one from internet (I reccommend Rockyou.txt with more than 14 million passwords). This method is reccomended due to the threads algorithm.

## HTTP Proxy Support
LazyBruter, uses HTTP Proxy which gives the attacker the anonimity. Many email services such as gmail, yahoo and hotmail, detects proxies and block them, but LazyBruter generates proxies every 10 seconds.
