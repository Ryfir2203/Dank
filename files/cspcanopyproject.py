vars=[0, 0]

def introduction():                                             #creates the introduction to the story
    print "Idaho Smith and the Temple of the Jade Donkey\n"
    print "The Temple of the Jade Donkey has long been a thing of legend. Rumored to be located within the depths of the Amazon Rainforest, you, Idaho Smith, have been sent by the Order of the Explorers to investigate it. You stand outside the entrance to the ancient building, eager to find out what lies within.\n"
    window_or_door()                                            #gives choices
    
def window_or_door():                                           #defines the 2 choices
  global theend
  while(vars[1]==0):
    print "There seem to be two ways to enter the temple, the main entrance or what seems to be a hole halfway up the stone walls of the structure. You think the entrance may be trapped, but climbing those vines would also be dangerous.\n\n(A) Head through the main entrance\n(B) Make your way up the vines towards the hole\n(Type a letter and press return)"
    answer = raw_input()
    print ("\n" * 5)                                            #creates 5 blank lines
    answer = answer.lower()
    if answer=="a":                                             #<
      choice_entrance()                                         #<--- checks for specific input 
    elif answer=="b":                                           #<
      choice_hole()                                             
    else:                                                       #adresses other inputs
        print "Idaho Smith may be the best explorer this side of Boise, but he cant do that!\n"
        
def choice_hole():
    print "After an easy enough climb, you make it up and into the temple and find yourself in a medium sized chamber. Vines hang from the ceiling and a rat scurries across the floor and under a pile of bricks. You noticed that the rat had something shiny in its mouth. You figure there are two ways to get the rat out of the bricks.\n\n(A) Kick the pile of bricks until the rat gets scared out\n(B) Pour your flask of Idaho Whiskey into the pile of bricks and light it on fire"
    answer = raw_input()
    print ("\n" * 5)                                           #creates 5 blank lines
    answer = answer.lower()
    if answer=="a":                                            #<
      choice_kick()                                            #<--- checks for specific input
    elif answer=="b":                                          #<
      choice_whiskey()
    else:                                                      #adresses other inputs
        print "Idaho Smith may be the best explorer this side of Boise, but he cant do that!\n"
        
def choice_kick():
    print "You kick the pile of bricks for about a half hour. You cant feel your toes, but the rat finally scurries out and drops the object as it runs. You pick up what you now see is a silver key. It is in suprisingly good condition, and there seems to be a keyhole in the door on the other side of the room."
    print ("\n" * 5)                                          #creates 5 blank lines
    bladeroom()
    
def choice_whiskey():
    print "You empty your whiskey flask into the pile of bricks, take out your fire starter, and light it up. The flaming rat runs out of the bricks and drops the object as it flees. You pick up what you now see is a silver key. It is in suprisingly good condition, and there seems to be a keyhole in the door on the other side of the room."
    print ("\n" * 5)                                          #creates 5 blank lines
    bladeroom()
    
def choice_entrance():
    print "You drink the last of your Idaho whiskey and walk calmly into the entrance and find yourself in a large central chamber. All but two doors have collapsed. The door on the left has footprints leading into it, and the one on the right seems undisturbed.\n\n(A) Take the left door\n(B) Take the right door"
    answer = raw_input()
    print ("\n" * 5)                                          #creates 5 blank lines
    answer = answer.lower()
    if answer=="a":                                           #<
      choice_leftdoor()                                       #<--- checks for specific input
    elif answer=="b":                                         #<
      choice_rightdoor()
    else:                                                     #adresses other inputs
        print "Idaho Smith may be the best explorer this side of Boise, but he cant do that!\n"
        
def choice_leftdoor():
    print "You follow the footprints through the door and into a small chamber. The chamber is scorched and there is a faint smell of chicken. Nothing seems of interest, so you follow the prints out of the chamber once again."
    print ("\n" * 5)                                         #creates 5 blank lines
    bladeroom()
    
def choice_rightdoor():
    print "You head through the door and see a small chamber. In the middle of the chamber lies a skeleton with a vaguely familiar hat. You recognize the hat as belonging to the long missing beloved adventurer North Dakota Nick. With no sign of how he died, you gulp and head further into the temple."
    print ("\n" * 5)                                        #creates 5 blank lines
    bladeroom()
    
