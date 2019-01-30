import zipfile

def main():

    zipfilename = input("Enter the .zip File name: ")
    dictionary = input("Enter the wordlist file name: ")
	
    zip_file = zipfile.ZipFile(zipfilename)
    
    with open(dictionary, 'r') as f:

        for line in f.readlines():
            password = line.strip('\n')
           
            try:
                zip_file.extractall(pwd=password)
                password = ("Password found: ",password)
                input("Press Enter to save the result in .txt")
                file = open("password cracked.txt","w")
                file.write(".Zip File: ")
                file.write(zipfilename)
                file.write("    Password: ")
                file.write(password)
                file.close()
                input("Password saved! Search for <password cracked.txt> in LazyBruter Folder")
                break
			
            except:
                print("Incorrect password: ", password)

 

if __name__ == '__main__':

	main()