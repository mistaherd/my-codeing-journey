import random
import collections
import sys
def prize(winlist):

    jackpot=19000000
    highercashprize=1000000
    lowercashprize=500000
    bonus=10000

def lotto(j,lottonumber,newuserlottolist):
    rndLotto=[]
    rndLottoPlus1=[]
    rndLottoPlus2=[]
    
 
    if j==1:
        rndLotto=random.sample(range(1,45),6)
        rndLottoPlus1 = random.sample(range(1,45),6)
        rndLottoPlus2 = random.sample(range(1,45),6)
        
    elif j==2:
       choose_lotto_combo=int(input("please enter what lotto combination you  want 1.lotto and lottoplus 1 2.lotto and lottoplus 2")) 
       if(choose_lotto_combo==1):
           rndLotto=random.sample(range(1,45),6)             
           rndLottoPlus1 = random.sample(range(1,45),6)
       elif(choose_lotto_combo==2):
           rndLotto=random.sample(range(1,45),6) 
           rndLottoPlus2 = random.sample(range(1,45),6)
    elif j==3:
        choose_lotto_type=int(input("please enter which lotto you want 1.for lotto,2.for lotto plus 1,3. for lotto plus 2"))
        if(choose_lotto_type==1):
            rndLotto=random.sample(range(1,45),6) 
        elif(choose_lotto_type==2):
            rndLottoPlus1 = random.sample(range(1,45),6)
        elif(choose_lotto_type==3):
            rndLottoPlus2 = random.sample(range(1,45),6)
            
    
    #compare lottonumber with each 
    compare_lottonumbers(j,rndLotto,rndLottoPlus1,rndLottoPlus2,lottonumber,newuserlottolist)
        #if j is 1 etc compare wit
def validateuserlottonumber(userlottonumbers):
    if int(userlottonumbers) in range(1,45):
        return True
    else:
        return False    
def compare_lottonumbers(j,rndLotto,rndLottoPlus1,rndLottoPlus2,lottonumber,newuserlottolist):
   amountofcombinations=0
 
def check_for_winnings(lottonumbers,newuserlottolist):
    #check each lotto lists against the user list
   
    print("choose what lotto u want ")
    lotto_type=int(input("enter 1 for all the lotto,2 choose lotto combination ie lotto , lottoplus1 , 3 pick one lotto system:")) 
    lotto(lotto_type,lottonumbers,newuserlottolist)  
def choice(userlottolist):
    newuserlottolist =[]
    pick=int(input("enter 1. for quick pick , 2. to  choose your own lotto numbers,3.exit program:"))
    if pick == 1:
        a=True
        while (a):
            userlottonumbers=random.sample(range(1,45),6)
            a_set =set(userlottonumbers)
            duplicate= len(userlottonumbers) != len(a_set)
            if (duplicate == True):
                a=True
                userlottonumbers.clear()
            else:
                a=False
    elif pick == 2:
        #vaildate each number typed in
        b=True
      
        while (b):
            for i in range(0,6):
                userlottonumbers=int(input("please enter in your lotto numbers" + str(i+1) + " between 1 and 45: "))
                while not validateuserlottonumber(userlottonumbers): 
                    userlottonumbers=int(input("please enter lotto number"+str(i+1)+" between 1 and 45:"))
                #put duplictae into for loop
                newuserlottolist.append(userlottonumbers)
                    
            a_set=set(newuserlottolist)
            duplicate= len(newuserlottolist) != len(a_set)
            if (duplicate == True):
                b=True
                userlottonumbers.clear()
            else:
                b=False
    elif pick ==3:
        sys.exit()
    else:
            print("invalid input",pick)
    if len(userlottonumbers)==1:
        userlottonumbers=[]
    if len(newuserlottolist)==1:
        newuserlottolist=[]
        
    check_for_winnings(userlottonumbers,newuserlottolist)
def main():
    theuserlottonumbers = []
    print("welcome to lotto ")
    choice(theuserlottonumbers)
while (True):
    main()