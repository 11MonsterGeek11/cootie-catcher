
msg_A = "You’re just like bacon...you make everything better."
msg_B = 'You are someone’s "The one that got away”'
msg_C = """You are devastatingly good looking and that is the least interesting
thing about you."""
msg_D ="The F.B.I. tapped your phone just to hear your voice"
msg_E = "You could make one of the Queen’s guards crack a smile."
msg_F = "All your friends worry that they are not as funny as you."
msg_G = "You’re worth the last french fry in the bag."
msg_H = "You’re smarter than Google and Mary Poppins combined"


set_c = ['red', 'purple', 'blue', 'orange']
set_d = ['yellow', 'green', 'black', 'white']
set_a = [4, 8, 3, 7]
set_b = [5, 8, 2, 6]

def start():
    print ("Hi, I'm an origami game.  Do you want to play?  ")
    ans = input().lower()

    if ans.startswith('y'):
        print ("Great, let's begin")
    elif ans.startswith('n'):
        print ("You're boring and I don't like you.")
    else: 
        print ("Please enter Yes or No")
        start()

start()


def game_phase_one ():
    global answer_one    
    #print (answer)
    print ("""
    The origami has 8 sides on the outside to pick from.  Pick any number from 1 through
    8 and the origami will open and close that many times to reveal your next set of 
    choices.""")
    answer_one = int(input())

    if answer_one in set_a: #1 or answer == 2 or answer == 5 or answer == 6:
        print ("""
        Excellent! The origami has opened """ + str(answer_one) + """ times. Now pick a 
        color below and type it in""")
       
    elif answer_one in set_b: #== 3 or answer == 4 or answer == 7 or answer == 8:
         print ("""
        Excellent! The origami has opened """ + str(answer_one) + """ times. Now pick a 
        color below and type it in""")
       
    else: 
        print ("Lets try again")
        game_phase_one()

game_phase_one ()


def game_phase_two():
    global answer_two

    answer = answer_one % 2
    print (answer)

    if answer > 0:  #odd
        print (str(set_c) )
        answer_two = str(input())

    else: #even
        print (str(set_d) )
        answer_two = str(input())

game_phase_two()

def game_phase_three():
    global answer_three
    
    if answer_two in set_c:
        print ("Now for the last time pick one more color to get your fortune!" + str(set_d))
        answer_three = str(input())
    
    elif answer_two in set_d:
        print ("Now for the last time pick one more color to get your fortune!" + str(set_c))
        answer_three = str(input())

    else: 
        game_phase_two()

game_phase_three ()

    
def game_phase_four ():
    if answer_three == "red":
        print (msg_A)
    if answer_three == "purple": 
        print (msg_B)
    if answer_three == "blue": 
        print (msg_C)
    if answer_three == "orange": 
        print (msg_D)
    if answer_three == "yellow": 
        print (msg_E)
    if answer_three == "green": 
        print (msg_F)
    if answer_three == "black": 
        print (msg_G)
    if answer_three == "white": 
        print (msg_H)

game_phase_four()

