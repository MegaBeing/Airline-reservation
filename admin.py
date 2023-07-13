import os

flight_files=[]                         #To handle file names in the program

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


def find_files(filename, search_path):
# Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            return filename
        else:
            return 'not found'
d = None
x=0
fl_file=f'flight_{x}.txt'
while d!='not found':
    fl_file="flight_{}.txt".format(x)
    d = find_files(fl_file,os.getcwd())
    if d==fl_file:
        flight_files.append(d)
        x+=1
    elif d=='not found':
        break

def Check_flight_avgs(arkey):

    file = open('flight_type.txt', 'r')
    ud = file.readlines()
    f = True

    for x in range(len(ud)):
        ud[x].rstrip('\n')
        if ud[x] == arkey:
            f = ud[x+6]
            break
    file.close()
    return f


def check_flight_type(arkey):
    file = open('flight_type.txt','r')
    ud = file.readlines()
    f = int()

    for x in ud:
        x=x.rstrip('\n')
        if x == arkey:
            f = 1
            break
        else:
            f = 0
    file.close()
    return f

def flight_type(model, np, avgs, mavgs, fc, ft, arkey,tksp):
    """model = you know what it is
        np = No of Passengers
        avgs = Cruising speed
        fc = fuel capacity
        arkey = airplane key
        tksp = take off speed
        mavgs = Maximum Cruising speed"""
    f=open('flight_type.txt','a')
    f.write(arkey+'\n')
    f.write(model+'\n')
    f.write(np+'\n')
    f.write(tksp + '\n')
    f.write(fc+'\n')
    f.write(ft + '\n')
    f.write(avgs+'\n')
    f.write(mavgs)
    f.write('\n')
    f.close()



def new(arkey,flkey, fm, fm_time, to, td ,Date,avgs,np):
    """fm = departure place ;
    to = destination place ;
    fm_time = take of time ;
    td = total distance;
    Date = you know what it is;"""
    global fl_file
    global x
    global flight_files

    f = open (fl_file , "w+")
    flight_files.append (fl_file)
    x+=1
    fl_file = "flight_ "+ str(x)  +".txt"

    tim = int(td) / int(avgs)                 # tim = tim taken by the flight
    ab = abs(tim)               # ab = absolute value (just for calculations)
    hrs = ab
    ti = (tim - ab) * 100
    m = round(ti * 0.6, 0)
    minutes = m
    org_time = fm_time.split(':')
    hr, mun = (int(k) for k in org_time)                #adding time for eta of arrival at the destination
    ab+=hr
    m+=mun
    if m>=60:
        m-=60
        ab+=1

    f.write(arkey+'\n')
    f.write(flkey+'\n')
    f.write(fm + '\n')
    f.write(str(fm_time) + '\n')
    f.write(to + '\n')
    f.write(str(int(round(ab,0))) + ':' + str(int(round(m,0))) + '\n')
    f.write(str(td) + '\n')
    f.write(Date + '\n')
    f.write(str(int(round(hrs,0))) +":" + str(int(round(minutes,0))) + '\n')
    f.write(str(np) + '\n')
    f.write('0\n')
    f.write('------------------------------------------------\n')
    f.write('------------------------------------------------\n')
    f.close()
    return True

def old(arkey,flkey, fm, fm_time, to, td ,Date,avgs,np):
    global fl_file
    global x
    global flight_files
    file = open('flight_type.txt','r')
    man = file.readlines()
    for y in range(len(man)):
        if arkey == man[y].strip('\n'):
            u = open(fl_file,'w+')
            flight_files.append(fl_file)
            x+=1
            tim = int(td) / int(avgs)  # tim = tim taken by the flight
            ab = abs(tim)  # ab = absolute value (just for calculations)
            hrs = ab
            ti = (tim - ab) * 100
            m = round(ti * 0.6, 0)
            minutes = m
            org_time = fm_time.split(':')
            hr, mun = (int(k) for k in org_time)  # adding time for eta of arrival at the destination
            ab += hr
            m += mun
            fl_file = 'flight_' + str(x) +'.txt'
            u.write(man[x] + '\n')
            u.write(fm + '\n')
            u.write(str(fm_time) + '\n')
            u.write(to + '\n')
            u.write(str(ab) + ' : ' + str(m) + '\n')
            u.write(str(np) + '\n')
            u.write(str(td) + '\n')
            u.write(str(hrs) + " " + str(minutes) + '\n')
            u.write(str(np) + '\n')
            u.write('0\n')
            u.write('------------------------------------------------\n')
            u.write('------------------------------------------------\n')
            u.close()
            fi = True
            return fi
            break
        else:
            fi = False
    if fi == False:
        return fi


