define encontrou_passagem = False


screen investigacao_quintal_noir():
        imagemap:
            idle "bg_quintal_noir.png"
            hover "bg_quintal_noir.png"
            ground "bg_quintal_noir.png"
        
            hotspot(82, 300, 1197, 155) action Jump("quintal_noir_pularcerca")
            hotspot(5, 378, 71, 80) action Jump("quintal_noir_passagem")

label quintal_colorido:

    scene bg_quintal_real with dissolve
    
    c_caramelo "Estou preparado.{p}{i}{alpha=.5}{cps=25}E sempre estarei.{/cps}{/alpha}{/i}"
    
    "{i}{alpha=.5}Apesar do esforço, sou grato pelos treinos do Chefe.{p}{cps=25}Um humano sábio.{/cps}{/alpha}{/i}"
    "{i}{alpha=.5}Mesmo com a companhia um do outro e seguros, ele se prepara para o pior.{p}Eu concordo com você, Chefe.{/alpha}{/i}"
    "{i}{alpha=.5}É sempre bom estar pronto para enfrentar o caos do mundo.{/alpha}{/i}"
    c_random "Yada, yada. Comida. Yada. Comida. Yada, yada."
    "{i}{alpha=.5}Ignore ele, ignore ele. Você tem um trabalho a fazer, foque.{/alpha}{/i}"
    c_caramelo "Em posição! Pode lançar."
    c_dono "yada. yada yada yada."
    "{i}{alpha=.5}O chefe está falando algo com o bloco de sons. Boas informações são realmente indispensáveis.{/alpha}{/i}"
    c_dono "yada yada yada...{w} YADA?!"
    "{i}{alpha=.5}Este é o sinal! Eu pego, eu pego.{/alpha}{/i}"
    c_random "YADA! YADA! Comida! Yada! Atrasado! Yada!"
    "{i}{alpha=.5}{cps=15}Eu nã{/cps}{cps=5}o...{/cps}{w} N-{w}{cps=50}não consigo encontrá-la!{/cps}{/alpha}{/i}"
    "{i}{alpha=.5}Acho que o equipamento não está na área de treino... deve ter saído de nosso território.{/alpha}{/i}"
    "{i}{alpha=.5}Ainda sinto seu cheiro, ela está nos arredores, será que...{w} De'Loco.{/alpha}{/i}"
    c_billy "Yada! Fiuuuuuiiii! Comida. Yum, yada, yum."
    "{i}{alpha=.5}Preciso encontrar uma forma de confirmar minhas suspeitas,{w}{cps=25} deve haver algum jeito.{/cps}{/alpha}{/i}"
    c_caramelo "Posso ser um cachorro comum... mas sou um cachorro comum com instintos!"

    jump quintal_noir

label quintal_noir:
    
    
    if not encontrou_passagem:
        scene bg_quintal_noir with dissolve
        call screen investigacao_quintal_noir
    
    scene bg_quintal_noir_buraco with dissolve
    "{i}{alpha=.5}Consegui, essa foi por um pêlo.{/alpha}{/i}"
    c_caramelo "Chefe, tem alguém na entrada, fique atrás de mim!{w}{cps=25} ...Chefe?{/cps}"
    c_billy "Yada, yada, CARAMELO. Yada!"

    play sound "sounds/beeh-simples.mp3" #Som: Som vaso quebrado
        
    c_billy "Yada, yada!"

    play sound "sounds/beeh-simples.mp3" #Som: Som porta batendo com pressa
    c_caramelo "Chefe, o que houve?! Estou indo!"

    jump sala_noir


label quintal_noir_pularcerca:

    "{i}{alpha=.5}Mesmo com meu treino, acho que não seria capaz de pular essa barreira.{p}E mesmo que fosse, quem sabe o que me espera do outro lado?{/alpha}{/i}"

    jump quintal_noir
    

label quintal_noir_passagem:
    
    "{i}{alpha=.5}Deve ter  algo escondido  que me a{cps=25}jude a …{/cps}{/alpha}{i}"
    scene bg_quintal_noir_buraco with dissolve
    c_caramelo "Bingo!{w} É como eu sempre digo, instintos é que fazem o cão."
    $ encontrou_passagem = True
    
    scene bg_billy_noir with dissolve
    

    jump quintal_vizinho