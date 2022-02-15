label start:
    play music pianolofi
    scene mansion
    "this is a story about two teenagers and the mansion, it contains some horror scenes, Are you sure to continue?"
    menu:
        "yes":
            jump school

        "no":
            "you didn't even start the story"
            "Lazy Ending"
            return
label school:
    scene school
    show xuezhi at left
    xuezhi "good morning xin"
    show xin at right
    xin "Good morning xuezhi"
    xuezhi "What idea you got for the new video of youtube"
    xin "I've heard about they were talking about a haunted house near us"
    xuezhi "Is the one that I know?"
    show teacherangry
    "teacher""Go to classroom"
    menu:
        "Go to classroom":
            jump classroom
        "Stay to talk":
            "teacher""I will call your mom"
            hide xin
            hide xuezhi
            show xuezhismile at left
            show xinsmile at right
            play sound emotional
            xin "Emotional damage!"
            xuezhi "Emotional damage!"
            hide teacher
            show teajesus
            play sound jesus
            "teacher""I will send you to Jesus!"
            "the teacher called your mom and your mom send you to jesus"
            "Good Ending"
            return
label classroom:
    scene classroom
    show teacherangry
    "teacher" "Next time I won't not let you guys enter"
    hide teacherangry
    show xin at right
    xin "That was kind of scary, isn't it"
    show xuezhi at left
    xuezhi "Yeah, so it was the one that i know?"
    xin "I think so"
    hide xuezhi
    show xuezhismile at left
    xuezhi "So do we go after school?!"
    hide xuezhismile
    show xuezhi at left
    xin "Do we?!, I'm kind of scared..."
    menu:
        "Go to haunted house":
            jump mansion
            scene mansion
            pause
        "No, im scared":
            "Why yo so coward?"
            "Coward Ending"
            return
