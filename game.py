import random
import math
import os

length=35
width=120

os.system("mode con: cols=125 lines=40")

def path():
    #y=mx+c

    #initializing values
    u_power=-1
    ctr_p=1
    while u_power<0 or u_power>25:
        if ctr_p!=1:
            print 'Invalid choice.'
        ctr_p+=1
        u_power=input('Enter power: ')
    u_angle=-1
    ctr_a=1
    while u_angle<0 or u_angle>90:
        if ctr_a!=1:
            print 'Invalid choice.'
        ctr_a+=1
        u_angle=input('Enter angle: ')

    if u_angle>35 and u_angle<=69:
        u_angle-=21
        
    elif u_angle>69:
        u_angle-=(90-u_angle)
    else:
        u_angle-=(u_angle/2)

        
    rad=math.radians(u_angle)
    h_max=(((u_power)**2)*(math.sin(rad))**2)/1.5
    h_max=int(math.ceil(h_max))    
    if h_max>length:
        h_max=length
    slope=math.tan(rad)
    #---------------------------------

    #raw list-1 generator
    x,y=1,1
    i=True
    l1=[[[1],1]]
    l2=[]
    while i:
        x+=1
        y=math.ceil(x*slope)
        y=int(y)
        if y>h_max or y==h_max:
            y=h_max
            l1+=[[[x],y]]
            i=False
        else:
            l1+=[[[x],y]]
    #----------------------------------

    #modifier 1
    edited=[]
    new_l1=[]
    for j in range(len(l1)):
        y1=l1[j][1]
        check=y1
        k=j        
        temp=[]
        if j not in edited:
            while check==y1:
                temp+=[l1[k][0][0]]
                edited+=[k]
                if k!=len(l1)-1:
                    k+=1
                    check=l1[k][1]
                else:
                    break
            new_l1+=[[temp,y1]]
    l1=new_l1
    #-----------------------------------
    
    #modifier 2
    new_l1=[]
    prev=1
    x1=[1]
    for h in range(len(l1)):


        if l1[h][1]>prev:
            while prev!=l1[h][1]:
                new_l1+=[[x1,prev]]
                prev+=1
        prev+=1
        x1=l1[h][0]
        new_l1+=[[l1[h][0],l1[h][1]]]
    l1=new_l1
    #------------------------------------               

    #raw list-2 generator
    start=x+1
    i=True
    l2=[]
    x+=1
    while i and x<=width:
        y=math.ceil(h_max-(slope*(x-start)))
        y=int(y)
        if y<=1:
            y=1
            l2+=[[[x],y]]
            break
        l2+=[[[x],y]]    
        x+=1
    #------------------------------------

    #modifier 1
    edited=[]
    new_l2=[]
    for j in range(len(l2)):
        y1=l2[j][1]
        check=y1
        k=j
        temp=[]
        if j not in edited:
            while check==y1:
                temp+=[l2[k][0][0]]
                edited+=[k]
                if k!=len(l2)-1:
                    k+=1
                    check=l2[k][1]
                else:
                    break
            new_l2+=[[temp,y1]]
    l2=new_l2
    #----------------------------------

    #modifier 2
    new_l2=[]
    prev=h_max
    if l2:
        temp=l2[0][0]
    for i in range(len(l2)):
        if l2[i][1]<prev:
            while l2[i][1]!=prev:
                new_l2+=[[temp, prev]]
                prev-=1
        new_l2+=[[l2[i][0],l2[i][1]]]
        temp=l2[i][0]
        prev-=1
    l2=new_l2 
    #----------------------------------            

    return l1,l2,u_power, u_angle


