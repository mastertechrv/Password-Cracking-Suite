#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries 
import os
import time

# Colors
class bg:
    input = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    option = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def lock():
    print("\n"+bg.option)                                                            
    print("                                 :;;;;;;;;;;;                    ")                                     
    print("                                ;;;;;;;;;;;;;;;                  ")                                 
    print("                              `;;;;;;;;;;;;;;;;;                 ")                         
    print("                              ;;;;;;`     `;;;;;;                ")                         
    print("                             ;;;;;          ,;;;;`               ")                         
    print("                            .;;;;            ,;;;;               ")                         
    print("                            ;;;;              ;;;;               ")                         
    print("                            ;;;;               ;;;;              ")                         
    print("                           .;;;.               ;;;;              ")                         
    print("                           ;;;;                ;;;;              ")                         
    print("                           ;;;;                .;;;              ")                         
    print("                           ;;;;                                  ")                         
    print("                           ;;;;                .....             ")                    
    print("                       ::::::::::::::::::::::::::::::::          ")                         
    print("                       ::::::::::::::::::::::::::::::::          ")                         
    print("                       ::::::::::::::::::::::::::::::::          ")                         
    print("                       ,:::.                       ::::          ")                         
    print("                       ,:::.          ;;;;         ::::          ")                         
    print("                       ,:::,         ;;;;;.        ::::          ")                         
    print("                       .:::,         ;;;;;;        ::::          ")                         
    print("                       .:::,         ;;;;;,        ::::          ")                         
    print("                         ::::        ;;;;;,      ,::::           ")                         
    print("                         :::::       ;;;;;;      ::::            ")                         
    print("                          ::::,      ;;;;;;     :::::            ")                         
    print("                          ,::::,               :::::             ")                         
    print("                           ::::::            ,:::::              ")                         
    print("                            :::::::.       :::::::`              ")                         
    print("                             ::::::::::::::::::::                ")                         
    print("                              `:::::::::::::::::                 ")                         
    print("                                .:::::::::::::                   ")                         
    print(bg.input+bg.bold+bg.underline+"\n\tPassword Cracking Suit by @SalvaCorts for @TecnoHackOrg"+bg.end)                                                            

# Banner
def banner():
    print("\n"+bg.end+bg.green+"##################################################################################")
    print("#                                                                                #")
    print("#"+bg.underline+bg.bold+bg.input+"\t\t\t   Hash Craking Suite by @SalvaCorts   "+bg.end+bg.green+"                  #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#"+bg.end+bg.bold+"\t\t\t\t·HASH IDENTIFICATION:"+bg.end+bg.green+"                            #")
    print("#                                                                                #")
    print("#"+bg.option +"\t[1]"+bg.blue+"Hash Type"+bg.end+bg.green+"                                                             #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#"+bg.end+bg.bold+"\t\t\t\t·HASH CRACKING:"+bg.end+bg.green+"                                  #")
    print("#                                                                                #")
    print("#"+bg.option+"\t[2]"+bg.blue+" Online Crack\t"+bg.option+"[3]"+bg.blue+" Dictionary Crack\t"+bg.option+"[4]"+bg.blue+" Bruteforce"+bg.end+bg.green+"           #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#"+bg.end+bg.bold+"\t\t\t\t·MISCELLANEOUS:"+bg.green+"                                  #")
    print("#                                                                                #")
    print("#"+bg.end+bg.option+"\t[5]"+bg.blue+" List Dictionaries\t"+bg.option+"[6]"+bg.blue+" Create a Dictionary"+bg.green+"                          #")
    print("#                                                                                #")
    print("#"+bg.end+bg.option+"\t[7]"+bg.blue+" Install Tools\t"+bg.option+"[8]"+bg.blue+" Exit"+bg.green+"                                         #")    
    print("#                                                                                #")
    print("##################################################################################\n"+bg.end)