def via_key(b,c,d='nothing',e='nothing'):             # b=key, c=True/False(for psgn_lst), d=key or all ,e = person key
    global fl_file
    global x
    global flight_files
    g = []
    for i in flight_files:
        p = []
        f = open(i, 'r')
        nl = f.readlines()
        for j in range(len(nl)):
            if nl[j].strip('\n') == b:
                p.append(nl[0].strip('\n'))                  # do you want the psgn list or not
                p.append(nl[1].strip('\n'))
                p.append(nl[2].strip('\n'))
                p.append(nl[3].strip('\n'))
                p.append(nl[4].strip('\n'))
                p.append(nl[5].strip('\n'))
                p.append(nl[6].strip('\n'))
                p.append(nl[7].strip('\n'))
                p.append(nl[8].strip('\n'))
                p.append(nl[9].strip('\n'))
                p.append(nl[10].strip('\n'))
                p.append(nl[11].strip('\n'))
                p.append(nl[12].strip('\n'))
                if c is True:
                    if d =='key':
                        f.seek(0,0)
                        for z in range(len(nl)):
                            if z == e:                          #searching via key
                                p.append('Key:',nl[z].strip('\n'))
                                p.append('Name:',nl[z+1].strip('\n'))
                                p.append('Seat No:',nl[z+2].strip('\n'))
                                p.append('Age:',nl[z+3].strip('\n'))
                                p.append('Gender:',nl[z+4].strip('\n'))
                                p.append('Status:',nl[z+5].strip('\n'))
                                p.append('--------------------------------'.strip('\n'))
                                p.append('--------------------------------'.strip('\n'))
                                f.close()
                                break
                        g.append(p)
                    elif d == 'all':
                        f.seek(0,0)
                        for z in range(14,len(nl),6):
                            p.append('Key:', nl[z].strip('\n'))
                            p.append('Name:', nl[z + 1].strip('\n'))
                            p.append('Seat No:', nl[z + 2].strip('\n'))
                            p.append('Age:', nl[z + 3].strip('\n'))
                            p.append('Gender:', nl[z + 4].strip('\n'))
                            p.append('Status:', nl[z + 5].strip('\n'))
                            p.append('--------------------------------'.strip('\n'))
                            p.append('--------------------------------'.strip('\n'))
                        f.close()
                        g.append(p)
                else:
                    g.append(p)
    if len(p) > 0:
        if len(p) > 13:
            g.append(True)
            return g
        else:
            g.append(False)
            return g
    elif len(p) == 0:
        return False

def via_dec(b1,b2,c,d='nothing',e='nothing'):
    global fl_file
    global x
    global flight_files

    g=[]
    for i in flight_files:
        p=[]
        f = open(i,'r')
        nl = f.readlines()
        for j in range(len(nl)):
            if nl[j].strip('\n')==b1 and nl[j + 3 ].strip('\n') == b2:
                count+=1
                  # nl = extract lines to split
                p.append(nl[0].strip('\n'))  # do you want the psgn list or not
                p.append(nl[1].strip('\n'))
                p.append(nl[2].strip('\n'))
                p.append(nl[3].strip('\n'))
                p.append(nl[4].strip('\n'))
                p.append(nl[5].strip('\n'))
                p.append(nl[6].strip('\n'))
                p.append(nl[7].strip('\n'))
                p.append(nl[8].strip('\n'))
                p.append(nl[9].strip('\n'))
                p.append(nl[10].strip('\n'))
                p.append(nl[11].strip('\n'))
                p.append(nl[12].strip('\n'))
                if c is True:
                    if d == 'key':

                        f.seek(0, 0)
                        for z in range(len(nl)):
                            if z == e:  # searching via key
                                p.append('Key:', nl[z].strip('\n'))
                                p.append('Name:', nl[z + 1].strip('\n'))
                                p.append('Seat No:', nl[z + 2].strip('\n'))
                                p.append('Age:', nl[z + 3].strip('\n'))
                                p.append('Gender:', nl[z + 4].strip('\n'))
                                p.append('Status:', nl[z + 5].strip('\n'))
                                p.append('--------------------------------'.strip('\n'))
                                p.append('--------------------------------'.strip('\n'))

                        g.append(p)
                        f.close()



                    elif d == 'all':
                        for z in range(10, len(nl), 6):
                            p.append('Key:', nl[z].strip('\n'))
                            p.append('Name:', nl[z + 1].strip('\n'))
                            p.append('Seat No:', nl[z + 2].strip('\n'))
                            p.append('Age:', nl[z + 3].strip('\n'))
                            p.append('Gender:', nl[z + 4].strip('\n'))
                            p.append('Status:', nl[z + 5].strip('\n'))
                            p.append('--------------------------------'.strip('\n'))
                            p.append('--------------------------------'.strip('\n'))
                        g.append(p)
                        f.close()
                else:
                    g.append(p)
    if len(p) > 0:
        if len(p) > 13:

            g.append(True)
            return g
        else:

            g.append(False)
            return g
    elif len(p) == 0:
        return False

