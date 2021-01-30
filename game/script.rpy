##Personagens c_

define c_caramelo = Character('Caramelo')
image caramelo_de_boa = "caramelo_de_boa.png"
image caramelo_bolado = "caramelo_bolado.png"
image caramelo_detetive = "caramelo_detetive.png"

define c_billy = Character('Billy')

define c_dono = Character('Dono')
image dono_play = "dono_play.webp"
image dono_troll = "dono_troll.jpg"

define c_random = Character('???')
##add
image bolinha = "bolinha.png"


##Backgorunds bg_
image bg_sala_real = "bg_sala_real.jpg"
image bg_sala_noir = "bg_sala_noir.jpg"
image bg_quintal_real = "bg_quintal_real.jpg"
image bg_quintal_noir = "bg_quintal_noir.jpg"
image bg_billy_noir = "bg_billy_noir.jpg"

##Audio s_ m_


#--------------------------------
label start:
    "{cps=25}{i}{alpha=.5}Mais um dia agradável.{/alpha}{/i}{/cps}"
    scene bg_sala_real
    show caramelo_de_boa:
        xalign 0.0
        yalign 1.0
    "{i}{alpha=.5}Nada como viver sob a segurança de portões resistentes, almofadas macias e um Chefe vigilante.{/alpha}{/i}"
    "{i}{alpha=.5}Eu posso jurar que em seus olhos ele pode até mesmo ver o destino das coisas.{p}Falando nele, sinto o cheiro ficando mais forte.{/alpha}{/i}"   
    show dono_play with moveinleft:
        xalign 1.0
        yalign 1.0
    c_dono "yada yada yada yada yada BOLINHA yada."
    hide dono_play with dissolve
    "{i}{alpha=.5}Estranho, ainda não terminei o descanso do primeiro treino. E o Chefe já tem mais um exercício planejado.{/alpha}{/i}"
    "{i}{alpha=.5}Se ele acha mesmo necessário, eu é que não negarei.{/alpha}{/i}"
    c_caramelo "A caminho, Chefe."

    scene bg_quintal_real with dissolve
    pause 1
    show caramelo_de_boa with moveinleft:
        xalign 0.0
        yalign 1.0
    c_caramelo "Estou preparado.{p}{i}{alpha=.5}E sempre estarei.{/alpha}{/i}"
    "{i}{alpha=.5}Apesar do esforço, sou grato pelos treinos do Chefe.{p}Um homem sábio.{/alpha}{/i}"
    "{i}{alpha=.5}Mesmo na companhia um do outro e seguros, ele pensa no pior.{p}Eu concordo com você, Chefe.{/alpha}{/i}"
    show dono_troll with moveinleft:
        xalign 1.0
        yalign 1.0
    pause
    show bolinha with moveinbottom:
        xalign 0.5
        yalign -5.0
    scene bg_quintal_real with dissolve
#####texto encaixado daqui pra baixo é 200% zuera (antes disso era apenas 90%zueira)
    show caramelo_bolado with moveinbottom:
        xalign 0.0
        yalign 1.0
    c_caramelo "Carai patrão, isolou a bolinha"
    c_caramelo "vou virar detetive entaum"
    scene bg_quintal_noir with dissolve
    show caramelo_detetive with dissolve:
        xalign 0.0
        yalign 1.0
##AQUI COMEÇA O POINT'N CLICK DE INVESTIGAÇÃO - preciso de ajuda HEITOOOOOOR
label cerca:
    scene bg_quintal_noir
    show caramelo_detetive:
        xalign 0.0
        yalign 1.0
menu:
    "pular cerca":
        jump nop
    
    "passar pelo buraco na cerca":
        jump papagaio

label nop:
    c_caramelo "num rola, muito alto"
    jump cerca
    

label papagaio:
    c_caramelo "lol! um buracao na cerca, voentra!!"
    scene bg_billy_noir with dissolve
    pause