import time
import random


print("Hello User")
while True:
    choice = input("Wanna Play a Quick Quiz (Yes / No) ?? \n").lower() 
    if (choice == 'yes'): # If want to play type yes else it will quit.
        print("Let's Start :")
        break
    elif(choice == 'no'):
        quit()
        break
    else:
        print("Invalid!")
        break


name = input("Your Name : ").title() # Taking user name (input)
print("Welcome ," , name)

# If answer is correct add value otherwise subtract in correct.
correct = 0

# If correct / len(question).
score = 0

print("Choose One of the Options below the Questions.")

# Writing Questions here and accesing them later through Loops.
# Multiple Dictionary inside a single dictionary. 
question = [
    {   'ques':"Q  : Which gas do plants take in for photosynthesis? ",
        'options':{'A':"Oxygen",'B':"Nitrogen",'C':"Helium",'D':"Carbon dioxide"},
        'ans':"D"
        },

    {   'ques':"Q : What is the name of the largest river by discharge volume in the world? ",
        'options':{'A':"Amazon",'B':"Nile",'C':"Chilika",'D': "Indus" },
        'ans':"A"
        },

    {   'ques':"Q : Which planet is closest to the Sun? ",
        'options':{'A':"Mercury",'B':"Mars",'C':"Pluto",'D':"Venus"},
        'ans':"A"
        },

    {   'ques':"Q : Who painted the Mona Lisa? ",
        'options':{'A':"Leonardo da Caprico",'B':"Leonardo da Vinci" , 'C':"Pablo Picasso", 'D':"Claude Monet" },
        'ans':"B"
        },
    
    {   'ques':"Q : What is the chemical symbol for water? ",
        'options':{'A':"Nacl",'B':"HCL",'C':"H2O",'D':"NO2"},
        'ans':"C"
        },

    {   'ques':"Q : Which is the fastest land animal? ",
        'options':{'A':"Panther",'B':"Wolf",'C':"Lion",'D':"Cheetah"},
        'ans':"D"
        },

    {   'ques':"Q : What is the boiling point of water in Celsius? ",
        'options':{'A':"300°C",'B':"100°C",'C':"101°C",'D':"256°C"},
        'ans':"B"
        },

    {   'ques':"Q : Who is known as the father of computers? ",
        'options':{'A':"Charles Babbage",'B':"Ada Lovelace",'C':"Alan Turing",'D':"Ray Tomlinson"},
        'ans':"A"
        },

    {
        'ques': "Q : Who developed the theory of relativity?",
        'options': {'A': "Isaac Newton", 'B': "Albert Einstein", 'C': "Galileo Galilei", 'D': "Nikola Tesla"},
        'ans': "B"
    },

    {   'ques': "Q : What is the capital city of Japan?",
        'options': {'A': "Beijing", 'B': "Seoul", 'C': "Tokyo", 'D': "Bangkok"},
        'ans': "C"
    },   

    {
        'ques': "Q : Which programming language is known as the 'mother of all languages'?",
        'options': {'A': "C", 'B': "Python", 'C': "Java", 'D': "Assembly"},
        'ans': "A"
    },

    {
        'ques': "Q : What is the hardest natural substance on Earth?",
        'options': {'A': "Gold", 'B': "Iron", 'C': "Diamond", 'D': "Platinum"},
        'ans': "C"
    },

    {
        'ques': "Q : When did World War II end?",
        'options': {'A': "1939", 'B': "1942", 'C': "1945", 'D': "1950"},
        'ans': "C"
    },
    {
        'ques': "Q : What is the capital of Australia?",
        'options': {'A': "Sydney", 'B': "Melbourne", 'C': "Perth", 'D': "Canberra"},
        'ans': "D"
    },
    {
        'ques': "Q : Who was the first man to step on the moon?",
        'options': {'A': "Buzz Aldrin", 'B': "Yuri Gagarin", 'C': "Neil Armstrong", 'D': "Michael Collins"},
        'ans': "C"
    },
    {
        'ques': "Q : What gas do humans need to survive?",
        'options': {'A': "Carbon Dioxide", 'B': "Oxygen", 'C': "Nitrogen", 'D': "Hydrogen"},
        'ans': "B"
    },
    {
        'ques': "Q : Which organ in the human body pumps blood?",
        'options': {'A': "Lungs", 'B': "Kidney", 'C': "Brain", 'D': "Heart"},
        'ans': "D"
    },
    {
        'ques': "Q : What is the hardest natural substance on Earth?",
        'options': {'A': "Gold", 'B': "Diamond", 'C': "Iron", 'D': "Granite"},
        'ans': "B"
    },
    {
        'ques': "Q : Which vitamin do we get from sunlight?",
        'options': {'A': "Vitamin A", 'B': "Vitamin B", 'C': "Vitamin C", 'D': "Vitamin D"},
        'ans': "D"
    },
    {
        'ques': "Q: What is the largest mammal in the world?",
        'options': {'A': "Elephant", 'B': "Blue Whale", 'C': "Giraffe", 'D': "Hippopotamus"},
        'ans': "B"
    },

    {
        'ques': "Q : Which company created the Windows operating system?",
        'options': {'A': "Apple", 'B': "Google", 'C': "Microsoft", 'D': "IBM"},
        'ans': "C"
    },
    {
        'ques': "Q : What does 'HTTP' stand for?",
        'options': {'A': "HyperText Transfer Protocol", 'B': "High Transmission Text Process", 'C': "Hyperlink Transfer Process", 'D': "Hyper Tool Text Protocol"},
        'ans': "A"
    },
    {
        'ques': "Q : Which programming language is mainly used for AI/ML today?",
        'options': {'A': "C", 'B': "Java", 'C': "Python", 'D': "PHP"},
        'ans': "C"
    }
]


  # Print Only keys and values like = A : option
for q in random.sample(question , 10):
    start = time.perf_counter()
    # 1st loop to accessing Dictionary multi-dictionary and printing ques.
    print('\n' , q["ques"])

    for keys, values in q["options"].items():
        # 2nd loop to print those options of the ques.
        print(keys,':',values)

    while True:
        # Infinite loop until you choose from below.
        u_ans = input("Enter Your Choice (A/B/C/D): ").upper()
        if(u_ans) in ['A','B','C','D']:
            if(u_ans == q['ans']):
                correct += 100
                print("Correct!!")
            else:
                # Here, Accessing option(like A..) then accessing answers value.
                print("Wrong! Correct Answer is ",q['ans']+' : '+q['options'][q['ans']])
                correct -= 50
            break
        else:
            print("Invalid Choice!, Please Enter A , B , C or D.")

end = time.perf_counter()
# Perf_counter will gave high precision
total_time = end - start

print("Total Time Taken: ",int(total_time)," Seconds")
score = correct
print("Score : ",score)