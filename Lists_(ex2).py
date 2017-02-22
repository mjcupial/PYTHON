# THE CHARACTER CREATOR PROGRAM ---
# The gamer should get pool of 30 points which can divided into 4 atributes:
# strength, health, wisdom and ability. The gamer should has possibilities to
# get back points assigned to another atribute and forwards it back to pool.
#
# by mj.c

atributes = []
print ("")
name = ("Strength","Health","Wisdom","Ability")
pool = 30
choice = ""
print ("\t\t The Character Creator 2.2.1\n")

while choice != "0":
    print ("\nYou've got",pool,"points to divide into 4 attributes:")
    print ("""
    0 - EXIT

    1 - Reset and hand points around
    2 - Strip points from attributes
    3 - Hand rest points around
    4 - Display attributes

    """)
    choice = input("Your choice: ")
    if choice == "0":
        print ("EXIT\n")
    elif choice == "1":
        pool=30
        atributes=[]
        name = ("Strength","Health","Wisdom","Ability")
        for i in name:
            print("*)", i,":")
            value = int(input())
            pool = pool - value
            print(pool)
            entry = [i, value]
            atributes.append(entry)


    elif choice == "2":
        for entry in atributes:
            name, value = entry
            print(name,"\t",value)
            subtrahend=int(input("How much points take?: "))
            pool += subtrahend
            entry[1]=value-subtrahend


    elif choice =="3":
        for entry in atributes:
            name, value = entry
            print("\n")
            print(name,": ",value," --- pool: ",pool)
            add=int(input("How much points add?: "))
            pool -= add
            entry[1]=value+add


    elif choice =="4":
        print("\n")
        for entry in atributes:
            i, value = entry
            print(i," - ",value)
        print("\n")

    else:
        print ("Please insert correct value")
input ("Press any kay to continue")
