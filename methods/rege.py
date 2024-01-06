import pyperclip as pc
import re
        

       
text = pc.paste()
       
pattern_phone = re.compile(r'''(
    (\d{3}|\(\d{3}\)?)           #area code
    (\s|-|\.)                     
    (\d{3})     
    (\s|-|\.) 
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d))?             
                     
)'''  ,re.VERBOSE |re.IGNORECASE)

pattern_email = re.compile(r'''(
    
    https:\/\/(www\.)?
     [a-zA-Z0-9-%+_]+
    (\.[a-zA-Z]{2,4})?
    |
    [a-zA-Z0-9-%+_]+
    @
    [a-zA-Z0-9_-]+
    (\.[a-zA-Z]{2,4})
    
)''',re.VERBOSE | re.IGNORECASE) 


matches = []
for i in pattern_phone.findall(text):
    phonenum = '-'.join([i[1],i[3],i[5]])
    if i[8] != '':
        phonenum += 'x' + i[8]
    matches.append(phonenum)
    
for i in pattern_email.findall(text):
    matches.append(i[0])
    
if len(matches) > 0 :
    pc.copy('\n'.join(matches))
    print("copied to clipboard")
    print("\n".join(matches))
else:
    print("none matches regarding address and phone number")