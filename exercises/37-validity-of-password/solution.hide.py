import re

def valid_password(password):
    value = []
    items=[x for x in password.split(',')]
    for p in items:
        if len(p)<6 or len(p)>12:
            continue
        else:
            pass
        if not re.search("[a-z]",p):
            continue
        elif not re.search("[0-9]",p):
            continue
        elif not re.search("[A-Z]",p):
            continue
        elif not re.search("[$#@]",p):
            continue
        elif re.search("\s",p):
            continue
        else:
            pass
        value.append(p)
    return (",".join(value))

print(valid_password("ABd1234@1,ABd1234@1,2w3E*,2We3345"))
