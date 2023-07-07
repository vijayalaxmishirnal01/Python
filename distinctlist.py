l1=[1,2,3,4,5]
def checkdistinctlist(l1):
    if(len(l1)==len(set(l1))):
        return True
    else:
        return False