##Personagens c_

define fdp = Character('', window_background=None)
define c_caramelo = Character('Noir')
define c_billy = Character('Billie De\'Loco')
define c_dono = Character('Chefe')
define c_random = Character('???')

image caramelo_serio_flipped = im.Flip("caramelo_serio.png", horizontal=True)
image caramelo_noir_flipped = im.Flip("caramelo_noir.png", horizontal=True)
image caramelo_noir_surpreso_flipped = im.Flip("caramelo_surpreso.png", horizontal=True)
image caramelo_noir_brabo_flipped = im.Flip("caramelo_noir_brabo.png", horizontal=True)
image caramelo_noir_confiante_flipped = im.Flip("caramelo_noir_confiante.png", horizontal=True)
image caramelo_noir_medo_flipped = im.Flip("caramelo_noir_medo.png", horizontal=True)

## "{i}{alpha=.5}{/alpha}{/i}"
#--------------------------------
label start:
    #jump quintal_vizinho
    jump sala_inicio

label end:
    return