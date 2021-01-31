define invest_escuro = False
define invest_vaso = False
define invest_porta = False
define cena_entrada_noir = True

screen investigacao_sala_noir():
        imagemap:
            idle "bg_sala_noir.png"
            hover "bg_sala_noir.png"
            ground "bg_sala_noir.png"
        
            hotspot(0, 0, 1280, 69) action Jump("sala_noir_invest_escuro")
            hotspot(2, 602, 83, 116) action Jump("sala_noir_invest_escuro")
            hotspot(1168, 600, 109, 119) action Jump("sala_noir_invest_escuro")
            hotspot(1, 60, 260, 87) action Jump("sala_noir_invest_escuro")

            hotspot(620, 413, 129, 59) action Jump("sala_noir_invest_vaso")
                      
            hotspot(771, 168, 114, 231) action Jump("sala_noir_invest_porta")

screen investigacao_sala_noir_final():
        imagemap:
            idle "bg_sala_noir.png"
            hover "bg_sala_noir.png"
            ground "bg_sala_noir.png"

            hotspot(1081, 86, 169, 268) action Jump("sala_noir_invest_janela")


label sala_inicio:
    "{cps=25}{i}{alpha=.5}Mais um dia agradável.{/alpha}{/i}{/cps}"
    
    scene bg_sala_real

    "{i}{alpha=.5}Nada como viver sob a segurança de portões resistentes, almofadas macias e um Chefe vigilante.{/alpha}{/i}"
    "{i}{alpha=.5}Acredito que seus olhos podem ver até mesmo o destino das coisas.{p}Falando nele, sinto seu cheiro ficando mais forte.{/alpha}{/i}"   
    
    c_dono "yada yada NOIR yada yada BOLINHA yada."
    
    hide dono_play with dissolve

    "{i}{alpha=.5}Estranho, sequer terminei o descanso do primeiro treino e o Chefe já tem mais um exercício planejado.{/alpha}{/i}"
    "{i}{alpha=.5}Mas se ele acha mesmo necessário, então eu também acho.{/alpha}{/i}"
    
    c_caramelo "A caminho, Chefe."

    jump quintal_colorido


label sala_noir:
    scene bg_sala_noir with dissolve
    
    if cena_entrada_noir:
        $ cena_entrada_noir = False
        c_caramelo "Meu deus, o que houve aqui?"

    if not invest_porta or not invest_vaso or not invest_escuro:
        call screen investigacao_sala_noir

    ##após os 3 cliques
    "{i}{alpha=.5}Isso não parece bom. Escureceram meu quarto, quebraram um dos meus alvos, talvez em alguma luta, e o Chefe não está em lugar algum...{/alpha}{/i}"
    c_caramelo "Havia alguém na porta!{p}{i}{alpha=.5}{cps=30}Preciso checar na janela.{/cps}{/alpha}{/i}"

    call screen investigacao_sala_noir_final


label sala_noir_invest_vaso:
    $ invest_vaso = True
    "{i}{alpha=.5}Estranho, isto é um dos meus alvos de prática. Mas já estava assim antes?{w} Não, eu estava cansado demais para treinar dentro de casa, alguma coisa o quebrou.{/alpha}{/i}"
    jump sala_noir

label sala_noir_invest_escuro:
    $ invest_escuro = True
    "{i}{alpha=.5}Está escuro aqui. Por que impediram o Sol de entrar? Algo não cheira bem.{/alpha}{/i}"
    jump sala_noir
    
label sala_noir_invest_porta:
    $ invest_porta = True
    c_caramelo "Chefe!?"
    "{i}{alpha=.5}Ele não parece estar aqui, mas então onde estaria?{/alpha}{/i}"
    jump sala_noir


label sala_noir_invest_janela:
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
    c_caramelo "{size=50}CHEFE!!!{/size}"

    scene cs_foco_luz with dissolve
    pause

##Cena da bolinha caindo
    "{i}{alpha=.5}De’Loco estava certo.{/alpha}{/i}"

    scene cs_foco_bolinha
    "{i}{alpha=.5}{cps=25}Era tarde demais...{/cps}{/alpha}{/i}"
##Bolinha no chão-luz foco com corte das persianas na bolinha
    scene bg_black with dissolve
    "{i}{alpha=.5}{cps=15}Eu estava atrasado...{/cps}{/alpha}{/i}"

##fadeout pra tela preta
    "{b}{vspace=50}{space=830}Continua...{/b}"    

    jump end
