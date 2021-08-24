import json
import re

def menu2(path):
    with open(f'{path}/data/recipients.json','r') as file:
        email_list = json.loads(file.read())
    
    while(True):
        print("The stored email addresses are: ")
        for i in email_list:
            sl = re.findall('.+\.',email_list[i])[0][:-1]
            name = re.findall('\..+',email_list[i])[0][1:].strip()
            print(f'{sl}. {i}: {name}')
        break

menu2('/root/work/PyEmail')