import re
value=[]
item=[x for x in input("nhap mat khau:").split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.seach("[0-9]",p):
        continue
    elif not re.seach("[A-Z]",p):
        continue
    elif not re.seach("[$#@]",p):
        continue
    elif not re.seach("[\s]",p):
         continue
    else:
         pass
    value.append(p)
    print(",".join(value))