class game:

    def __init__(self):
        self.i=0
    def chances(self,i):
        i=str(i)
        num=len(i)
        self.line1=(num+2)*'='
        self.line2='|'+str(i)+'|'
        self.line3=(num+2)*'='
     

    def assembler(self,l1,l2,u_power,u_angle):
        #basic initialization
        
        no=0
        line=length
        flag=0
        decider=0
        #---------------------------------------
        #a crash
        
        for i in l1:
            if i[1]<o_height:
                if o_dist in i[0]:
                    flag=1

        if flag==1:
            new_l1=[]
            for i in l1:
                new_l1+=[i]
                if o_dist in i[0]:
                    new_l=[]
                    for j in i[0]:
                        if j<o_dist:
                            new_l+=[j]
                    l=new_l
                    new_l1+=[[l,i[1]]]
                    break
            l1=new_l1
            l2=[]
        #----------------------------------------
        #for chances
        
        #main loop
        print width*'_'
        while line>0 and flag!='win':
            #basic initialization
            #for game:
            a,b,c,d=[],[],0,[]
            a_nxt,b_bck=[],[]

            #-------------------------------------
            #initializing a and a_nxt
            
            for i in range(len(l1)):
                if line==l1[i][1]:
                    a=l1[i][0]
                    if i<len(l1)-1:
                        a_nxt=l1[i+1][0]
            #--------------------------------------
            #initializing b and b_bck
            
            for i in range(len(l2)):
                if line==l2[i][1]:
                    b=l2[i][0]
                    if i>0:
                        b_bck=l2[i-1][0]
            #---------------------------------------
            #initializing c

            if line<o_height:
                c=o_dist
            #---------------------------------------
            #initializing d

            if line<height+7 and line>height:
                d=[dist-5,dist-4,dist-3,dist-2,dist-1,dist]
            #---------------------------------------
            #b crash
                
            if c in b:
                new_b=[]
                
                for i in b:
                    if i<c:
                        new_b+=[i]
                        break
                b=new_b
                flag=2
            if flag==2:
                b=[]
            #---------------------------------------
            #d crash
                
            for i in a:
                if i in d:
                    flag=3
            if flag==3:
                
                for i in a:
                    if i in d:
                        no+=1
                    else:
                        continue

            for i in b:
                if i in d:
                    flag=4
            if flag==4:
                
                for i in b:
                    if i in d:
                        no+=1
                    else:
                        continue
            #----------------------------------------
            #line maker
                    
            pos=1
            maker=''
            while pos<width:
                if pos in a:

                    if pos in a_nxt:
                        maker+='|'
                    else:
                        maker+='/'

                elif pos in b:

                    if pos in b_bck:
                        maker+='|'
                    else:
                        maker+='\\'

                elif pos==c:
                    maker+='|'

                elif pos in d:
                    maker+='+'
    
                else:
                    maker+=' '
                pos+=1
            print maker+'|'
            
            #-----------------------------------------
            #decides whether to continue or not
            if flag==3 or flag==4:
                play=False
            else:
                play=True
            line-=1
        print width*'-'
        return play, no
        print no

def chances(turn,ch1,ch2,ch3):    
    print '\nChances used: '
    obj.chances(turn)
    ch1+=obj.line1
    ch2+=obj.line2
    ch3+=obj.line3

    print ch1
    print ch2
    print ch3
    return ch1, ch2, ch3

#main
print 'Welcome!\n\n'
print 'INSTRUCTIONS \n1)You have to hit the target marked in \'+\' with your arrow'
print '2)Your arrow starts from the bottom left of the screen and has a power and angle'
print '3)The power ranges from 0-50 and angle from 0-90'
print '4)Make sure to avoid the wall in between as the arrow cannot pass through the wall'
print '5)Hit the target in the least possible chances and hit a larger chunk of the target to score higher!'
print '6)Each game has 5 rounds, each with one target to break'
raw_input('\nPress enter to continue: ')
score=0
total=1
while total<6:
    print 'Target', total

    dist=random.randint(3*width/5,4*width/5)
    height=random.randint(length/2,4*length/5)
    o_dist=random.randint(2*width/5,width/2)
    o_height=random.randint(2*length/5,3*length/5)

    turn=0
    counter=0
    ch1=''
    ch2=''
    ch3=''
    play=True
    obj=game()
    l1,l2=[],[]
    u_power,u_angle=0,0

    while play:
        counter+=1
        if counter%2==1:
            if turn!=0:
                ch1,ch2,ch3=chances(turn,ch1,ch2,ch3)
                raw_input('Press enter to continue: ')
            l1,l2=[],[]
            u_power,u_angle=0,0
            play,no=obj.assembler(l1,l2,u_power, u_angle)
        else:
            turn+=1
            l1,l2,u_power,u_angle=path()
            play,no=obj.assembler(l1,l2,u_power, u_angle)
            raw_input('Press enter to continue:')
        if play!=True:
            print 'Congrats!!\nYou hit the target in', turn,'moves!'
            score_rd=(100*no -(turn*50))
            score+=(100*no -(turn*50))
            print '\nYour score for this round is:',score_rd
            raw_input('Press enter to continue.')

    total+=1
print width*'-', '\nCongrats! You finished the game!'
print 'Your total score is', score
raw_input('Press enter to exit.')
