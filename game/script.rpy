##Personagens c_

define c_caramelo = Character('Caramelo')

define c_billy = Character('Billy')

define c_dono = Character('Chefe')

define c_random = Character('???')

##Imagens


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
    "{i}{alpha=.5}Nada como viver sob a segurança de portões resistentes, almofadas macias e um Chefe vigilante.{/alpha}{/i}"
    "{i}{alpha=.5}Eu posso jurar que em seus olhos ele pode até mesmo ver o destino das coisas.{p}Falando nele, sinto o cheiro ficando mais forte.{/alpha}{/i}"   
    c_dono "yada yada yada yada yada BOLINHA yada."
    hide dono_play with dissolve
    "{i}{alpha=.5}Estranho, ainda não terminei o descanso do primeiro treino. E o Chefe já tem mais um exercício planejado.{/alpha}{/i}"
    "{i}{alpha=.5}Se ele acha mesmo necessário, eu é que não negarei.{/alpha}{/i}"
    c_caramelo "A caminho, Chefe."

    scene bg_quintal_real with dissolve
    c_caramelo "Estou preparado.{p}{i}{alpha=.5}E sempre estarei.{/alpha}{/i}"
    "{i}{alpha=.5}Apesar do esforço, sou grato pelos treinos do Chefe.{p}Um homem sábio.{/alpha}{/i}"
    "{i}{alpha=.5}Mesmo na companhia um do outro e seguros, ele pensa no pior.{p}Eu concordo com você, Chefe.{/alpha}{/i}"
    scene bg_quintal_noir with dissolve

label cerca:
    scene bg_quintal_noir
    
menu:
    "pular cerca":
        jump nop
    
    "moita":
        jump papagaio

label nop:

    jump cerca
    

label papagaio:
    scene bg_billy_noir with dissolve
    pause