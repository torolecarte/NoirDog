label sala_inicio:
    "{cps=25}{i}{alpha=.5}Mais um dia agradável.{/alpha}{/i}{/cps}"
    
    scene bg_sala_real

    "{i}{alpha=.5}Nada como viver sob a segurança de portões resistentes, almofadas macias e um Chefe vigilante.{/alpha}{/i}"
    "{i}{alpha=.5}Eu posso jurar que em seus olhos ele pode até mesmo ver o destino das coisas.{p}Falando nele, sinto o cheiro ficando mais forte.{/alpha}{/i}"   
    
    c_billy "yada yada yada yada yada BOLINHA yada."
    
    hide dono_play with dissolve

    "{i}{alpha=.5}Estranho, ainda não terminei o descanso do primeiro treino. E o Chefe já tem mais um exercício planejado.{/alpha}{/i}"
    "{i}{alpha=.5}Se ele acha mesmo necessário, eu é que não negarei.{/alpha}{/i}"
    
    c_caramelo "A caminho, Chefe."

    jump quintal_colorido


label sala_noir:
    scene bg_sala_noir with dissolve

    "Placeholder" "Entra cena da sala noir com vaso quebrado"

    play sound "sounds/beeh-simples.mp3" #Som: Porta batendo

    jump sala_noir_janela


label sala_noir_janela:
    scene bg_sala_noir with dissolve

    "Placeholder" "Entra cena olhando pela janela"

    play sound "sounds/beeh-simples.mp3" #Som: Porta mala batendo

    jump end