def via_dpc(b1,b2,c,d='nothing',e='nothing'):
    global fl_file
    global x
    global flight_files

    g = []
    for i in flight_files:
        p=[]
        f = open(i, 'r')
        nl = f.readlines()
        for j in range(len(nl)):
            if nl[j].strip('\n') == b1 and nl[j + 5].strip('\n') == b2:
                count += 1
                # nl = extract lines to split
                p.append(nl[0].strip('\n'))  # do you want the psgn list or not
                p.append(nl[1].strip('\n'))
                p.append(nl[2].strip('\n'))
                p.append(nl[3].strip('\n'))
                p.append(nl[4].strip('\n'))
                p.append(nl[5].strip('\n'))
                p.append(nl[6].strip('\n'))
                p.append(nl[7].strip('\n'))
                p.append(nl[8].strip('\n'))
                p.append(nl[9].strip('\n'))
                p.append(nl[10].strip('\n'))
                p.append(nl[11].strip('\n'))
                p.append(nl[12].strip('\n'))
                if c is True:
                    if d == 'key':

                        f.seek(0, 0)
                        for z in range(len(nl)):
                            if z == e:  # searching via key
                                p.append('Key:', nl[z].strip('\n'))
                                p.append('Name:', nl[z + 1].strip('\n'))
                                p.append('Seat No:', nl[z + 2].strip('\n'))
                                p.append('Age:', nl[z + 3].strip('\n'))
                                p.append('Gender:', nl[z + 4].strip('\n'))
                                p.append('Status:', nl[z + 5].strip('\n'))
                                p.append('--------------------------------'.strip('\n'))
                                p.append('--------------------------------'.strip('\n'))
                        f.close()
                        g.append(p)


                    elif d == 'all':
                        for z in range(10, len(nl), 6):
                            p.append('Key:', nl[z].strip('\n'))
                            p.append('Name:', nl[z + 1].strip('\n'))
                            p.append('Seat No:', nl[z + 2].strip('\n'))
                            p.append('Age:', nl[z + 3].strip('\n'))
                            p.append('Gender:', nl[z + 4].strip('\n'))
                            p.append('Status:', nl[z + 5].strip('\n'))
                            p.append('--------------------------------'.strip('\n'))
                            p.append('--------------------------------'.strip('\n'))
                        f.close()
                        g.append(p)
                else:
                    g.append(p)
    g = []
    if len(p) > 0:
        if len(p) > 13:
            g.append(True)
            return g
        else:

            g.append(False)
            return g
    elif len(p) == 0:
        return False

def via_time(b1,b2,c,d='nothing',e='nothing'):
    global fl_file
    global x
    global flight_files

    g = []
    for i in flight_files:
        p=[]
        f = open(i, 'r')
        nl = f.readlines()
        for j in range(len(nl)):
            if nl[j].strip('\n') == b1 and nl[j + 4].strip('\n') == b2:
                count += 1
                # nl = extract lines to split
                p.append(nl[0].strip('\n'))  # do you want the psgn list or not
                p.append(nl[1].strip('\n'))
                p.append(nl[2].strip('\n'))
                p.append(nl[3].strip('\n'))
                p.append(nl[4].strip('\n'))
                p.append(nl[5].strip('\n'))
                p.append(nl[6].strip('\n'))
                p.append(nl[7].strip('\n'))
                p.append(nl[8].strip('\n'))
                p.append(nl[9].strip('\n'))
                p.append(nl[10].strip('\n'))
                p.append(nl[11].strip('\n'))
                p.append(nl[12].strip('\n'))
                if c is True:
                    if d == 'key':

                        f.seek(0, 0)
                        for z in range(len(nl)):
                            if z == e:  # searching via key
                                p.append('Key:', nl[z].strip('\n'))
                                p.append('Name:', nl[z + 1].strip('\n'))
                                p.append('Seat No:', nl[z + 2].strip('\n'))
                                p.append('Age:', nl[z + 3].strip('\n'))
                                p.append('Gender:', nl[z + 4].strip('\n'))
                                p.append('Status:', nl[z + 5].strip('\n'))
                                p.append('--------------------------------'.strip('\n'))
                                p.append('--------------------------------'.strip('\n'))

                        f.close()
                        g.append(p)



                    elif d == 'all':
                        for z in range(10, len(nl), 6):
                            p.append('Key:', nl[z].strip('\n'))
                            p.append('Name:', nl[z + 1].strip('\n'))
                            p.append('Seat No:', nl[z + 2].strip('\n'))
                            p.append('Age:', nl[z + 3].strip('\n'))
                            p.append('Gender:', nl[z + 4].strip('\n'))
                            p.append('Status:', nl[z + 5].strip('\n'))
                            p.append('--------------------------------'.strip('\n'))
                            p.append('--------------------------------'.strip('\n'))
                        f.close()
                        g.append(p)
                else:
                    g.append(p)

    if len(g) > 0:
        if len(g) > 13:

            g.append(True)
            return g
        else:

            g.append(False)
            return(g)
    elif len(p) == 0:
        return False
