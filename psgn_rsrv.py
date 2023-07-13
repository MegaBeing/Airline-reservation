import os
import admin
import random

psgn_tkt=[]
def find_files(filename, search_path):
# Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            return filename
        else:
            return 'not found'
d = None
x=0
while d!='not found':
    fl_file=f"My_ticket_{x}.txt"
    d = find_files(fl_file,os.getcwd())
    if d==fl_file:
        psgn_tkt.append(d)
        x+=1
    elif d=='not found':
        break

def finds_files(filename, search_path):
# Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            return filename
        else:
            return 'not found'
a = finds_files('flight_type.txt',os.getcwd())
if a == 'not found':
    file = open('flight_type.txt','w')
    file.close()

def key_generator():
    a=chr(random.randint(65,90))
    b=chr(random.randint(65,90))
    key=f'P{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{a}{b}'
    return key

def seat_generator(flight):
    file = open(flight, 'r')
    m = file.readlines()

    for y in range(1,31):
        for z in range(65,71):
            Seat=f'{y}{chr(z)}'
            count=0
            for i in m:
                if Seat==i:
                    count+=1
                    break
                else:
                    continue
        if count==0:
            return Seat
            break

def Booking(nm,age,gd,flkey):
    global psgn_tkt,x
    key = key_generator()
    for i in range(len(admin.flight_files)):
        file=open(f'flight_{i}.txt','r')
        m=file.readlines()
        fi=str()
        d=False
        for y in m:
            y=y.rstrip('\n')
            if flkey==y:
                d=True
                fi=f'flight_{i}.txt'
                break
        if d is True:
            file.close()
            break
    u=open(fi,'a')
    u.write(f'{key}\n')
    u.write(f'{nm}\n')
    seat=seat_generator(fi)
    u.write(f'{seat}\n')
    u.write(f'{age}\n')
    u.write(f'{gd}\n')
    u.write(f'{0}\n')
    u.close()
    u=open(fi,'r')
    z=u.readlines()
    z[9]=int(z[9].strip('\n'))
    z[9]-=1
    z[9]= str(z[9])+'\n'
    z[10] = int(z[10].strip('\n'))
    z[10] += 1
    z[10] = str(z[10])+'\n'
    u.close()
    u=open(fi,'w')
    for m in z:
        u.write(m)
    u.close()
    f = open(f"My_ticket_{x}.txt", 'w+')
    psgn_tkt.append(f"My_ticket_{x}.txt")
    x += 1
    f.write(f'{key}\n')
    f.write(f'{nm}\n')
    f.write(f'{age}\n')
    f.write(f'{gd}\n')
    f.write(f'{z[1]}')
    f.write(f'{z[2]}')
    f.write(f'{z[3]}')
    f.write(f'{z[4]}')
    f.write(f'{z[5]}')
    f.write(f'{z[6]}')
    f.write(f'{z[7]}')
    f.write(f'{z[8]}')
    f.close()
    u.close()
    return key

def ticket_print():
    global psgn_tkt,x
    g=[]
    for y in range(len(psgn_tkt)):
        p = []
        f=open(psgn_tkt[y],'r')
        u=f.readlines()
        m=False

        p.append(f'{u[0]}\n')
        p.append(f'{u[1]}\n')
        p.append(f'{u[2]}\n')
        p.append(f'{u[3]}\n')
        p.append(f'{u[4]}\n')
        p.append(f'{u[5]}\n')
        p.append(f'{u[6]}\n')
        p.append(f'{u[7]}\n')
        p.append(f'{u[8]}\n')
        p.append(f'{u[9]}\n')
        p.append(f'{u[10]}\n')
        p.append(f'{u[11]}\n')

        g.append(p)
    return g

def via_ev(date,dpc,dsc):
    p=[]
    for x in range(len(admin.flight_files)):
        f=open(admin.flight_files[x],'r')
        u=f.readlines()
        if date==u[7].strip('\n') and dpc==u[2].strip('\n') and dsc==u[4].strip('\n'):
            p.append(admin.flight_files[x])
    if len(p)>0:
        return p
    else:
        return False