def bladeroom():
    print "You reach a very long hallway filled with skeletons. Upon closer inspection, you notice that the walls are covered in spike traps. You throw a rock into the hallway, spikes fly out of the walls and retract ten seconds later. There seem to be several ways of going about this.\n\n(A) Run through the hall\n(B) Throw your empty whiskey flask into the hall and run through the spikes before they reset\n(C) Wait for something to happen\n(D) Use your trusty pea shooter to hit the kill switch on the other side of the hall"
    answer = raw_input()
    print ("\n" * 5)                                       #creates 5 blank lines
    answer = answer.lower()
    if answer=="a":                                        #<
      choice_runhall()                                         #<
    elif answer=="b":                                      #<
      choice_throw()                                       #<--- checks for specific input
    elif answer=="c":                                      #<
      choice_wait()                                        #<
    elif answer=="d":                                      #<
      choice_peashooter()
    else:                                                  #adresses other inputs
        print "Idaho Smith may be the best explorer this side of Boise, but he cant do that!\n"
        
def choice_runhall():
    print "You run through the hall and the spikes impale you, killing you instantly.\n(You really thought that would work?)\n\n YOU HAVE DIED"
    print ("\n" * 5)                                      #creates 5 blank lines
    bladeroom()
    
def choice_throw():
    print "You throw the empty flask into the hall. The spikes extend as expected, so you make a run for it. You almost reach the end, but the spikes reset before you can and impale you, killing you instantly.\n(I guess you could say that was whiskey business)\n\n YOU HAVE DIED"
    print ("\n" * 5)                                     #creates 5 blank lines
    bladeroom()
    
def choice_peashooter():
    print "You take aim and fire at the button. You hit your target dead on, only to realize it wasnt the kill switch. A trap door opens beneath you and you fall to your death.\n(What are the odds of that?)\n\n YOU HAVE DIED "
    print ("\n" * 5)                                    #creates 5 blank lines
    bladeroom()
    
def choice_wait():
    print "While you are waiting, you notice the ceiling of the hallway shifting and creaking. After about five hours, the ceiling collapses, blocking the spike traps. You walk through the hall without being impaled and make your way to the next room. You emerge into the next room only to see a large pit of capybaras blocking you from the middle of the room. There are pillars in the pit that look as if they could be used to jump across. 'Capybaras', you say. 'Why did it have to be capybaras?'\n\n(A) Use the Pillars to jump across the pit\n(B) Swing across using some vines from the ceiling\n(C) Jump the pit using your explorer brand jumping shoes\n(D) Climb across the wall and over the pit"
    answer = raw_input()
    print ("\n" * 5)                                   #creates 5 blank lines
    answer = answer.lower()
    if answer=="a":                                    #<
      choice_pillars()                                 #<
    elif answer=="b":                                  #<
      choice_swing()                                   #<--- checks for specific input
    elif answer=="c":                                  #<
      choice_jump()                                    #<
    elif answer=="d":                                  #<
      choice_climb()
    else:                                              #adresses other inputs
        print "Idaho Smith may be the best explorer this side of Boise, but he cant do that!\n"
        
def choice_pillars():
    print "You make the jump onto the first pillar just fine, however your second landing does not go nearly as well when you slip and fall on a pile of bat droppings.\n(Death by ROUS)\n\n YOU HAVE DIED"
    print ("\n" * 5)                                  #creates 5 blank lines
    choice_wait()
    
def choice_swing():
    print "You grab the nearest vine. When you are about to swing, you realize that this vine is infact a deadly snake. Atleast it was a better way to go than the capybaras\n(Snake? SNAAAAKKEEE?!)\n\n YOU HAVE DIED."
    print ("\n" * 5)                                  #creates 5 blank lines
    choice_wait()
    
def choice_jump():
    print "It is impressive how far you were able to jump, but not impressive enough.\n(Capybaras are actually very friendly creatures, your just allergic)\n\n YOU HAVE DIED"
    print ("\n" * 5)                                 #creates 5 blank lines
    choice_wait()
  
def choice_climb():
    print "Several bricks fall off the wall at your touch, but you make it across in one piece. As you proceed to the next chamber, you begin to hear familiar voices. You enter the chamber and see exactly what you had hoped you would. The Jade Donkey, seated upon a rock in the middle of the room. What you did not expect to see, however, were several key members of the adventurers guild waiting for you. You recognize them as Arizona Abe, Mississippi Marve, Florida Frank, and his apprentice, Tallahassee Tim.\n\n(A) 'What the hell is going on here?'\n(B) 'I thought you guys were on vacation in Hawaii'"
    answer = raw_input()
    print ("\n" * 5)                                 #creates 5 blank lines
    answer = answer.lower()
    if answer=="a":                                  #<
      choice_what()                                  #<--- checks for specific input
    elif answer=="b":                                #<
      choice_hawaii()
    else:                                            #adresses other inputs
        print "Idaho Smith may be the best explorer this side of Boise, but he cant do that!\n"
        
