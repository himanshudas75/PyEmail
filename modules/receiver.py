import json
import re
from clear import clean

menu2="""\

1> Add email(s)
2> Delete email(s)
3> Back

Enter an option: """

addemail="""\
-> Enter the e-mail addresses to add (one in each line)
-> If you want to add a name as well, write it after a colon (:)
-> To stop entering, enter STOP (case insensitive)
Example:
test@example.com
hello@work.com
money@cash.com: Money Man

NOTE: Entering an email which already exists will just overwrite it with the name you enter now

"""

delemail="""\
-> Enter the e-mail addresses to delete (comma-separated, or line-by-line)
-> You can enter either the e-mail address, serial number, or name
-> In case of ambiguity, appropriate message will be shown
-> In case of numbers, if you want to delete a range of e-mail addresses, enter it like - 2:5
-> Enter SHOW to show the current list of e-mail addresses
-> Enter STOP to stop deleting and return to the menu

"""
def print_email(email_list):
    print("The stored email addresses are: ")
    for i in email_list:
        sl = re.findall('.+\.',email_list[i])[0][:-1]
        name = re.findall('\..+',email_list[i])[0][1:].strip()
        print(f'{sl}. {i}: {name}')

def add_email(email_list, path):
    clean()
    l = len(email_list)
    print(addemail)
    while(True):
        text = input()
        if 'STOP' in text.upper():
            break
        if ':' in text:
            email=re.findall('.+:',text)[0][:-1].strip()
            name=re.findall(':.+',text)[0][1:].strip()
        else:
            email=text
            name=re.findall('.+@',email)[0][:-1].strip()

        l+=1
        email_list[email]=f'{l}. {name}'

    with open(f'{path}/data/recipients.json','w') as file:
        json.dump(email_list, file, indent=4)
    return

def del_email(email_list, path):
    clean()
    print(delemail)
    while(True):
        text = input()
        if 'STOP' in text.upper():
            break
        elif 'SHOW' in text.upper():
            print()
            print_email(email_list)
            print()
        else:
            text = text.split(',')
            for i.strip() in text:
                if i.isnumeric():
                    i = int(i)
                    if i > len(email_list):
                        i = len(email_list)
                    for email in email_list:
                        sl = re.findall('.+\.',email_list[email])[0][:-1]
                        if int(sl.strip()) == i:
                            pop = email_list.pop(email,-1)
                            break
                elif ':' in text:
                    text = text.split(':')
                    


def email_receive(path):
    with open(f'{path}/data/recipients.json','r') as file:
        email_list = json.load(file)
    
    while(True):
        clean()
        print_email(email_list)
        
        print(menu2,end="")
        opt = int(input())
        if opt == 1:
            add_email(email_list, path)
        elif opt == 2:
            del_email(email_list,path)
        else:
            break

email_receive('/root/work/PyEmail')