# bruteforce Banner
def brutBanner():
    print("\n"+bg.end+bg.green+"##################################################################################")
    print("#                                                                                #")
    print("#"+bg.underline+bg.bold+bg.input+"\t\t\t   Hash Craking Suite by @SalvaCorts   "+bg.end+bg.green+"                  #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#"+bg.end+bg.bold+"\t\t\t\t·Incremental Modes:"+bg.end+bg.green+"                              #")
    print("#                                                                                #")
    print("#"+bg.option+"\t[*]"+bg.blue+" Only Letters:"+bg.input+" alpha"+bg.green+"                                                  #")
    print("#"+bg.option+"\t[*]"+bg.blue+" Only Numbers:"+bg.input+" digits"+bg.green+"                                                 #")
    print("#"+bg.option+"\t[*]"+bg.blue+" Letters, Numbers and Special Characters:"+bg.input+" lanman"+bg.green+"                      #")
    print("#"+bg.option+"\t[*]"+bg.blue+" All Characters:"+bg.input+" all"+bg.green+"                                                  #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("##################################################################################\n"+bg.end)   

    
    
    
# Ask if finish
def finish():
    finish = input(bg.input+"\n [+] "+bg.blue+"Finish?(y/n)  >> "+bg.end)
    finish = str(finish)
    if (finish == "y"):
        main()
    else:
        while True:
            finish = input(bg.input+"\n [+] "+bg.blue+"Finish?(y/n)  >> "+bg.end)
            finish = str(finish)
            if finish == "y":
                main()
            else:
                continue

# Online Crack
def online():   
    os.system("clear")
    hash = input(bg.input+"\n [+] "+bg.blue+"Hash? >> "+bg.end)
    hashType = input(bg.input+"\n [+] "+bg.blue+"Hash Encryption? >> "+bg.end)
    hashType = str(hashType)
    os.system("python2 tools/online.py "+hashType+" -h"+" '"+hash+"'")
    
# List Dictionaries
def dics():
    os.system("clear")
    print("\n"+bg.option+"#########################################################################"+bg.end+bg.bold+"\n")
    os.system("ls dics/ | grep '' ")
    print("\n"+bg.option+"#########################################################################"+bg.end)
    print("\n")
    
# Dictionary Creator
def newDic():
    os.system("clear")
    minLen = input(bg.input+"\n [+] "+bg.blue+"Password Minimun Length (the same as pattern)? >> "+bg.end)
    minLen = str(minLen)
    maxLen = input(bg.input+"\n [+] "+bg.blue+"Password Maximun Length? >> "+bg.end)
    maxLen = str(maxLen)
    char = input(bg.input+"\n [+] "+bg.blue+"Characters to be used?[] >> "+bg.end)
    char = str(char)
    pattern = input(bg.input+"\n [+] "+bg.blue+"Pattern to be based on and variations (Ej: word@@ will create word11, word12,...,word99)?[] >> "+bg.end)
    pattern = str(pattern)
    name = input(bg.input+"\n [+] "+bg.blue+"Dictionary Name? >> "+bg.end)
    name = str(name)
    if (char == ""):
        print (bg.option+"\n [*] Running command:  "+bg.end+"crunch "+bg.input+minLen+" "+maxLen+bg.end+" -o dics/"+bg.input+name+bg.end+"\n")
        os.system("crunch "+minLen+" "+maxLen+" -o dics/"+name)
    elif ((char != "") and (pattern == "")):
        print (bg.option+"\n [*] Running command:  "+bg.end+"crunch "+bg.input+minLen+" "+maxLen+bg.input+" "+char+bg.end+" -o dics/"+bg.input+name+bg.end+"\n")
        os.system("crunch "+minLen+" "+maxLen+" "+char+" -o dics/"+name)
    elif (pattern != ""):
        print (bg.option+"\n [*] Running command:  "+bg.end+"crunch "+bg.input+minLen+" "+maxLen+bg.input+" "+char+bg.end+" -t "+bg.input+pattern+bg.end+" -o dics/"+bg.input+name+bg.end+"\n")
        os.system("crunch "+minLen+" "+maxLen+" "+char+" -t "+pattern+" -o dics/"+name)
        
# Hash Type
def HashType():
    os.system("clear")
    os.system("python2 tools/hashid.py")
    
# Dictionary Crack
def dictionary():
    os.system("clear")
    hash = input(bg.input+"\n [+] "+bg.blue+"Hash? >> "+bg.end)
    hashType = input(bg.input+"\n [+] "+bg.blue+"Hash Encryption? >> "+bg.end)
    dictionary = input(bg.input+"\n [+] "+bg.blue+"Dictionary Path? >> "+bg.end)
    addOp = input(bg.input+"\n [+] "+bg.blue+"Additional options? >> "+bg.end)
    f = open("hash.txt", "w")
    f.write(hash)
    f.close()
    print (bg.option+"\n [*] Running command:  "+bg.end+"john --wordlist="+bg.input+dictionary+bg.end+" --format="+bg.input+hashType+" "+addOp+bg.end+" hash.txt"+bg.option+"   With Hash "+bg.input+hash+bg.end+"\n")
    os.system("john --wordlist="+dictionary+" --format="+hashType+" "+addOp+" hash.txt")
    os.system("rm hash.txt")

# Bruteforce Attack
def bruteforce():
    os.system("clear")
    brutBanner() # Display Bruteforce Banner
    hash = input(bg.input+"\n [+] "+bg.blue+"Hash? >> "+bg.end)
    hashType = input(bg.input+"\n [+] "+bg.blue+"Hash Encryption? >> "+bg.end)
    incrementalMode = input(bg.input+"\n [+] "+bg.blue+"Incremental Mode?[] >> "+bg.end)
    f = open("hash.txt", "w")
    f.write(hash)
    f.close()
    if (incrementalMode == ""):
        print (bg.option+"\n [*] Running command:  "+bg.end+"john --incremental --format="+bg.input+hashType+" hash.txt"+bg.option+"    With Hash "+bg.input+hash+bg.end+"\n")
        os.system("john --incremental --format="+hashType+" hash.txt")
        os.system("rm hash.txt")
    else:
        print (bg.option+"\n [*] Running command:  "+bg.end+"john --incremental="+bg.input+incrementalMode+bg.end+" --format="+bg.input+hashType+bg.end+" hash.txt"+bg.option+"   With Hash "+bg.input+hash+bg.end+"\n")
        os.system("john --incremental="+incrementalMode+" --format="+hashType+" hash.txt")
        os.system("rm hash.txt")

# Install Tools
def install():
    # Install Hash Identifier
    print(bg.end+bg.option+"\n [*] Installing Hash Identifier"+bg.end)
    os.system("cd tools && wget https://hash-identifier.googlecode.com/files/Hash_ID_v1.1.py && mv Hash_ID_v1.1.py hashid.py")
    
    # Install Find My Hash
    print(bg.end+bg.option+"\n [*] Installing Find My Hash"+bg.end)
    os.system("cd tools && wget https://findmyhash.googlecode.com/files/findmyhash_v1.1.2.py && mv findmyhash_v1.1.2.py online.py")
    
    # Install John The Ripper
    print(bg.end+bg.option+"\n [*] Installing John The Ripper"+bg.end)
    os.system("sudo pacman -S john") # Archlinux
    os.system("sudo apt-get install john") # Ubuntu
    os.system("sudo yum install john") # Fedora
    
    # Install Crunch
    print(bg.end+bg.option+"\n [*] Installing Crunch"+bg.end)
    os.system("yaourt -S crunch") # Archlinux
    os.system("sudo apt-get install crunch") # Ubuntu
    os.system("sudo yum install crunch") # Fedora    
    
     
    # Everything Done
    print(bg.end+bg.option+"\n\n\n [*] Everything have been installed!"+bg.end)
    
# Main
def main():
    os.system("clear")
    lock()
    time.sleep(1.5)
    os.system("mkdir dics && mkdir tools")
    os.system("clear")
    def init():
        banner()
        option = input(bg.input+" [+] "+bg.blue+"Option?  >> "+bg.end)
        option = option.lower() # Convert user input to LowCase
        option = str(option)
        if (option == "1"): # Hash Type
            HashType()
            finish()
        elif (option == "2"): # Online Crack
            online()
            finish()
        elif (option == "3"): #  Dictionary Crack
            dictionary()
            finish()
        elif (option == "4"): #  Bruteforce Crack
            bruteforce()
            finish()
        elif (option == "5"): # List Dictionaries
            dics()
            init()
        elif (option == "6"): # List Dictionaries
            newDic()
            init()
        elif (option == "7"): # Install Tools
            install()
            finish()
        elif (option == "8"): # Exit
            os.system("clear")
            print(bg.option+"\n Happy Hacking!"+bg.end)
            time.sleep(1)
            os.system("clear")
            exit()
        else:
            os.system("clear")
            print(bg.fail+"\n [!] Type 1, 2, 3, 4, 5 or 6\n"+bg.end)
            time.sleep(1.5)
            main()
    init()

# Start
if __name__ == '__main__':
    main()
