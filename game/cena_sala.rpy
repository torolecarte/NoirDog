label sala_inicio:
    "{cps=25}{i}{alpha=.5}Mais um dia agradável.{/alpha}{/i}{/cps}"
    
    scene bg_sala_real

    "{i}{alpha=.5}Nada como viver sob a segurança de portões resistentes, almofadas macias e um Chefe vigilante.{/alpha}{/i}"
    "{i}{alpha=.5}Acredito que seus olhos podem ver até mesmo o destino das coisas.{p}Falando nele, sinto seu cheiro ficando mais forte.{/alpha}{/i}"   
    
    c_billy "yada yada yada yada yada BOLINHA yada."
    
    hide dono_play with dissolve

    "{i}{alpha=.5}Estranho, ainda não terminei o descanso do primeiro treino. E o Chefe já tem mais um exercício planejado.{/alpha}{/i}"
    "{i}{alpha=.5}Se ele acha mesmo necessário, então eu também acho.{/alpha}{/i}"
    
    c_caramelo "A caminho, Chefe."

    jump quintal_colorido


label sala_noir:
    scene bg_sala_noir with dissolve

    c_caramelo "Meu deus, o que houve aqui?" 

##Clique no vaso quebrado
    "{i}{alpha=.5}Estranho, isto é um dos meus alvos de prática. Mas já estava assim antes?{w} Não, eu estava cansado demais para treinar dentro de casa, alguma coisa o quebrou.{/alpha}{/i}"

##Clique em uma parte escura
    "{i}{alpha=.5}Está escuro aqui. Por que impediram o Sol de entrar? Algo não cheira bem.{/alpha}{/i}"
    
##Clique na porta
    c_caramelo "Chefe!?"
    "{i}{alpha=.5}Ele não parece estar aqui, mas então onde estaria?{/alpha}{/i}"

##após os 3 cliques=    
    "{i}{alpha=.5}Isso não parece bom. Escureceram meu quarto, quebraram um dos meus alvos, talvez em alguma luta, e o Chefe não está em lugar algum...{/alpha}{/i}"
    c_caramelo "Havia alguém na porta!"

##clique janela(???)
    jump sala_noir_janela


label sala_noir_janela:
    scene bg_janela with dissolve

    c_caramelo "{cps=15}Não.{/cps}"
    scene cs_porta_malas with dissolve
##Silhueta com rabo de cavalo joga algo no porta malas de um carro
    c_caramelo "{cps=30}NÃO!{/cps}"
    scene cs_entra_carro with dissolve
##Rabo de Cavalo” entra no carro
    "{i}{alpha=.5}Isso não pode estar acontecendo, me descuidei demais.{/alpha}{/i}"
    scene cs_carro_acelera with dissolve
##Carro acelera e sai de cena   
    c_caramelo "CHEFE!!!"

    scene cs_foco_luz with dissolve
    pause

##Cena da bolinha caindo
    "{i}{alpha=.5}De’Loco estava certo.{w}{nw}{/alpha}{/i}"

    scene cs_foco_bolinha with dissolve
    "{i}{alpha=.5}...era tarde demais...{/alpha}{/i}"
##Bolinha no chão-luz foco com corte das persianas na bolinha
    scene bg_black with dissolve
    "{i}{alpha=.5}{cps=15}Eu estava atrasado...{/cps}{/alpha}{/i}"

##fadeout pra tela preta
    "{b}Continua...{/b}"    

    jump end
