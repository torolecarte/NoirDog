define invest_papagaio = False
define invest_bolinha = False
define invest_semente_girassol = False


screen investigacao_quintal_vizinho():
        imagemap:
            idle "bg_billy_noir.jpg"
            hover "bg_billy_noir.jpg"
            ground "bg_billy_noir.jpg"
        
            hotspot(529, 17, 197, 132) action Jump("invest_papagaio")

label quintal_vizinho:
    
    if invest_papagaio: # and invest_bolinha and invest_semente_girassol:
        menu:
            "Executar plano":
                c_caramelo "Hora de executar o plano"
                jump quintal_vizinho_plano

    call screen investigacao_quintal_vizinho

    "Placeholder"

    #menu:
    #    "Papagaio":
    #        c_caramelo "Fala sobre papagaio"
    #        $ invest_papagaio = True
    #    "Bolinha":
    #        "Fala sobre bolinha"
    #        $ invest_bolinha = True
    #    "Semente de girassol":
    #        "Fala sobre semente de girassol"
    #        $ invest_semente_girassol = True

    "Fim da cena"
    jump quintal_noir


label invest_papagaio:    
    $ invest_papagaio = True
    "Clicou no papagaio"

    jump quintal_vizinho


label invest_bolinha:
    $ invest_bolinha = True    
    "Clicou na bolinha"

    jump quintal_vizinho


label invest_semente_girassol:
    $ invest_semente_girassol = True
    "Clicou na semente de girassol"

    jump quintal_vizinho



label quintal_vizinho_plano:
    play sound "sounds/beeh-simples.mp3" #Som: Barulho da campainha

    menu:
        "Voltar para casa":
            "Preciso ir proteger a casa"
    
    # Foco na pata pisando na semente de girassol