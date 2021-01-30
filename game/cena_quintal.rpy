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
    
    "{i}{alpha=.5}Apesar do esforço, sou grato pelos treinos do Chefe.{p}{cps=25}Um homem sábio.{/cps}{/alpha}{/i}"
    "{i}{alpha=.5}Mesmo na companhia um do outro e seguros, ele pensa no pior.{p}Eu concordo com você, Chefe.{/alpha}{/i}"
    "{i}{alpha=.5}É sempre bom estar preparado para enfrentar o caos do mundo.{/alpha}{/i}"
    c_random "Yada, yada. Comida. Yada. Comida. Yada, yada."
    "{i}{alpha=.5}Ignore ele, ignore ele. Você tem um trabalho a fazer, foque.{/alpha}{/i}"
    c_caramelo "Em posição!"
    c_dono "yada. yada yada yada."
    "{i}{alpha=.5}O chefe está falando algo com o bloco de sons. Boas informações são indispensáveis.{/alpha}{/i}"
    c_dono "yada yada yada...{w} YADA?!"
    "{i}{alpha=.5}Este é o sinal! Eu pego, eu pego.{/alpha}{/i}"
    c_random "YADA! YADA! Comida! Yada! Atrasado! Yada!"
    "{i}{alpha=.5}{cps=15}Não...{/cps}{w} não é possível.{/alpha}{/i}"
    "{i}{alpha=.5}O equipamento não está na área de treino... deve ter saído de nosso território.{/alpha}{/i}"
    "{i}{alpha=.5}Ainda sinto seu cheiro, pode estar nos arredores, mas...{w} De'Loco.{/alpha}{/i}"
    c_billy "Yada! Fiuuuuuiiii! Comida. Yum, yada, yum."
    "{i}{alpha=.5}Preciso encontrar uma forma de confirmar minhas suspeitas,{w}{cps=25} deve haver algum jeito.{/cps}{/alpha}{/i}"
    c_caramelo "Posso ser um cachorro comum... mas sou um cachorro comum com instintos!"

    jump quintal_noir

label quintal_noir:
    
    scene bg_quintal_noir with dissolve

    if not encontrou_passagem:
        call screen investigacao_quintal_noir
    
    c_caramelo "Consegui. Chefe, Tem alguém na entrada, fique atrás de mim! ...Chefe?"
    c_billy "Yada, yada, CARAMELO. Yada!"

    play sound "sounds/beeh-simples.mp3" #Som: Som vaso quebrado
    play sound "sounds/beeh-simples.mp3" #Som: Pisando na casca de semente de girassol
    
    pause
    c_billy "Yada, yada!"

    play sound "sounds/beeh-simples.mp3" #Som: Som porta batendo com pressa
    c_caramelo "Chefe, o que houve?! Estou indo!"

    jump sala_noir


label quintal_noir_pularcerca:

    "{i}{alpha=.5}Mesmo com meu treino, acho que não seria capaz de pular essa barreira.{p}E mesmo se fosse, quem sabe o que pode estar me esperando do outro lado?{/alpha}{/i}"

    jump quintal_noir
    

label quintal_noir_passagem:
    
    "{i}{alpha=.5}Talvez por aqui tenha algo oculto que eu possa…{/alpha}{i}"
    c_caramelo "Bingo!{w} É como eu sempre digo, instintos é que fazem o cão."
    $ encontrou_passagem = True
    
    scene bg_billy_noir with dissolve
    

    jump quintal_vizinho