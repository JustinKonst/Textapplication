import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes =  ["Y", "y", "yes", "Yes"]
no = ["N", "n", "No", "no"]

required = ("\nUse only A, B or C\n")

def intro():
    print ("September 30th 2058 "
"Somewhere in space "
"On the UES Contact Light "
"A spaceship to cargo items to different worlds "
"You, are in the UES Contact Light, employed to make sure not a single cargo is left unchecked or disappears during the flight "
"Today's cargo seems especially important, extra care has been made to ensure that the cargo is guarded. "
"The extra care in question was to get hired guns, to your left you see an engineer, you notice that he can make his own Turrets, " 
"HQ must have given him good money to keep this place Guarded "
"To the engineer's left, you see a robot, you're unsure if the engineer made this robot, but this robot seems to be more advanced than the turrets. " 
"way, you notice that the robot has been equipped with a minigun, HQ definitely put a lot of money on securing this robot. "
"To the right, you see… "
"Wait… is this guy even hired? He looks like a thief, should I… should I call HQ? "
"He is just sitting there eating beans and fast too, look at him munch! Where did HQ get this guy? " 
"The “thief” does look dapper though, he's got a revolver on his belt and a shotgun right on his back, "
"maybe he's one of those “Westerners” people talk about. "
"The thief glances at you, then starts to stand up and walk towards you."
"“Hey pal,” said the thief “What's up with these packages, I didn't get this information in my contract.”")

time.sleep(1)
print ("Choose response"
" A. I don't know, they haven't told me anything either"
" B. Special delivery probably"
" C. How can you eat those beans so fast")
choice = input(">>> ")
