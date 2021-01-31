define encontrou_passagem = False

screen investigacao_quintal_noir():
        imagemap:
            idle "bg_quintal_noir.png"
            hover "bg_quintal_noir.png"
            ground "bg_quintal_noir.png"
        
            hotspot(370, 318, 908, 176) action Jump("quintal_noir_pularcerca")
            hotspot(0, 316, 359, 81) action Jump("quintal_noir_pularcerca")
            hotspot(14, 394, 350, 121) action Jump("quintal_noir_passagem")

label quintal_colorido:

    scene bg_quintal_real with pushright
    show caramelo_alegre at left with moveinright
    show chefe_bolinha at right with moveinright
    c_caramelo "Estou preparado.{p}{i}{alpha=.5}{cps=25}E sempre estarei.{/cps}{/alpha}{/i}"
    
    "{i}{alpha=.5}Apesar do esforço, sou grato pelos treinos do Chefe.{p}{cps=25}Um humano sábio.{/cps}{/alpha}{/i}"
    "{i}{alpha=.5}Mesmo com a companhia um do outro e seguros, ele se prepara para o pior.{p}Eu concordo com você, Chefe.{/alpha}{/i}"
    "{i}{alpha=.5}É sempre bom estar pronto para enfrentar o caos do mundo.{/alpha}{/i}"
    show caramelo_curioso at left
    c_random "{size=-5}Yada, yada. Comida. Yada. Comida. Yada, yada.{/size}"
    "{i}{alpha=.5}Ignore ele, ignore ele. Você tem um trabalho a fazer, foque.{/alpha}{/i}"
    hide caramelo_curioso
    c_caramelo "Em posição! Pode lançar."
    show chefe_fone at right
    hide chefe_bolinha
    show caramelo_curioso at left
    c_dono "yada. yada yada yada."    
    "{i}{alpha=.5}O chefe está falando algo com o bloco de sons. Boas informações são realmente indispensáveis.{/alpha}{/i}"
    c_dono "yada yada yada...{w}{nw}"
    show chefe_jogando at right
    hide chefe_fone
    hide caramelo_curioso
    extend "{size=50} YADA?!{/size}"
    hide chefe_jogando with moveoutright
    hide caramelo_curioso
    "{i}{alpha=.5}Este é o sinal! Eu pego, eu pego.{/alpha}{/i}"
    c_random "{size=-5}YADA! YADA! Comida! Yada! Atrasado! Yada!{/size}"
    show caramelo_serio_flipped at left
    hide caramelo_alegre
    "{i}{alpha=.5}{cps=15}Eu nã{/cps}{cps=5}o...{/cps}{w} N-{w}{cps=50}não consigo encontrá-la!{/cps}{/alpha}{/i}"
    "{i}{alpha=.5}Acho que o equipamento não está na área de treino... deve ter saído de nosso território.{/alpha}{/i}"
    "{i}{alpha=.5}Ainda sinto seu cheiro, ela está nos arredores, será que...{w} De'Loco.{/alpha}{/i}"
    c_billy "Yada! {size=30}Fiuuuuuiiii!{/size} Comida. {size=-5}Yum, yada, yum.{/size}"
    hide caramelo_serio_flipped with dissolve
    "{i}{alpha=.5}Preciso encontrar uma forma de confirmar minhas suspeitas...{/alpha}{/i}"
    show caramelo_serio_flipped at left with dissolve
    "{i}{alpha=.5}{cps=25}...deve haver algum jeito.{/cps}{/alpha}{/i}"
    show caramelo_serio_flipped at center with MoveTransition(1.2)
    c_caramelo "Posso ser um cachorro comum... mas sou um cachorro comum com instintos!"
    hide caramelo_noir with dissolve
    jump quintal_noir

label quintal_noir:
    
    
    if not encontrou_passagem:
        scene bg_quintal_noir with dissolve
        call screen investigacao_quintal_noir
    
    scene bg_quintal_noir_buraco with dissolve
    show caramelo_noir_flipped at left with moveinbottom
    "{i}{alpha=.5}Consegui, essa foi por um pêlo.{/alpha}{/i}"
    play sound "sounds/vaso.wav" volume 0.2 #Som: Som vaso quebrado
    c_caramelo "Chefe, tem alguém na entrada, fique atrás de mim!"
    hide caramelo_noir_flipped
    show caramelo_noir_surpreso_flipped at left      
    
    ##hide caramelo_noir_flipped
    c_caramelo "{cps=25} ...Chefe?{/cps}"
    c_billy "{size=-5}Yada, yada, NOIR. Yada!{/size}"            
    

    play sound "sounds/porta.mp3" volume 0.1
    pause 1
    play sound "sounds/tranca.mp3" volume 0.1
    c_caramelo "Chefe, o que houve?! Estou indo!"
    hide caramelo_noir_surpreso_flipped with moveoutright
    jump sala_noir


label quintal_noir_pularcerca:
    show caramelo_noir at right with dissolve
    "{i}{alpha=.5}Mesmo com meu treino, acho que não seria capaz de pular essa barreira.{p}E mesmo que fosse, quem sabe o que me espera do outro lado?{/alpha}{/i}"

    jump quintal_noir
    

label quintal_noir_passagem:
    show caramelo_noir at right with dissolve
    "{i}{alpha=.5}Deve ter  algo escondido  que me a{cps=25}jude a …{/cps}{/alpha}{i}"
    play sound "sounds/folhas.wav"  ##barulho de arbusto
    
    scene bg_quintal_noir_buraco with dissolve
    show caramelo_noir_confiante at right with dissolve
    c_caramelo "{size=+10}Bingo!{/size}{w} É como eu sempre digo, instintos é que fazem o cão."
    $ encontrou_passagem = True    

    jump quintal_vizinho