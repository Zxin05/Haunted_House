define xuezhi = Character('xuezhi', color= "#FF0000")
define xin = Character('xin', color= "#00FFFF")
#------------------------------------------------------------------------------------------------------------------------------------------------------
label mansion:
    scene mansion
    play music horrormusic volume 0.5
    show xuezhi at left
    xuezhi "we are finally here, one last chance to give up eh, xin."
    show xin at right
    menu:
        "Nah, I'm too brave to give up":
            show xinsmile at right
            xin "Nah, I'm too brave to give up"
            show xuezhismile at left
            xuezhi "alright, bet"
            xuezhi "Do you have our things prepared?"
            xin "Of course I do"
            jump letsenter
        "Let's go home, this place seems too cursed":
            xin "Let's go home, this place seems too cursed"
            "you guys return back home and play videogames, lame."
            "Lazy Ending"
    return
#------------------------------------------------------------------------------------------------------------------------------------------------------
    label letsenter:
    scene mansion inside
    show xuezhisurprise at left
    xuezhi "this place looks kind of expensive not gonna lie"
    show xinsurprise at right
    xin "I would like to live here to be honest"
    show xuezhismile at left
    xuezhi "this place isn't that scary to me"
    show xinsmile at right
    xin "let's explore around"
    xin "where should we start first?"
    menu:
        "middle door":
            xuezhi "Let's go through middle first"
            jump middledoor
        "Upstairs":
            xuezhi "Let's go upstairs first"
            play sound walkonwood
            jump upstairs
#------------------------------------------------------------------------------------------------------------------------------------------------------
    label middledoor:
        play sound opendoor
        scene mansionliving
        show xinsurprise at right
        xin "Wow, what a livingroom, it is already bigger than my house"
        show xuezhismile at left
        xuezhi "This place is great!"
        play sound doorlock
        show xuezhiquestion at left
        xuezhi "What was that?"
        show xin at right
        xin "Did someone just lock the door?"
        xuezhi "Let me check"
        play sound tryopendoor
        xuezhi "It is locked!"
        xin "what? Is someone tring to joke with us?"
        show xinscare at right
        show xuezhiangry at left
        xuezhi "I'm not sure but we must find someway out this place"
    menu:
        "Search the books":
            xin "This book is kind of weird"
            show xinquestion at right
            xin "*Touches the book*"
            "The roof start to compress on you"
            show xuezhiscare at left
            show xinscare at right
            play sound earthquake
            xuezhi "What is happenning?"
            xin "The roof is compressing at us!"
            xuezhi "What?!"
            "Finally the roof completely compressed on you, you both died"
            "Bad Ending"
            stop sound
            return
        "Search the chimney":
            show xinsurprise at right
            xin "I think I touched something!"
            play sound gearwheel
            xin "I found a secret door to basement here"
            show xuezhi at left
            xuezhi "Let's try going down!"
            jump basement
#------------------------------------------------------------------------------------------------------------------------------------------------------
    label upstairs:
        scene mansionstair
        "......"
        stop sound
        show xuezhiquestion at left
        xuezhi "Haven't we reach yet?"
        show xinquestion at right
        xin "I have a felling of walking on this stair for years already"
        xuezhi "but the second floor seems so close, how are we not up there yet?"
        xin "I don't understand neither"
        xuezhi "let's just keep going I guess"
        hide xuezhiquestion
        hide xinquestion
        play sound walkonwood
        "......"
        stop sound
        show xuezhiscare at left
        xuezhi "How? How are we still not up yet?!"
        show xinscare at right
        xin "I think we are stuck on this stair, it is like a infinite loop of stair, just like the horror movies!"
        xuezhi "Oh man, I'm starting to really getting chills on me"
        xin "Now what we do?"
    menu:
        "Try to find the reason on your phone":
            xuezhi "Let's try to find out the reason on the phone"
            show xuezhiquestion at left
            xuezhi "It says that the loop is caused because a invisible ghost is blocking the way"
            xuezhi "If we open the camara, we may saw he through the phone and escape from he"
            xuezhi "All what we need to do is not touch the ghost or we are gonna be sent back again in the loop"
            show xuezhiangry at left
            xuezhi "Let's do this!"
            xin "Okay, so lets see where is the ghost"
            hide xuezhiangry
            hide xinscare
            show phone
            "......"
            jump gosecondfloor
        "Run to downstair":
            "Running back to downstair didn't work for you and you guys died because of hungry and thirsty after 1 week stuck on the stairs"
            "Bad Ending"
    return
#------------------------------------------------------------------------------------------------------------------------------------------------------
    label gosecondfloor:
        scene stairghost
        hide phone
        "       "
        show xuezhiscare at left
        show xinscare at right
        "......"
        xin"On 3 we run okay?"
        xuezhi"Okay"
        xin"1"
        xuezhi"2"
        xin"3!"
        play sound runonwood
        xuezhi "Be careful! she is starting to chase us"
        play sound ghostscream
        xin "Run faster!"
        play sound runonwood
        xuezhi"Look, there is a open room, let's get in there!"
        jump hallway
#------------------------------------------------------------------------------------------------------------------------------------------------------
label basement:
    return
#------------------------------------------------------------------------------------------------------------------------------------------------------
label hallway:
    scene hallway
    play sound runonwood
    show xuezhiscare at left
    show xinscare at right
    xin "She is so close to me right now!"
    xuezhi "Come on xin, only a bit more!"
    play sound closedoor
    jump room
#------------------------------------------------------------------------------------------------------------------------------------------------------
label room:
    scene room
    show xuezhiscare at left
    xuezhi "Uffff, we finally reach in time, did you closed the door?"
    show xinscare at right
    xin "I'm using all my strength to close it and not letting it go, I don't know if she is gonna push the door"
    return
