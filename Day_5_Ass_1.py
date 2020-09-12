sub_list = [1,1,5]

def find_match(listy):
    index1 = listy.index(1)
    index5 = listy[::-1].index(5)
    index5 = len(listy) - 1 - index5
    if 1 in listy[index1+1:index5]:
        return True
    return False

listy = [1,5,1,2,3,4,5,3,4]

print("it's a Match" if find_match(listy) else "it's Gone")