item1 = list(input("give me a word: "))
item2 = list(input("give me another word: "))
 
def combo(item1, item2):
    tups_list = []
    for index, item in enumerate(item2):           
        tups_list.append((item1[index], item))
    return tups_list
    
print(combo(item1, item2))
