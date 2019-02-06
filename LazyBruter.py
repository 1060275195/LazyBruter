#!/usr/bin/env python
import smtplib
import os
import itertools
#display logo

print("         _                           ______                                 ")
print("	| |                         (____  \             _               ")
print("	| |      ____ _____ _   _    ____)  ) ____ _   _| |_  ____  ____ ")
print("	| |     / _  (___  ) | | |  |  __  ( / ___) | | |  _)/ _  )/ ___)")
print("	| |____( ( | |/ __/| |_| |  | |__)  ) |   | |_| | |_( (/ /| |     ")  
print("	|_______)_||_(_____)\__  |  |______/|_|    \____|\___)____)_|   ")
print("	                   (____/                                      ")
																															  
print		("\nThis tool is a bruter tool that is meant to crack email password.")

"""
This tool is meant for research purposes only
and any malicious usage of this tool is prohibited.

@author TheBrowserPirates <tthebrowserpirates@gmail.com>

@date 14/01/2019
@version 1.0.1

LICENSE:
This software doesn't have any license.

LEGAL NOTICE:
THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY!
IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY
THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT.
BY USING THIS SOFTWARE YOU AGREE WITH THESE TERMS.
"""
#endbanner
print ("\nLazyBruter is still on Beta, you might experience some bugs!")

print ("Opening LazyBruter v1.2 (Beta)...")
proxyconfirm = input ("\nDo you want to enable proxy? [y/n]")
if proxyconfirm == "y":
	print ("Opening a new shell to generate proxies...")
	os.system('start cmd /D /C "py proxychanger.py"')
	
	if proxyconfirm == "n":
	    print (method_attack)

method_attack = input("Choose which to Bruteforce > \n(a)Gmail \n(b)Yahoo \n(c)Live \n(d)PHP Website \n(e).Zip Files \n(h)Help \n(x)Exit \n=> ")
if method_attack == "a":
    print("\nOpening Gmail Shell...")
    os.system('start cmd /D /C "py lazybruter_gmail.py"')
	
if method_attack == "b":
    print("\nOpening Yahoo Shell...")
    os.system('start cmd /D /C "py lazybruter_yahoo.py"')
	
if method_attack == "c":
    print("\nOpening Live Shell...")
    os.system('start cmd /D /C "py lazybruter_live.py"')
	
if method_attack == "d":
    print("\nOpening PHP Shell...")
    os.system('start cmd /D /C "py lazybruter_php.py"')	

if method_attack == "e":
    print("\nOpening Zip Shell...")
    os.system('start cmd /D /C "py lazybruter_zip.py"')

if method_attack == "x":
    input('Press ENTER to exit') 
	
if method_attack == "h":
    input("\nOpening Help Shell...")
    os.system('start cmd /D /C "py lazybruter_help.py"')

else:
    print("Wrong Input. Try again.")
    print (method_attack)