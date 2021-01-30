##Personagens c_

define c_caramelo = Character('Caramelo')

define c_billy = Character('Billy')

define c_dono = Character('Chefe')

define c_random = Character('???')

##Imagens


##Backgorunds bg_
#image bg_sala_real = "bg_sala_real.jpg"
#image bg_sala_noir = "bg_sala_noir.jpg"
#image bg_quintal_real = "bg_quintal_real.jpg"
#image bg_quintal_noir = "bg_quintal_noir.jpg"
#image bg_billy_noir = "bg_billy_noir.jpg"

##Audio s_ m_

## "{i}{alpha=.5}{/alpha}{/i}"
#--------------------------------
label start:
    #jump quintal_vizinho
    jump sala_inicio

label end:
    return