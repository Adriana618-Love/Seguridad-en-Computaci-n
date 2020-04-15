from datetime import datetime
import tkinter as tk 

###TIMER###
TIMES=[]
idxi=0
idxf=-1
###########

###FUNCTIONS AREA###
def SizeFiltro(Password):#Si es mayor igual a 8. True/False
    if(len(Password)<8):
        return False
    return True

def UserEquality(User, Password):#Si DH es menor a 1. True/False
    i=0
    count=0
    while(len(User)>i<len(Password)):
        if(User[i]!=Password[i]):
            count=count+1
        i+=1
    if(count<=1):
        return True
    return False

def UserInclude(User, Password):#Si User esta en Password. True/False
    if(User in Password):
        return True
    return False

def SomeUpper(Password):#Si hay alguna Mayúscula. True/False
    i=0
    for i in range(0,len(Password)):
        if('A'<=Password[i]<='Z'):
            return True
    return False

def SomeLower(Password):#Si hay alguna Minúscula. True/False
    i=0
    for i in range(0,len(Password)):
        if('a'<=Password[i]<='z'):
            return True
    return False

def onlyAlphaNum(Password):#Si es solo alfanumérico. True/False
    return Password.isalpha()

def Consecutive(Password):#Si hay alguna letra que se repita tres veces. True/False
    count=0
    for i in range(0,len(Password)-1):
        if(Password[i]==Password[i+1]):
            count+=1
        else:
            count=0
        if(count>=2):
            return True
    return False

def DateTime():#Si esta entre 8am y 10am. True/False
    now=datetime.now()
    if(now.hour>10 or now.hour<8):
        return False
    return True

def Check(User, Password):
    Messages=[]
    verify=True
    if(not SizeFiltro(Password)):
        Messages.append("El tamaño esta por debajo de 8")
        verify=False
    if(UserEquality(User, Password)):
        Messages.append("El usuario es el mismo que la contraseña")
        verify=False
    if(UserInclude(User,Password)):
        Messages.append("El usuario esta incluido en la contraseña")
        verify=False
    if(not SomeLower(Password)):
        Messages.append("No hay letras minúsculas")
        verify=False
    if(not SomeUpper(Password)):
        Messages.append("No hay letras mayúsculas")
        verify=False
    if(onlyAlphaNum(Password)):
        Messages.append("Faltan carácteres no alfanuméricos")
        verify=False
    if(Consecutive(Password)):
        Messages.append("Hay carácteres que se repiten 3 veces seguidas")
        verify=False
    if(not DateTime()):
        Messages.append("No esta en el horario indicado")
        verify=False
    if(not checkTime()):
        Messages.append("Bloqueado")
        verify=False
    if(verify):
        Messages.append("Todo en orden, contraseña aceptada")
    return verify,Messages
         
####################
#######CHECKTIME####
def checkTime():#Si hay tres intentos fallidos en menos de 60 segundos. False/True
    global idxf,idxi,TIMES
    while((TIMES[idxf]-TIMES[idxi]).total_seconds()>60.0):
        idxi+=1
    TIMES = TIMES[idxi:]
    if(len(TIMES)>=3):
        return False
    return True
####################

sin_pass=False

while(sin_pass):
    inputName=str(input("Usuario"))
    inputPass=str(input("Password"))
    TIME=datetime.now()
    TIMES.append(TIME)
    idxf+=1
    raw=Check(inputName,inputPass)
    validator=raw[0]
    messages=raw[1]
    if(validator):
        sin_pass=False
    for i in range(0,len(messages)):
        print(messages[i])
    
#########TKINTER##############
def Validar(User,Pass):
    global TIMES,idxf,idxi
    TIME=datetime.now()
    TIMES.append(TIME)
    idxf+=1
    raw=Check(User,Pass)
    validator=raw[0]
    messages=raw[1]
    label['text']=""
    for i in range(0,len(messages)):
        label['text']+=messages[i]+'\n'
    if(validator):
        outcome['bg']='green'
    else:
        outcome['bg']='red'

HEIGHT=700
WIDTH=800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background_image = tk.PhotoImage(file='landscape.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.14, relwidth=0.75, relheight=0.1, anchor='n')

frame2 = tk.Frame(root, bg='#80c1ff', bd=5)
frame2.place(relx=0.5, rely=0.04, relwidth=0.75, relheight=0.1,anchor='n')

entry = tk.Entry(frame,text="User", font=40)
entry.place(relwidth=0.65, relheight=1)

entry2 = tk.Entry(frame2,text="Password",font=40)
entry2.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Check", font=40, command=lambda: Validar(entry2.get(),entry.get()))
button.place(relx=0.85, relheight=1, relwidth=0.15)

user_label = tk.Label(frame2, text="<=User", font=40)
user_label.place(relx=0.68, relheight=1, relwidth=0.15)

pass_label = tk.Label(frame, text="<=Pass", font=40)
pass_label.place(relx=0.68, relheight=1, relwidth=0.15)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lower_frame,text="Aquí se mostrará el resultado de si tu constraseña es válida o no",anchor='nw',justify='left',font=16)
label.place(relwidth=1, relheight=1)

outcome_frame = tk.Frame(root, bg='#80c1ff', bd=10)
outcome_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')
outcome = tk.Label(outcome_frame,text="OUTCOME",justify='left')
outcome.place(relwidth=1, relheight=1)

root.mainloop()