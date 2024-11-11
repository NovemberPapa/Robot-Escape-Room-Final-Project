import cyberpi
import event
import time

'''

Two functions:

updatescores(scores, newscore) updates a list of current scores. Parameter -scores- is a list of 6 lists.
Ex[["alex_",123], ["sam__", 124], ["idk__", 124], [], [], []]
This example list holds 3 players times with 3 empty placeholders. Each list in the list represents a rank on the leaderboard
which can only hold 6 positions. The parameter -newscore- is the new time in SECONDS from the latest game played. It takes this new time and adds an entry
to the leaderboards if it is less than any current entry OR there is an empty spot in the list.
Technically, the newscore value can only go up to 6049 seconds.
The name that is entered can only be 5 letters, numbers, or "_" due to space on cyberpi. 
The list does NOT save after the cyberpi is reset or turned off. 

displayscores(scores) Takes a list of 6 lists and displays a highscore rank on the screen.
The function does not remove the display. Whatever the next function to go hould clear display or I can update the code to clear after pressing a button. idk

the code in hashes below is test code if you want to try this out. copy/paste this whole code into mblock.
you can update the newtime variable to be whatever (<=6049 seconds) and the current scores list (just keep names with 5 characters).
Ex of list
[[], [], [], [], [], []] this has no entries (the cyberpi just turned on and a game hasn't been completed yet)
[["alex_",123], ["sam__", 124], ["idk__", 124], [], [], []] this list has 3 entries, 3 games have aready happened.


'''

################################################################

@event.is_press('b')
def do_thing():
    newtime= 149
    scores=[['alex_',123], ["sam__", 124], ["boop_", 125],["beep_", 125],["3hree", 130],["poke_", 150]]
    scores = updatescores(scores, newtime)
    displayscores(scores)


    
################################################################

