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

    c_caramelo "Meu deus, o que houve aqui?" 

##Clique no vaso quebrado
    "{i}{alpha=.5}Estranho, isto é um dos meus alvos de prática. Mas já estava assim antes? Não, eu estava cansado demais para treinar dentro de casa, alguma outra pessoa o quebrou.{/alpha}{/i}"

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
    scene bg_sala_noir with dissolve

    c_caramelo "Não."
##Silhueta com rabo de cavalo joga algo no porta malas de um carro
    c_caramelo "NÃO!"
##Rabo de Cavalo” entra no carro
    "{i}{alpha=.5}Isso não pode estar acontecendo, me descuidei demais.{/alpha}{/i}"
##Carro acelera e sai de cena   
    c_caramelo "CHEFE!!!"

##Cena da bolinha caindo
    "{i}{alpha=.5}De’Loco estava certo. Era tarde demais…{/alpha}{/i}"
##Bolinha no chão-luz foco com corte das persianas na bolinha
    "{i}{alpha=.5}Eu estava atrasado...{/alpha}{/i}"

##fadeout pra tela preta
    "Continua..."    

    jump end
