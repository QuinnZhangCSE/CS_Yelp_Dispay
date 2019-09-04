#imports
import sys 

#classes
class Pokemon(object):
    def __init__(self, n, x, y, r, hp): #ititalize a pokemon with the nessary information
        self.name = n
        self.x = int(x)
        self.y = int(y)
        self.radius = int(r)
        self.hp = int(hp)
        
    def __str__(self): #prints out information about itself
        if self.hp <= 0:
            return "{:>12}: ({},{},{}) Health: {}".format(self.name,self.x,self.y,self.radius,0)
        return "{:>12}: ({},{},{}) Health: {}".format(self.name,self.x,self.y,self.radius,self.hp)
        
class Player(object):
    def __init__(self,n): #ititalize a player with a name and a list of pokemons caught
        self.name = n
        self.pokemons = []

#functions
def results(l): #prints out the result given a list of players
    l = sorted(l, key=lambda x: x.name) #sort the list given
    for p in l:
        if len(p.pokemons) > 0:
            print("{} caught {} pokemon".format(p.name,len(p.pokemons)))
            for pkm in p.pokemons:
                print("{:>12}".format(pkm))
        else:
            print("{} caught {} pokemon".format(p.name,0))

#main code
if __name__ == '__main__':
    #initializtions for the list of players and list of pokemons
    pkms = []
    plys = []
    
    #opens the file
    f_name = input("File name => ")
    print(f_name)
    file = open(f_name)
    
    #prints out the pokemons given
    num = int(file.readline()) 
    i = 0
    while i < num:
        p = file.readline().strip().split("|")
        pkms.append(Pokemon(p[0],int(p[1]),int(p[2]),int(p[3]),int(p[4])))
        i += 1
    for p in pkms:
        print(p)
    print()
    
    #reads all the actions
    for line in file:
        info = line.strip().split("|") #gets the x and y
        x = int(info[1])
        y = int(info[2])
        
        #appends all the players
        if len(plys) == 0:
            plys.append(Player(info[0]))
        else:
            c = False
            for p in plys:
                if p.name == info[0]:
                    c = True
            if c == False:
                plys.append(Player(info[0]))
                
        #lopps through the players list and the pokemons list to see if they collide
        for p in plys:
            if p.name == info[0]:
                hits = False #bolean for if ball hits pokemon
                for pkm in pkms:
                    if (x - pkm.x)**2 + (y - pkm.y)**2 < pkm.radius**2: #if the ball is a direct hit
                        print("{} throws a pokeball to position ({}, {}) hits {}:".format(p.name,x,y,pkm.name))
                        pkm.hp -= 2
                        print(pkm)
                        hits = True
                    elif (x - pkm.x)**2 + (y - pkm.y)**2 == pkm.radius**2: #if the ball hits the edge of pokemon
                        print("{} throws a pokeball to position ({}, {}) hits {}:".format(p.name,x,y,pkm.name))
                        pkm.hp -= 1
                        print(pkm)
                        hits = True
                    elif (pkm.radius-5)**2 <= (pkm.x-x)**2+(pkm.y-y)**2 <= (pkm.radius+5)**2: #if pokemon is within AOE of the ball
                        print("{} throws a pokeball to position ({}, {}) hits {}:".format(p.name,x,y,pkm.name))
                        pkm.hp -= 1
                        print(pkm)
                        hits = True
                    if pkm.hp <= 0: #if the pokeon is caught
                        p.pokemons.append(pkm.name)
                        pkms.remove(pkm)
                        print("{} is caught!".format(pkm.name))
                if hits == False: #if the ball misses
                    print("{} misses at ({}, {})".format(p.name,x,y))

        if len(pkms) == 0: #if all pokemons are caught
            print()
            print("All pokemon caught, results:")
            
            results(plys)
            sys.exit() #exits the code to prevent excuting the lines below
    
    #if all lines are read and pokemons still remain
    print()
    print("Players run out of pokeballs, results:")
    results(plys)
    sys.exit() #not necessary, but did it for consistency