define encontrou_passagem = False


label quintal_colorido:

    scene bg_quintal_real with dissolve
    
    c_caramelo "Estou preparado.{p}{i}{alpha=.5}E sempre estarei.{/alpha}{/i}"
    
    "{i}{alpha=.5}Apesar do esforço, sou grato pelos treinos do Chefe.{p}Um homem sábio.{/alpha}{/i}"
    "{i}{alpha=.5}Mesmo na companhia um do outro e seguros, ele pensa no pior.{p}Eu concordo com você, Chefe.{/alpha}{/i}"
    
    jump quintal_noir

label quintal_noir:
    
    scene bg_quintal_noir with dissolve

    # Adicionar controle de fluxo para caso a seleção já tenha sido feita!!
    if not encontrou_passagem:
        menu:
            "pular cerca":
                jump quintal_noir_pularcerca
            "moita":
                jump quintal_noir_passagem
    
    "Placeholder" "[Fala antes de entrar na casa]"

    play music "sounds/beeh-simples.mp3" #Som: Pisando na casca de semente de girassol

    jump sala_noir


label quintal_noir_pularcerca:

    "Não consigo"

    jump quintal_noir
    

label quintal_noir_passagem:
    
    $ encontrou_passagem = True

    "Encontrei uma passagem"
    
    scene bg_billy_noir with dissolve
    pause

    jump quintal_vizinho