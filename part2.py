#imports
import json
import textwrap
import sys #this is the exit the code early if business is not found

#functions
#this function prints the adress of the business that is used
def using(name,adress):
    print("Using {} at:".format(name))
    print(adress)

#this function prints the reviews from the file reviews.json
def print_reviews(id_number):
    file = open("reviews.json")
    rating = []
    for line in file:
        business = json.loads(line)
        if id_number == business["business_id"]: 
            rating.append(business["text"]) #adds all the reviews to the rating list
    for i in range(len(rating)):
        print()
        print("Review: " + str(i+1))
        wrapper = textwrap.TextWrapper( initial_indent = ' '*4, subsequent_indent = ' '*4 )
        if "\n\n" in rating[i]: #if the review has mutiple paragraph
            rating[i] = rating[i].split("\n\n")
            for j in range(len(rating[i])):
                for l in wrapper.wrap(rating[i][j]):
                    print(l)
                print()
        else: #if the review has only one line
            for l in wrapper.wrap(rating[i]):
                print(l)
            print()

        
#main
#initializations
f = open("businesses.json")
b = input("Enter a business name => ")
print(b)
bs = dict()
exist = False

#add business id and adress to the dictionary
for line in f:
    business = json.loads(line)
    if b == business["name"]:
        exist = True
        bs[business["business_id"]] = business["full_address"]

#if no name is found in the file
if exist == False:
    print("This business is not found")
    sys.exit()
    
#if only one adress found
if len(bs) == 1:
    print()
    using(b,list(bs.values())[0])
    print_reviews(list(bs.keys())[0])
    
#if mutiple adress found
else:
    sorted_business = sorted(bs.items(), key=lambda x: x[0], reverse=True) #sorts the business by thier id
    print()
    
    print("Found {} at:".format(b)) #prints the options of business
    for i in range(len(bs.values())): 
        print()
        print(str(i+1)+".")
        print(sorted_business[i][1])
        
    #asks user for a input until a valid one is given
    print()
    choise = int(input("Select one from 1 - {} ==> ".format(len(bs))))
    print(choise)
    while choise not in list(range(1,len(bs)+1)):
        choise = int(input("Select one from 1 - {} ==> ".format(len(bs))))
        print(choise)
    choise -= 1
    
    print()
    using(b,sorted_business[choise][1])
    print_reviews(sorted_business[choise][0])