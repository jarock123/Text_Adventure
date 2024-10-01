import random

def stat_creation(your_class):
    if your_class == "warrior":
        strength = random.randint(3,9)
        intelligence = random.randint(1,6)
        dexterity = random.randint(2,7)
        constitution = random.randint(3,9)
        return str(strength) + str(intelligence) + str(dexterity) + str(constitution)
    if your_class == "wizard":
        strength = random.randint(1,6)
        intelligence = random.randint(3,9)
        dexterity = random.randint(1,6)
        constitution = random.randint(1,5)
        return str(strength) + str(intelligence) + str(dexterity) + str(constitution)    
    if your_class == "archer":
        strength = random.randint(1,5)
        intelligence = random.randint(1,6)
        dexterity = random.randint(3,9)
        constitution = random.randint(1,7)
        return str(strength) + str(intelligence) + str(dexterity) + str(constitution)    
    if your_class == "assassin":
        strength = random.randint(1,5)
        intelligence = random.randint(1,6)
        dexterity = random.randint(3,9)
        constitution = random.randint(3,8)
        return str(strength) + str(intelligence) + str(dexterity) + str(constitution)    
#loop for answer for text based answers
def answer_loop_text_name(answer,question):
    while True:
        try:
            answer = str(input(question))
        except ValueError:
            print("Sorry, I didn't understand.")
            continue
        else:
            return answer
            #break

def answer_loop_int_age(answer,question):
    while True:
        try:
            answer = int(input(question))
        except ValueError:
            print("Sorry, I didn't understand.")
            continue
        else:
            if answer < 18 or answer > 150:
                print("Sorry, you're not the right age to play.")
                continue
            else:
                return answer
                #break
def answer_loop_text_question(question,op1,op2,op3,op4):
    while True:
            getit = input(question)
            if getit == op1:
                return op1
            if getit == op2:
                return op2
            if getit == op3:
                return op3
            if getit == op4:
                return op4
            if getit != op1 or getit != op2 or getit != op3 or getit != op4:
                print("Not a valid response.")
                continue  
#name
name = answer_loop_text_name("text","What is your name?")
print(f"Ah, you must be {name[0].upper()}{name[1:].lower()}.")
name = name[0].upper() + name[1:].lower()
age = answer_loop_int_age(0,f"How old are you, {name}?")

#question = answer_loop_text_question("What is your intelligence? 2, 4, 6, or 8 ","2","4","6","8")
#print(f"Your intelligence is {question}.")



print(f"You are {age} years old.")
your_class = ""
while True:
    your_class = input("What is your class? \n Warrior \n Wizard \n Archer \n Assassin \n")
    if your_class.lower() == "warrior":
        print("You are a Warrior")
        break
    if your_class.lower() == "wizard":
        print("You are a Wizard")
        break
    if your_class.lower() == "archer":
        print("You are an Archer")
        break
    if your_class.lower() == "assassin":
        print("You are an Assassin")
        break
   
your_stats = stat_creation(your_class)
strength = your_stats[0]
intelligence = your_stats[1]
dexterity = your_stats[2]
constitution = your_stats[3]
print("Here are your stats: \n")
print(f"Strength: {strength}\nIntelligence: {intelligence}\nDexterity: {dexterity}\nConstituion: {constitution}\n")
print("Welcome to the Dungeon")


