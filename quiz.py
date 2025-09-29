import time
import random

print("HELLO USER")
while True: 
    ask = input("Wanna Play a Quiz (Yes / No) ?? \n").title()
    if(ask == 'Yes'):
        break
    elif(ask == 'No'):
        quit()
    else:
        print("Invalid Option , Try Again!!")

name = input("Your Name : ").title() # Taking user name (input)
print("Welcome ," , name)

# Score is used to show the points user gets for each correct and wrong answers.
score = 0

# Writing Questions here and accesing them later through Loops.
# Multiple Dictionary inside a single dictionary. 
question = {
    'easy':{
        'General':[
        # {
        #     'ques':"",
        #     'options':{'A':"",'B':"",'C':"",'D':""},
        #     'ans':""
        # },
        # ------------- General Knowledge ------------
            {
                'ques':"Q : What is the capital of India?",
                'options':{'A':"Mumbai",'B':"Delhi",'C':"Kolkata",'D':"Chennai"},
                'ans':"B"
            },

            {
                'ques':"Q : Who is called the Father of the Nation in India?",
                'options':{'A':"Bhagat Singh",'B':"Mahatma Gandhi",'C':"Jawaharlal Nehru",'D':"Subhash Chandra Bose"},
                'ans':"B"
            },

            {
                'ques':"Q : How many continents are there on Earth?",
                'options':{'A':"5",'B':"6",'C':"7",'D':"8"},
                'ans':"C"
            },

            {
                'ques':"Q : Which is the largest ocean on Earth?",
                'options':{'A':"Atlantic Ocean",'B':"Indian Ocean",'C':"Pacific Ocean",'D':"Arctic Ocean"},
                'ans':"C"
            },

            {
                'ques':"Q : Who was the first President of the USA?",
                'options':{'A':"George Washington",'B':"Abraham Lincoln",'C':"John Adams",'D':"Thomas Jefferson"},
                'ans':"A"
            },

            {
                'ques':"Q : What is the most common surname in the United States?",
                'options':{'A':"Johnson",'B':"Williams",'C':"Smith",'D':"Brown"},
                'ans':"C"
            },

            {
                'ques':"Q : What is the largest planet in our solar system?",
                'options':{'A':"Mars",'B':"Earth",'C':"Jupiter",'D':"Saturn"},
                'ans':"C"
            }

        ],

        'Science':[
    # ------------ Science ------------
            {
                'ques':"Q : Which planet is closest to the Sun?",
                'options':{'A':"Venus",'B':"Mercury",'C':"Mars",'D':"Earth"},
                'ans':"B"
            },

            {
                'ques':"Q : Humans breathe in which gas?",
                'options':{'A':"Oxygen",'B':"Carbon dioxide",'C':"Nitrogen",'D':"Helium"},
                'ans':"A"
            },

            {
                'ques':"Q : Water freezes at what temperature (Celsius)?",
                'options':{'A':"0",'B':"32",'C':"100",'D':"-1"},
                'ans':"A"
            },
            {

                'ques':"Q : What is the center of an atom called?",
                'options':{'A':"Proton",'B':"Nucleus",'C':"Electron",'D':"Neutron"},
                'ans':"B"
            },
            
            {
                'ques':"Q : What force keeps us on the ground?",
                'options':{'A':"Friction",'B':"Magnetism",'C':"Gravity",'D':"Pressure"},
                'ans':"C"
            },

            {
                'ques':"Q : What is the process by which plants convert sunlight to energy?",
                'options':{'A':"Respiration",'B':"Fermentation",'C':"Photosynthesis",'D':"Metabolism"},
                'ans':"C"
            },
            {
                'ques':"Q : What is the smallest unit of matter?",
                'options':{'A':"Molecule",'B':"Cell",'C': "Atom",'D':"Proton"},
                'ans':"C"
            }
        ],
        
        'Maths':[
    # ------------ Maths------------
            {
                'ques':"Q : What is 10 + 15?",
                'options':{'A':"20",'B':"25",'C':"30",'D':"35"},
                'ans':"B"
            },

            {
                'ques':"Q : What is 9 x 6?",
                'options':{'A':"45",'B':"52",'C':"54",'D':"64"},
                'ans':"C"
            },

            {
                'ques':"Q : What is half of 100?",
                'options':{'A':"20",'B':"25",'C':"40",'D':"50"},
                'ans':"D"
            },

            {
                'ques':"Q : The square root of 49 is?",
                'options':{'A':"6",'B':"7",'C':"8",'D':"9"},
                'ans':"B"
            },

            {
                'ques':"Q : How many sides does a hexagon have?",
                'options':{'A':"5",'B':"6",'C':"7",'D':"8"},
                'ans':"B"
            },

            {
                'ques':"Q : If x = 7, what is the value of 3x + 2?",
                'options':{'A': "21",'B':"22",'C':"23",'D':"24"},
                'ans':"C"
            },

            {
                'ques':"Q : What is the value of (15 x 4) ÷ 10?",
                'options':{'A':"5",'B':"6",'C':"7",'D':"8"},
                'ans':"B"
            }
        ]
    },

    'medium':{
        'General':[
            # ------------- General Knowledge ------------
            {
                'ques':"Q : Which country gifted the Statue of Liberty to the USA?",
                'options':{'A':"Germany",'B':"France",'C':"Italy",'D':"Spain"},
                'ans':"B"
            },

            {
                'ques':"Q : Who discovered sea route to India in 1498?",
                'options':{'A':"Christopher Columbus",'B':"Vasco da Gama",'C':"Ferdinand Magellan",'D':"Marco Polo"},
                'ans':"B"
            },

            {
                'ques':"Q : Which is the smallest country in the world?",
                'options':{'A':"Monaco",'B':"Vatican City",'C':"Maldives",'D':"San Marino"},
                'ans':"B"
            },

            {
                'ques':"Q : In which year did World War II end?",
                'options':{'A':"1942",'B':"1945",'C':"1947",'D':"1950"},
                'ans':"B"
            },

            {
                'ques':"Q : Who invented the telephone?",
                'options':{'A':"Alexander Graham Bell",'B':"Thomas Edison",'C':"Nikola Tesla",'D':"James Watt"},
                'ans':"A"
            },

            {
                'ques':"Q : Who was the Ancient Greek God of the Sun?",
                'options':{'A':"Apollo",'B':"Zeus",'C':"Ares",'D':"Hades"},
                'ans':"A"
            },

            {
                'ques':"Q : Which is the only country in the world that has a non-rectangular national flag?",
                'options':{'A':"Bhutan",'B':"Nepal",'C':"Switzerland",'D':"Vatican City"},
                'ans':"B"
            },

            {
                'ques': "Which ancient library, considered one of the largest and most significant in the world, was destroyed by fire?",
                'options': {'A':"Library of Alexandria",'B':"Nalanda University Library",'C':"Pergamum Library",'D':"Ashurbanipal Library"},
                'ans': "A"
            }  
        ],

        'Science':[
            # ------------ Science ------------
            {
                'ques':"Q : What is the speed of light in vacuum?",
                'options':{'A':"3x10^8 m/s",'B':"1.5x10^8 m/s",'C':"3x10^6 m/s",'D':"3x10^5 km/s"},
                'ans':"A"
            },

            {
                'ques':"Q : Which organelle is known as the powerhouse of the cell?",
                'options':{'A':"Nucleus",'B':"Mitochondria",'C':"Ribosome",'D':"Chloroplast"},
                'ans':"B"
            },

            {
                'ques':"Q : Which vitamin is produced by sunlight?",
                'options':{'A':"Vitamin A",'B':"Vitamin B12",'C':"Vitamin D",'D':"Vitamin C"},
                'ans':"C"
            },

            {
                'ques':"Q : The process of plants making food using sunlight is called?",
                'options':{'A':"Respiration",'B':"Photosynthesis",'C':"Transpiration",'D':"Fermentation"},
                'ans':"B"
            },

            {
                'ques':"Q : Which scientist gave the three laws of motion?",
                'options':{'A':"Galileo",'B':"Einstein",'C':"Newton",'D':"Kepler"},
                'ans':"C"
            },

            {
                'ques':"Q : How many elements are in the periodic table?",
                'options':{'A':"108",'B':"118",'C':"128",'D':"138"},
                'ans':"B"
            },

            {
                'ques':"Q : Which of these is responsible for carrying oxygen in human blood?",
                'options':{'A':"Hemoglobin",'B':"Plasma",'C':"Platelets",'D':"White blood cells"},
                'ans':"A"
            }
        ],

        'Maths':[
            # ------------ Maths------------
            {
                'ques':"Q : What is 15²?",
                'options':{'A':"200",'B':"215",'C':"225",'D':"250"},
                'ans':"C"
            },

            {
                'ques':"Q : What is 3/4 of 200?",
                'options':{'A':"100",'B':"125",'C':"150",'D':"175"},
                'ans':"C"
            },

            {
                'ques':"Q : Solve: 2x + 5 = 15. Find x.",
                'options':{'A':"4",'B':"5",'C':"6",'D':"7"},
                'ans':"B"
            },

            {
                'ques':"Q : What is the perimeter of a square with side 12?",
                'options':{'A':"36",'B':"44",'C':"48",'D':"52"},
                'ans':"C"
            },

            {
                'ques':"Q : What is 8! (factorial)?",
                'options':{'A':"40320",'B':"5040",'C':"362880",'D':"720"},
                'ans':"A"
            },

            {
                'ques':"Q : Solve for x: 2x + 5 = 17.",
                'options':{'A':"4",'B':"5",'C':"6",'D':"7"},
                'ans':"C"
            },

            {
                'ques':"Q : The perimeter of a square is 48 cm. What is its area?",
                'options':{'A':"121 cm²",'B':"144 cm²",'C':"169 cm²",'D':"196 cm²"},
                'ans':"B"
            }
        ]
    },

    'hard':{
        'General':[
            # ------------- General Knowledge ------------
            {
                'ques':"Q : Who was the first woman to win a Nobel Prize?",
                'options':{'A':"Marie Curie",'B':"Rosalind Franklin",'C':"Mother Teresa",'D':"Ada Lovelace"},
                'ans':"A"
            },

            {
                'ques':"Q : Machu Picchu is located in which country?",
                'options':{'A':"Mexico",'B':"Peru",'C':"Brazil",'D':"Chile"},
                'ans':"B"
            },

            {
                'ques':"Q : The Magna Carta was signed in which year?",
                'options':{'A':"1215",'B':"1315",'C':"1415",'D':"1515"},
                'ans':"A"
            },

            {
                'ques':"Q : Who painted the 'Mona Lisa'?",
                'options':{'A':"Vincent Van Gogh",'B':"Pablo Picasso",'C':"Leonardo da Vinci",'D':"Michelangelo"},
                'ans':"C"
            },

            {
                'ques':"Q : The city of Constantinople is now called?",
                'options':{'A':"Ankara",'B':"Athens",'C':"Istanbul",'D':"Baghdad"},
                'ans':"C"
            },

            {
                'ques':"Q : What is acrophobia a fear of?",
                'options':{'A':"Spiders",'B':"Heights",'C':"Crowds",'D':"Water"},
                'ans':"B"
            },

            {
                'ques':"Q : Which country has the highest life expectancy?",
                'options':{'A':"Japan",'B':"Monaco",'C':"Hong Kong",'D':"Iceland"},
                'ans':"C"
            }
        ],

        'Science':[
            # ------------ Science ------------
            {
                'ques':"Q : What is the chemical symbol of gold?",
                'options':{'A':"Ag",'B':"Gd",'C':"Au",'D':"Pt"},
                'ans':"C"
            },

            {
                'ques':"Q : Who discovered penicillin?",
                'options':{'A':"Louis Pasteur",'B':"Alexander Fleming",'C':"Joseph Lister",'D':"Robert Koch"},
                'ans':"B"
            },

            {
                'ques':"Q : Which part of the brain controls balance?",
                'options':{'A':"Cerebrum",'B':"Medulla",'C':"Cerebellum",'D':"Hypothalamus"},
                'ans':"C"
            },

            {
                'ques':"Q : Which is the most abundant gas in Earth's atmosphere?",
                'options':{'A':"Oxygen",'B':"Nitrogen",'C':"Carbon dioxide",'D':"Argon"},
                'ans':"B"
            },

            {
                'ques':"Q : Which blood cells help in clotting?",
                'options':{'A':"RBCs",'B':"WBCs",'C':"Platelets",'D':"Plasma"},
                'ans':"C"
            },

            {
                'ques':"Q : Which law explains why we need to wear seatbelts in a moving car?",
                'options':{'A':"Newton's First Law",'B':"Newton's Second Law",'C':"Newton's Third Law",'D':"Law of Gravitation"},
                'ans':"A"
            },

            {
                'ques':"Q : What happens to the frequency of a sound wave if its wavelength is doubled but the speed of sound remains constant?",
                'options':{'A':"It doubles",'B':"It halves",'C':"It becomes zero",'D':"It remains unchanged"},
                'ans':"B"
            }
        ],

        'Maths':[
            # ------------ Maths------------
            {
                'ques':"Q : Solve: (2x + 3)(x - 4) = 0. One solution is?",
                'options':{'A':"x=2",'B':"x=-3/2",'C':"x=4",'D':"Both B and C"},
                'ans':"D"
            },

            {
                'ques':"Q : What is the derivative of x²?",
                'options':{'A':"x",'B':"2x",'C':"x²",'D':"1"},
                'ans':"B"
            },

            {
                'ques':"Q : What is the value of log10(1000)?",
                'options':{'A':"1",'B':"2",'C':"3",'D':"4"},
                'ans':"C"
            },

            {
                'ques':"Q : If sinθ = 1/2, θ = ?",
                'options':{'A':"30°",'B':"45°",'C':"60°",'D':"90°"},
                'ans':"A"
            },

            {
                'ques':"Q : The area of a circle with radius 7 is?",
                'options':{'A':"154",'B':"144",'C':"176",'D':"132"},
                'ans':"A"
            },

            {
                'ques':"Q : How many faces does a Dodecahedron have?",
                'options':{'A':"8",'B':"10",'C':"12",'D':"14"},
                'ans':"C"
            },

            {
                'ques':"Q : If √x + 2 = 7, find the value of x.",
                'options':{'A':"15",'B':"25",'C':"36",'D':"49"},
                'ans':"B"
            }
        ]
    }
}




