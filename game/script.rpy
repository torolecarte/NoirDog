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
image chefe_bolinha_flipped = im.Flip("chefe_bolinha.png", horizontal=True)
image caramelo_medo_persiana_flipped = im.Flip("caramelo_medo_persiana.png", horizontal=True)
image caramelo_surpreso_persiana_flipped = im.Flip("caramelo_surpreso_persiana.png", horizontal=True)
image caramelo_curioso_flipped = im.Flip("caramelo_curioso.png", horizontal=True)
image caramelo_alegre_flipped = im.Flip("caramelo_alegre.png", horizontal=True)


#
#
#
#
#
#

#
#
#
#
#
#

#--------------------------------
label start:
    #jump quintal_vizinho
    jump sala_inicio

label end:
    return