def updatescores(scores, newscore):
    '''
    Given current list of names and times and a new time entry,
    displys screen to input new name entry to list
    '''
    cyberpi.display.clear()
    cyberpi.controller.reset_count("any")
    #cyberpi doesn't allow displayed text to wrap easily so extra long string. cyberpi is 16 bits across.
    #5 spaces + ##### + 11 spaces + ##### + 6 spaces = 2 lines
    name = "     _____           *          "
    minute = newscore // 60
    sec = newscore % 60
    ups = 0
    downs = 0
    rights = 0
    lefts = 0
    a = 0
    is_Done=False
    entry1=5
    entry2=6
    while is_Done == False:
        while (cyberpi.controller.get_count("up") == ups and cyberpi.controller.get_count("down")==downs and
               cyberpi.controller.get_count("left")==lefts and cyberpi.controller.get_count("right")==rights
               and cyberpi.controller.get_count("a") == a):
            cyberpi.controller.is_press("up")
            cyberpi.controller.is_press("down")
            cyberpi.controller.is_press("left")
            cyberpi.controller.is_press("right")
            cyberpi.controller.is_press("a")
            #title is 4 lines long
            title="Congrats!       Your time is:      "+str(minute)+"min"+str(sec)+"sec"+"    Enter Name:     "
            #name input is 2 lines long
            #one more line for "press a to enter"
            cyberpi.display.show_label(title+name+"Press A to enter", 16, 'center')
            cyberpi.controller.is_press("up")
            cyberpi.controller.is_press("down")
            cyberpi.controller.is_press("left")
            cyberpi.controller.is_press("right")
            cyberpi.controller.is_press("a")
        if cyberpi.controller.get_count("right") != rights:
            entry1= entry1+1
            entry2= entry2+1
            if entry2==11:
                entry1=5
                entry2=6
            name = name[0:10] + (' '* (entry1+6))  + '*' + (' ' * (15-entry1))
            rights = rights +1
        elif cyberpi.controller.get_count("left") != lefts:
            entry1= entry1-1
            entry2= entry2-1
            if entry2==5:
                entry1=9
                entry2=10
            name = name[0:10] + (' '* (entry1+6))  + '*' + (' ' * (15-entry1))
            lefts = lefts +1
        elif cyberpi.controller.get_count("down") != downs:
            if name[entry1:entry2]=='_':
                name = name[0:5] + name[5:entry1]+'A'+name[entry2:10] + name[10:32]
            elif name[entry1:entry2]=='Z':
                name = name[0:5] + name[5:entry1]+'0'+name[entry2:10] + name[10:32]
            elif name[entry1:entry2]=='9':
                name = name[0:5] + name[5:entry1]+'_'+name[entry2:10] + name[10:32]
            elif 65 <= ord(name[entry1:entry2]) < 90:
                name = name[0:5] + name[5:entry1]+chr(ord(name[entry1:entry2])+1)+name[entry2:10] + name[10:32]
            elif 48 <= ord(name[entry1:entry2]) < 57:
                name = name[0:5] + name[5:entry1]+chr(ord(name[entry1:entry2])+1)+name[entry2:10] + name[10:32]
            downs = downs + 1
        elif cyberpi.controller.get_count("up") != ups:
            if name[entry1:entry2]=='_':
                name = name[0:5] + name[5:entry1]+'9'+name[entry2:10] + name[10:32]
            elif name[entry1:entry2]=='A':
                name = name[0:5] + name[5:entry1]+'_'+name[entry2:10] + name[10:32]
            elif name[entry1:entry2]=='0':
                name = name[0:5] + name[5:entry1]+'Z'+name[entry2:10] + name[10:32]
            elif 65 < ord(name[entry1:entry2]) <= 90:
                name = name[0:5] + name[5:entry1]+chr(ord(name[entry1:entry2])-1)+name[entry2:10] + name[10:32]
            elif 48 < ord(name[entry1:entry2]) <= 57:
                name = name[0:5] + name[5:entry1]+chr(ord(name[entry1:entry2])-1)+name[entry2:10] + name[10:32]
            ups = ups + 1
        elif cyberpi.controller.get_count("a") != a:
            cyberpi.display.clear()
            
            name = name[5:10]
            #scores ony holds 6 ranks, top line for "HIGHSCORES:" ony 7 lines can be displayed
            newentry = [name, newscore]
            rank = 0
            for tier in scores:
                #print(tier)
                if tier == []:
                    if rank ==0:
                        scores= [newentry] + scores[0:5]
                        break
                    elif rank ==5:
                        scores = scores[0:5] + [newentry]
                    else:
                        scores = scores[0:rank] + [newentry] + scores[rank:6]
                        scores = scores[0:6]
                        break
                elif tier[1] > newentry[1]:
                    if rank == 0:
                        scores = [newentry] + scores[0:5]
                        break
                    elif rank == 5:
                        scores = scores[0:5] + [newentry]
                        break
                    else:
                        scores = scores[0:rank] + [newentry] + scores[rank:6]
                        scores = scores[0:6]
                        break
                elif rank == 5:
                    cyberpi.controller.reset_count("any")
                    while cyberpi.controller.get_count("a") == 0:
                        cyberpi.display.clear()
                        cyberpi.display.show_label("Sorry, you did  not make the    Leaderboards :C  Press A", 16, 'center')
                
                rank = rank +1
            is_Done = True    
    cyberpi.display.clear()
    return scores

def displayscores(scores):
    cyberpi.display.clear()
    display1 = "HIGHSCORES:     "
    place = 1
    for tier in scores:
        if tier == []:
            name='     '
            minute ="00"
            sec = "00"
            
        else:
            name = tier[0]
            time= tier[1]
            minute= str(time // 60)
            sec = str(time % 60)
            if len(minute)==1:
                minute = "0"+minute
            
            if len(sec)==1:
                sec = "0" + sec
                
        display1 = display1 + str(place)+'.'+name+' '+(minute)+'m'+(sec)+"s  "
        place = place + 1
    cyberpi.display.show_label(display1, 16, 'center')


                    
            
          
                    












                
