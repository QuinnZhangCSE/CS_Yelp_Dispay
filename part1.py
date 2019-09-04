#imports
import json
import sys #this is the exit the code early if searched category is not found

#initializations
f = open("businesses.json")
category = input("Enter a category ==> ")
print(category)
cut = int(input("Cutoff for displaying categories => "))
print(cut)
cross = dict() #this dictionary will contain all(including the searched category) the categories that crosses with the searched category
contain = False 

#fills the dictionary
for line in f:
    business = json.loads(line)
    if category in business["categories"]:
        contain = True #if searched category is found
        for c in business["categories"]: #if there is a instance of the category in the dictionary
            if c in cross.keys():
                cross[c] += 1
            else:
                cross[c] = 1

#checks if the searched category is found
if contain == False:
    print("Searched category is not found")
    sys.exit()
    
cross.pop(category) #removes the searched category itself

#removes any category that does not cross the searched category enough times
to_be_removed = []
for c in cross.keys():
    if cross[c] < cut:
        to_be_removed.append(c)
for key in to_be_removed: #extra list needed because dictionary cannot be removed within the loop
    cross.pop(key)
    
#prints the result
print("Categories co-occurring with Shopping:")
if len(cross) == 0:
    print("None above the cutoff")
else:
    sorted_corss = sorted(cross.items(), key=lambda x: x[0])
    for c in sorted_corss:
        print("{}:{:2}".format(c[0].rjust(30),c[1]))