while True:
    score = 0
    print("-------------- START --------------")

    while True:
        level = input("Difficulty (Easy / Medium / Hard) :\n").lower()

        if(level in question): # checking if level is in the dict or not 
            subject = input("Subject (General / Science / Maths) :\n").title()

            if(subject in question[level]): # checking that is inside level there is subject there or not.
                start = time.perf_counter()

                for i,q in enumerate(random.sample(question[level][subject] , 5)): # enumerate is used to access both keys and values || easy way '_' 
                    question_list = (question[level][subject])
                    # If not enough questions it will print display the user.

                    if(len(question_list) < 5):
                        print("Not Enough Questions yet, Please Choose Another Subject.")
                        continue
                    print("\n",q['ques'])

                    for keys, values in q['options'].items(): # displaying options of questions using item() function
                        print(keys,':',values)

                    while True:
                        user_ans = input("Enter a Choice (A/B/C/D): ").upper()
                        if(user_ans in ['A','B','C','D']):

                            if(user_ans == q['ans']):
                                score += 100
                                print("Correct !!")
                                break
                            else:
                                score -= 50
                                # Accesing both option like (A,B...) and its value.
                                print("Incorrect !! Correct Answer is ",q['ans']+' : '+q['options'][q['ans']])  # for accessing we can also write (keys+' : '+values)
                            break

                        else:
                            print("Invalid Choice, Choose From (A / B / C / D).")

                end = time.perf_counter()

                # Score Showing----------------
                if(score == 500):
                    print("Score :", score," Excellent!")

                elif(score < 500  and  score >= 100):
                    print("Score :",score," Good!")

                else:
                    print("Score :", score," Keep it Up!")

                total_time = end - start

                if(total_time < 60  and total_time >= 0):
                    print("Total Time Taken: ",round(total_time , 2)," Seconds")

                elif(total_time >= 60  and  total_time < 3600):
                    total_time /= 60
                    print("Total Time Taken: ",round(total_time , 2),"Minutes")

                else:
                    total_time /= 3600
                    print("Total Time Taken: ",round(total_time , 2),"Hours") 

                break        

            else:
                print("Invalid Subject , Try Again!! ")   

        else:
            print("Invalid Level ! , Try Again!! ")

    again = input("Wanna Play Again (Yes / No) ?? \n").title()
    if(again != 'Yes'):
        print("Thank You For Playing ! See Ya")
        quit()

