def is_permutations(a_list):
    for a in a_list:
        if not permutable(list(str(a_list[0])), str(a)):
            return False
    return True
        

def permutable(checklist, num):
    for digit in num:
        try:
            checklist.pop(checklist.index(digit))
        except:
            return False
    return True


def mult(n, m):
    return [n*(x+1) for x in range(m)] 

i = 3
m = 6

while not is_permutations(mult(i, m)):
    i+=1
    
print mult(i, m)