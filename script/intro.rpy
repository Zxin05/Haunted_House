image black = "#000"
image white = "#ffffff"
image logo = "logo.png"

transform transform_logo:
    on show:
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

transform transform_white:
    on show:
        alpha 0
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

label splashscreen:
    scene black
    $ renpy.pause(1, hard=True)
    show white at transform_white
    $ renpy.pause(2, hard=True)

    show logo at transform_logo
    $ renpy.pause(6, hard=True)

    hide logo
    $ renpy.pause(2, hard=True)

    hide white
    $ renpy.pause(3, hard=True)

    return

#label opening:
    #$ renpy.movie_cutscene('opening.ogv')
    #jump before_main_menu

transform transform_blink:
    linear 1.0 alpha 0.2
    linear 1.0 alpha 1.0
    repeat

#screen press_to_start():
    #tag menu
    #add "background"

    #add "press_to_start.png" xalign 0.5 yalign 0.5 at transform_blink

    #imagemap:
        #ground "transparent.png"
        #hotspot (0, 0,1920, 1080) focus_mask None action Show("main_menu", transition=dissolve)

    #timer 50 action Jump("opening")

#label before_main_menu:
    #call screen press_to_start
