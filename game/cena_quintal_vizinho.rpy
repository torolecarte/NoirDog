define invest_papagaio = False
define invest_bolinha = False
define invest_semente_girassol = False
define cena_entrada = True

image sprite_billie_acordado = "sprite billie acordado.png"

screen investigacao_quintal_vizinho():
        imagemap:
            idle "bg_billy_noir.png"
            hover "bg_billy_noir.png"
            ground "bg_billy_noir.png"
        
            hotspot(65, 375, 197, 172) action Jump("invest_papagaio")
            hotspot(419, 572, 51, 53) action Jump("invest_bolinha")
            hotspot(764, 547, 98, 71) action Jump("invest_semente_girassol")
            hotspot(1178, 516, 57, 42) action Jump("invest_semente_girassol")
            hotspot(71, 614, 52, 30) action Jump("invest_semente_girassol")

label quintal_vizinho:
    scene bg_billy_noir with dissolve

    if invest_papagaio and invest_bolinha and invest_semente_girassol:
        show caramelo_noir at right with dissolve
        show sprite sonolento at left with dissolve
        "{i}{alpha=.5}Se meu instinto estiver correto, eu só preciso esperar um pou{cps=15}co...{/cps}{/alpha}{/i}"
        hide sprite sonolento with dissolve
        show sprite billie dormindo at left with dissolve
        "{i}{alpha=.5}Como previsto, ele pode ser louco, mas o peso da comida tem sempre o mesmo resultado.{p} Sono.{/alpha}{/i}"
        "{i}{alpha=.5}Muito bem, agora posso executar o plano, preciso apenas me esquivar das sementes.{p} {cps=20}Serei sorrateiro como o silêncio.{/cps}{/alpha}{/i}"
        hide sprite billie dormindo
        hide caramelo_noir
        menu:
            "Executar plano":
                show caramelo_noir_confiante at left with dissolve
                c_caramelo "Bingo! Missão cumprida."
                "{i}{alpha=.5}Se isto fazia parte de seu treino, Chefe. Considere feito.{/alpha}{/i}"
                hide caramelo_noir_confiante
                jump quintal_vizinho_plano

    if cena_entrada:
        show caramelo_noir at right with dissolve
        c_caramelo "E eu tenho instintos demais para meu próprio bem...{w} De'Loco."
        $ cena_entrada = False
        hide caramelo_noir with dissolve

    call screen investigacao_quintal_vizinho


##-----

label invest_papagaio:    
    $ invest_papagaio = True
    show caramelo_noir at right with dissolve
    "{i}{alpha=.5}{cps=25}Pobre coitado,{/cps}{w} o mundo externo é feito de dor e sofrimento, e este animal conhece os dois intimamente.{/alpha}{/i}"
    "{i}{alpha=.5}Nem quero imaginar o que acontece por aqui, apenas os gritos constantes, cantorias estranhas e palavras sem sentido são suficientes para alimentar meus pesadelos.{/alpha}{/i}"
    "{i}{alpha=.5}Não sei o que tenha deixado ele assim,{w} mas seja o que for,{w}{cps=20} jamais quero encontrar.{/cps}{/alpha}{/i}"

    jump quintal_vizinho


label invest_bolinha:
    $ invest_bolinha = True    
    show caramelo_noir at right with dissolve
    "{i}{alpha=.5}Lá está,{w} brilhante como sempre, sua cor única me hipnotiza. Logo te salvarei, apenas preciso de um plano.{/alpha}{/i}"

    jump quintal_vizinho


label invest_semente_girassol:
    $ invest_semente_girassol = True
    show caramelo_noir at right with dissolve
    "{i}{alpha=.5}{cps=25}Sementes por todos os lados.{/cps}{w} Isso pode ser um problema,{w} mas por outro lado, Billie acabou de se alimentar.{/alpha}{/i}"    

    jump quintal_vizinho


label quintal_vizinho_plano:
    show caramelo_surpreso at left
    play sound "sounds/beeh-simples.mp3" #Som: Barulho da campainha
    "{i}{alpha=.5}Eu conheço esse som. É a entrada.{p} Deixei a casa desprotegida. Preciso voltar!{/alpha}{/i}"
        
    ##pisa nas sementes e o papagaio acorda
    c_caramelo "Mas qu{cps=5}e...{/cps}"
    
    
    play sound "sounds/beeh-simples.mp3" #Som: Barulho pisando nas sementes
    
    show foco pisada girassol at truecenter with moveinbottom
    pause 0.5
    c_billy "atrasaa{size=+5}A{/size}{size=+10}A{/size}{size=+15}R{/size}{size=+20}RR{/size}{size=+25}R{/size}{size=+30}GHHH!{/size} Atrasado! Yada! Yada!{size=40} Atrasado!{/size} Yada! Sementes! {size=30}Cão!{/size} Yada! Yada!"
    hide foco pisada girassol with dissolve
    hide caramelo_surpreso
    show caramelo_noir_brabo at left
    show sprite_billie_acordado at center with moveinleft

    "{i}{alpha=.5}Não tenho tempo para você, Billie.{w} Há alguém na casa!{/alpha}{/i}"

    #show sprite billie acordado at center with moveinleft
    show sprite_billie_acordado:
        choice:
            linear 0.5 xalign 0.1
        choice:
            linear 0.5 xalign 0.9
        choice:
            linear 0.5 xalign 0.5
        repeat

    c_caramelo "Saia da minha frente!"
    c_billy "Yada! Cão! Cão! Atrasado! Yada, Yada!"
    "{i}{alpha=.5}Ele é insano, fala como um dos humanos.{/alpha}{/i}"
    c_caramelo "Saia da frente!"
    
    show sprite_billie_acordado at center with move
    show caramelo_noir_brabo at center with move
    show bg_billy_noir 
    show sprite_billie_acordado at center
    with hpunch
    play sound "sounds/punch.opus"
    show caramelo_noir_brabo at left with move
    show sprite_billie_acordado at right with move
    c_caramelo "Você é louco!"
   

    c_billy "Yada! Yada! Yada! Yada! Yada!"
    
    jump quintal_noir