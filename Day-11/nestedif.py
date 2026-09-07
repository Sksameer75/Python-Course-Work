fa = eval(input("Follows Account:"))
if fa:
    cf = eval(input("Close Friend:"))
    if cf:
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follos the Account First")

reg = eval(input("Registered:"))
if reg:
    fee = eval(input("Fee Paid:"))
    if fee:
        print("Tournament Entry confirmed")
    else:
        print("Entry Fee pending")
else:
    print("Registratin Required")
    


file = eval(input("Link Active:"))
per= eval(input("Permission is granted:"))


if file:
    if per:
        print("Acceess")
    else:
        print("Permission Denied")
else:
    print("Invalid Link")
    


data = {
    'karthik':{'status':True,'python':98,'mysql':94,'flask':99},
    'sailesh':{'status':False,'python':None,'mysql':None,'flask':None},
    'pavan':{'status':True,'python':20 ,'mysql':65,'flask':38},
    'sameer':{'status':True,'python':60,'mysql':65,'flask':68},
    'narayana':{'status':True,'python':80,'mysql':78,'flask':86},
}
    
name = input("Enter your name")
if name in data:
    if data[name]['satus']:
        sum = data[name]['python'] + data[name]['mysql'] + data[name]['fladk']
        avg = sum/3
        print(f"Hello {name}!")
        print(f"Your Average Score is {avg}")
        if avg >=90:
            print(f"Outstanding performance {name}")
        elif avg >= 80:
            print(f"Very Good {name}")
        elif avg >= 70:
            print(f"Good Hard Work {name}")
        elif avg >= 35:
            print(f"Better Luck next time {name}")
        else:
            print("You Failed exam")
    else:
        print(f"{name} did not attend the exam")
            
else:
    print("Not Found")