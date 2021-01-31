##Personagens c_

define fdp = Character('')
define c_caramelo = Character('Noir', window_background="gui/textbox.png")
define c_billy = Character('Billie De\'Loco', window_background="gui/textbox.png")
define c_dono = Character('Chefe', window_background="gui/textbox.png")
define c_random = Character('???', window_background="gui/textbox.png")

## "{i}{alpha=.5}{/alpha}{/i}"
#--------------------------------
label start:
    #jump quintal_vizinho
    jump sala_inicio

label end:
    return