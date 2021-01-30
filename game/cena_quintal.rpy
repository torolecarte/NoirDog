label quintal_colorido:

    scene bg_quintal_real with dissolve
    
    c_caramelo "Estou preparado.{p}{i}{alpha=.5}E sempre estarei.{/alpha}{/i}"
    
    "{i}{alpha=.5}Apesar do esforço, sou grato pelos treinos do Chefe.{p}Um homem sábio.{/alpha}{/i}"
    "{i}{alpha=.5}Mesmo na companhia um do outro e seguros, ele pensa no pior.{p}Eu concordo com você, Chefe.{/alpha}{/i}"


label quintal_noir:
    
    scene bg_quintal_noir with dissolve

    menu:
        "pular cerca":
            jump quintal_noir_pularcerca

        "moita":
            jump quintal_noir_passagem


label quintal_noir_pularcerca:

    "Não consigo"

    jump quintal_noir
    

label quintal_noir_passagem:
    
    "Encontrei uma passagem"
    
    scene bg_billy_noir with dissolve
    pause

    jump quintal_vizinho