

def match_ends(words):
    count = 0    
    for i in words:
        if len(i) >=2 and i[0] == i[-1]:
            count +=1
        else:
            count +=0
    return count


####second exos#####
def front_x(words):
    list=[]
    xlist=[]
    for i in words:
        if i[0] == 'x':
            xlist.append(i)
        else: 
            list.append(i)
    return sorted(xlist) + sorted(list)
    
front_x(["aa","bb","xa","xb"])

#####Third exo#############
def sort_last(tuples):
    def last(x):
        return x[-1]
    return sorted(tuples, key=last)
    


#The forth one
def remove_adjacent(nums):
    return list(set(nums))
  
#The last one
def linear_merge(list1,list2):
    return sorted(list(set(list1+list2)))
    
    
    
    
def donuts(count):
    if count > 9:
        print('Number of donuts: many')
    else:
        print('Number of donuts:',count)
        
def both_ends(s):
    if len(s) <4:
        return []
    else:
        return s[:2]+s[-2:]

def fix_start(s):
    return s[0] + s[1:].replace(s[0],'*')
    

def mix_up(a,b):
    return b[0] + a[1:] + ' ' + a[0] + b[1:]


def verbing(s):
    if len(s) > 2:
        if s[-3:] == 'ing':
            return s+'ly'
        else:
            return s+'ing'
    else:
        return s

def not_bad(s):
    l=0
    m=0
    for i in range(0,len(s)-2):
        if s[i:i+3] == "not":
            l=i
        if s[i:i+3] == "bad":
            m=i
    if m > l:
        return s.replace('bad','good').replace('not ','')
    else:
        return s


def front_back(a,b):
   def devi(c):
        front = c[0:round(len(c)/2+0.49)]
        back = c[round(len(c)/2+0.49):]
        return([front,back])
   return devi(a)[0] + devi(b)[0] + devi(a)[1] + devi(b)[1]

