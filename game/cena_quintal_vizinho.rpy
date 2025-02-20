define invest_papagaio = False
define invest_bolinha = False
define invest_semente_girassol = False
define cena_entrada = True

image sprite_billie_acordado = "sprite billie acordado.png"

screen investigacao_quintal_vizinho():
        imagemap:
            idle "bg_billie_acordado.png"
            hover "bg_billie_acordado.png"
            ground "bg_billie_acordado.png"
        
            hotspot(65, 375, 197, 172) action Jump("invest_papagaio")
            hotspot(419, 572, 51, 53) action Jump("invest_bolinha")
            hotspot(764, 547, 98, 71) action Jump("invest_semente_girassol")
            hotspot(1178, 516, 57, 42) action Jump("invest_semente_girassol")
            hotspot(71, 614, 52, 30) action Jump("invest_semente_girassol")

label quintal_vizinho:
    scene bg_billie_acordado with dissolve

    if invest_papagaio and invest_bolinha and invest_semente_girassol:
        show caramelo_noir at right with dissolve
        
        "{i}{alpha=.5}Se meu instinto estiver correto, eu só preciso esperar um pou{cps=15}co...{/cps}{/alpha}{/i}"
        scene bg_billie_dormindo
        show caramelo_noir at right
        "{i}{alpha=.5}Como previsto, ele pode ser louco, mas o peso da comida tem sempre o mesmo resultado.{p} Sono.{/alpha}{/i}"
        "{i}{alpha=.5}Muito bem, agora posso executar o plano, preciso apenas me esquivar das sementes.{p} {cps=20}Serei sorrateiro como o silêncio.{/cps}{/alpha}{/i}"
        
        hide caramelo_noir
        menu:
            "Executar plano":
                scene bg_billie_dsb with dissolve
                show caramelo_noir_confiante_flipped at left with dissolve
                c_caramelo "Bingo! Missão cumprida."
                "{i}{alpha=.5}Se isto fazia parte de seu treino, Chefe. Considere feito.{/alpha}{/i}"
                hide caramelo_noir_confiante_flipped
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
    show caramelo_noir_surpreso_flipped at left
    play sound "sounds/campainha.mp3" volume 0.1
    "{i}{alpha=.5}Eu conheço esse som. É a entrada.{p} Deixei a casa desprotegida. Preciso voltar!{/alpha}{/i}"
    
    ##pisa nas sementes e o papagaio acorda
    c_caramelo "Mas qu{cps=5}e...{/cps}"
    
    scene bg_billie_sem_bola
    show caramelo_noir_surpreso_flipped at left 
    play sound "sounds/sementes.wav" volume 0.7 
    show foco pisada girassol at truecenter with moveinbottom
    
    pause 0.5

    play sound ("sounds/papagaio1.mp3")
    pause 1
    play sound ("sounds/papagaio1.mp3")
    
    
    
    c_billy "atrasaa{size=+5}A{/size}{size=+10}A{/size}{size=+15}R{/size}{size=+20}RR{/size}{size=+25}R{/size}{size=+30}GHHH!{/size} Atrasado! Yada! Yada!{size=40} Atrasado!{/size} Yada! Sementes! {size=30}Cão!{/size} Yada! Yada!"
    play sound ("sounds/papagaio1.mp3")
    hide foco pisada girassol with dissolve
    hide caramelo_noir_surpreso_flipped
    show caramelo_noir_brabo_flipped at left
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
    play sound ("sounds/papagaio1.mp3")
    pause 1
    "{i}{alpha=.5}Ele é insano, fala como um dos humanos.{/alpha}{/i}"
    play sound ("sounds/papagaio1.mp3")
    pause 1
    play sound ("sounds/papagaio1.mp3")
    c_billy "Yada! Cão! Cão! Atrasado! Yada, Yada!"
    "{i}{alpha=.5}Ele é insano, fala como um dos humanos.{/alpha}{/i}"
    c_caramelo "Saia da frente!"
    
    show sprite_billie_acordado at center with move
    show caramelo_noir_brabo_flipped at center with move
    show bg_billie_sem_bola 
    show sprite_billie_acordado at center
    with hpunch
    
    play sound "sounds/punch.opus" volume 0.5
    show caramelo_noir_brabo_flipped at left with move
    show sprite_billie_acordado at right with move
    c_caramelo "Você é louco!"
   

    c_billy "Yada! Yada! Yada! Yada! Yada!"
    
    jump quintal_noir