def choice_what():
    print "Florida Frank: 'I wouldnt talk to my superiors that way if I were you, Smith. Everybody already hates you anyway.'\n\nYou: 'Yea yea, Everybody hates me because my name doesnt match...'\n\nFlorida Frank: 'And it is for that reason that we tried to kill you with this temple.'"
    print ("\n" * 2)                                #creates 2 blank lines
    oh()
  
def choice_hawaii():
    print "Florida Frank: 'No, we were here. Building this temple, importing capybaras, and crafting a Jade Donkey..... all to kill you.'\n\nYou: Why would you want to kill ME?\n\nFlorida Frank: 'You have been the only one in 1,000 years to have broken our code and still been inducted. Your name does not match.'"
    print ("\n" * 2)                                #creates 2 blank lines
    oh()
  
    
def oh():
    print "(A) 'Im telling the guild about this'\n(B) 'Traitors!'"
    answer = raw_input()
    print ("\n" * 5)                               #creates 5 blank lines
    answer = answer.lower()
    if answer=="a":                                #<
      choice_tell()                                #<--- checks for specific input
    elif answer=="b":                              #<
      choice_traitor()
    else:                                          #adresses other inputs
        print "Idaho Smith may be the best explorer this side of Boise, but he cant do that!\n"
        
def choice_tell():
    print "Florida Frank: 'Im afraid you will never have the chance. Apprentice, kill him and show that you have what it takes to join the order.'\n\nTallahassee Tim: 'Yes Master!'\n\nTallahassee Tim draws his sword. You realize that youve never had a sword and feel slightly jealous. You wonder how your gonna get out of this one."
    print ("\n" * 2)                               #creates 2 blank lines 
    timduel()
    
def choice_traitor():
    print "Florida Frank: 'I am afraid it is you who is the traitor, Smith. Apprentice, Kill him and prove you are worthy to join the order.'\n\nTallahassee Tim: 'Yes Master!'\n\nTallahassee Tim draws his sword. You realize that youve never had a sword and feel slightly jealous. You wonder how your gonna get out of this one." 
    print ("\n" * 2)                               #creates 2 blank lines
    timduel()
    
def timduel():
    print "(A) Shoot Tim with your pea shooter\n(B) Run\n(C) Divide by zero\n(D) Sticky Grenade"
    answer = raw_input()
    print ("\n" * 5)                               #creates 5 blank lines
    answer = answer.lower()
    if answer=="a":                                #<
      choice_shoot()                               #<
    elif answer=="b":                              #<
      choice_run()                                 #<--- checks for specific input
    elif answer=="c":                              #<
      choice_zero()                                #<
    elif answer=="d":                              #<
      choice_grenade()
    else:                                          #adresses other inputs
        print "Idaho Smith may be the best explorer this side of Boise, but he cant do that!\n"
        
def choice_grenade():
    print "You pull your only sticky grenade out of your jacket. You try to throw it, but it sticks to your hand.\n(I always wondered how those things work)\n\n YOU HAVE DIED"
    print ("\n" * 5)                               #creates 5 blank lines
    timduel()
    
def choice_zero():
    print "You pull out your phone, open up the calculator app, and divide by zero. A slight hum makes its way through the room. You find it oddly soothing as your body goes numb, the room begins to shake, and everything fades to white.\n(Hey guys I just went to the bathroom real q-. Wait, where is everyone?)\n\n YOU HAVE DIED"
    print ("\n" * 5)                               #creates 5 blank lines
    timduel()
    
def choice_run():
    print "You turn around and make a run for it, only to realize the door closed, and that Tallahassee Tim has thrown his sword straight into your neck.\n(They say time heals all wounds, I dont think this is what they ment.)\n\n YOU HAVE DIED"
    print ("\n" * 5)                               #creates 5 blank lines
    timduel()
    
def choice_shoot():
    print "Tallahassee Tim swings his sword around as if he is showing off. You take out your pee shooter and shoot him dead. Tim falls to the ground and you run towards the exit. You manage to escape the temple the way you came and collapse the entrance so that the guild may come back and collect the traitors later. you head back to your plane where your apprentice, Boise Bob, waits to fly back home.\n\n THE END!"
    print ("\n" * 10)                             #creates 10 blank lines
    
    
introduction()                                    #restarts the game
    
    