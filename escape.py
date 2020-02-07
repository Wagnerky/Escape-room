# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:32:23 2020

@author: filmk
"""
controls = "* For commands you must first type the action and then the item you wish to interact with\n"\
"[look left/right] = allows you to face a new wall\n"\
"[open xxxx] = allows you to open objects\n"\
"[use xxxx on xxxx] = uses the first item on the second\n"\
"[get xxxx] = adds discovered items to inventory\n"\
"[see inventory] = displays the items you have collected\n"\
"[see controls] = displays the controls\n"\
"[enter xxxx] = allows you to enter number to a keypad\n"\
"\n**Please note, when you find something you need to 'get' it. Otherwise you won't bring it with you.**"\

 
north_wall_close = "You are facing the North wall. You see a barricaded door. \nTry as you might the door will not open."
north_wall_open = "You are facing the North wall. The door is no longer barricaded."
east_wall = "You are facing the east wall. You see a cabinet with a locked box on top."
south_wall ="You are facing the south wall. You see a key frozen inside some ice."
west_wall = "You are facing the west wall. You see a key pad with the numbers 1-9 in the wall."

def open_thing(control, room_count,lock):
    """
    function takes in players input, the room count, and the status of the object. checks to see if all criteria are meet
    to open object. If so texted is displayed and the objects status is updated.
    """
    if control[1] =="cabinet" and room_count == 1 and lock == "unlocked":
        print("you open the top drawer of the cabinet. In it you see a lighter.")
        return "open"
    if control[1] =="chest" and room_count == 1 and lock == "unlocked":
        print("You open the chest. Inside the numbers 4483 are inscribed to its base.")
        return "open"
    if control[1] == "door" and room_count == 0 and lock == "unlocked":
        return "open"
    else:
        print("Either it's locked, or you're on the wrong side of the room.")
        return None
    
def add_to_inventory(control, room_count,furniture,items,inventory):
    """
    function takes in the players input, the object (furniture) that the item is held in, the player's own
    inventory, and the game's inventory. Checks to see if the criteria to actually get the item are meet. if meet,
     it pops the item from the game's inventory and appends it to the players inventory.
    """
    
    if control[1] =="lighter" and room_count == 1 and furniture == "open":
        lighter = items.pop(1)
        inventory.append(lighter)
        print("* Lighter added to inventory *")
        return None
    
    if control[1] == "key" and room_count == 2 and furniture == "unlocked":
        key = items.pop()
        inventory.append(key)
        print("* key added to inventory *")
        return None
    else:
        print("Try as you might, you can't",*control,".")
        return None

def use(control, room_count, item, inventory):
    
    if control[1] == "lighter" and control[2] == "on" and (control[3] == "key" or control[3] == "ice") and room_count == 2 and "lighter" in inventory and item == "locked":   
        print("It took you a while, but eventually the ice around the key melted.")
        return "unlocked"
    if control[1] == "key" and control[2] == "on" and control[3] == "chest" and room_count == 1 and "key" in inventory and item == "locked":
        print("You hear a click from the chest as you finish turning the key.")
        return "unlocked"
    if control[1] == "lighter" and control[2] == "on" and (control[3] == "key" or control[3] == "ice") and room_count == 2 and "lighter" in inventory and item == "unlocked":
        print("The lighter is out of Butane and you already got the key. Why are you wasting time?")
        return "unlocked"
    if control[1] == "key" and control[2] == "on" and control[3] == "chest" and room_count == 1 and "key" in inventory and item == "unlocked":
        print("For some reason you lock the chest again. Thankfully you have the key to unlock it again.")
        return "locked"
    else:
        print ("Try as you might, you can't",*control,".")
        return "locked"

def enter(control, room_count):
    if control[1] == "4483" and room_count == 3:
        print("Access Granted")
        print("You hear a loud 'Clunk' from the north wall")
        return "unlocked"
    if room_count != 3:
        print("There doesn't seem be any place to enter these numbers on this side of the room")
        return "locked"
    if control[1] != "4483" and room_count == 3:
        print("Access Denied")
        return "locked"
    
        

def room_look(control,room_count,pass_code):
    """
    Updates where the player is looking and returns the value of the room in the end. Room 0 = north
    room 1 = east, room 2 = west, and room 3 = south. room count resets to zero if at 4 or goes to -1 
    """
    if control[1] == "left":
        room_count += 1
    if control[1] == "right":
        room_count -= 1
    if room_count == -1:
        room_count = 3
    if room_count == 4:
        room_count = 0
    if control[1] != "left" and control[1] != "right":
        print("You don't know how to look",control[1])
        return room_count
        
    if room_count == 0 and pass_code =="locked":
        print(north_wall_close)
        return room_count
    if room_count == 0 and pass_code =="unlocked":
        print(north_wall_open)
        return room_count
    if room_count == 1:
        print(east_wall)
        return room_count
    if room_count == 2:
        print(south_wall)
        return room_count
    if room_count == 3:
        print(west_wall)
        return room_count
    
def main():
    inventory = []
    items = ["key","lighter"]
    chest= "closed"
    chest_lock = "locked"
    cabinet = "closed"
    door = "closed"
    pass_code = "locked"
    cabinet_open = "unlocked"
    key = "locked"
    
    
    room_count = 0
    start= input("Welcome to the room escape. press enter to begin.")
    
    print(start)
    print(' ')
    print(' ')
    print(controls)
    print(' ')
    print(' ')
    print(north_wall_close)
   
    
    while True:
        control = input(": ").lower().split()
        if not control:
            print ("You just stood in place.")
            continue
        if control[0]== "look":
            print("")
            room_count = room_look(control,room_count,pass_code)
            continue
        
        if control[0]== "open":
            if control[1] == "chest":
                chest = open_thing(control, room_count, chest_lock)
                continue
            if control[1] == "cabinet":
                cabinet = open_thing(control, room_count,cabinet_open)
                continue
            if control[1] == "door":
                door = open_thing(control, room_count, pass_code)
                
            else:
                print("You tried to",*control,"but not much happened")
                continue
                
        if control[0] == "use":
            if control[1]== "lighter":
                key = use(control, room_count, key, inventory)
                continue
            if control[1] == "key":
                chest_lock = use(control, room_count, chest_lock, inventory)
                continue
            else:
                print("You tried to",*control,"but not much happened")
                continue
            
        if control[0] == "enter":
                pass_code = enter(control, room_count)
                continue
        
        if control[0]== "get":
            if control[1] == "lighter":
                add_to_inventory(control, room_count,cabinet,items,inventory)
                continue
            if control[1] =="key":
                add_to_inventory(control, room_count,key,items,inventory)
                continue
            else:
                print("You tried to",*control,"but not much happened")
                continue
        if control[0] == "see":
            if control[1] == "controls":
                print(controls)
                continue
            if control[1] == "inventory":
                print("Inventory:",*inventory)
                continue
            else:
                print("You tried to",*control,"but not much happened")
                continue
            
        
        if door == "open":
            print("you win!!!")
            break
        
        if control[0] =="q":
            break
        else:
            print("You tried to",*control,"but not much happened")
                  
    

if __name__ == '__main__':
    main()