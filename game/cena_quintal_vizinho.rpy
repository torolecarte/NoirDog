define invest_papagaio = False
define invest_bolinha = False
define invest_semente_girassol = False
define entrou_cena = True


screen investigacao_quintal_vizinho():
        imagemap:
            idle "bg_billy_noir.jpg"
            hover "bg_billy_noir.jpg"
            ground "bg_billy_noir.jpg"
        
            hotspot(529, 17, 197, 132) action Jump("invest_papagaio")
            hotspot(491, 172, 70, 51) action Jump("invest_bolinha")
            hotspot(833, 555, 86, 90) action Jump("invest_semente_girassol")

label quintal_vizinho:
    
    if invest_papagaio and invest_bolinha and invest_semente_girassol:
        "{i}{alpha=.5}Se meu instinto estiver correto, eu só preciso esperar um pou{cps=15}co...{/cps}{/alpha}{/i}"
        ##Papagaio muda o sprite de acordado para dormindo
        "{i}{alpha=.5}Como previsto, ele pode ser louco, mas o peso da comida tem sempre o mesmo resultado.{p} Sono.{/alpha}{/i}"
        "{i}{alpha=.5}Muito bem, agora posso executar meu plano, apenas preciso evitar pisar nessas sementes.{p} {cps=20}Serei sorrateiro como o silêncio.{/cps}{/alpha}{/i}"
        menu:
            "Executar plano":
                c_caramelo "Bingo! Missão cumprida."
                "{i}{alpha=.5}Se isto fazia parte de seu treino, Chefe. Considere feito.{/alpha}{/i}"
                jump quintal_vizinho_plano

    if entrou_cena:
        c_caramelo "E eu tenho instintos demais para meu próprio bem...{w} De'Loco."
        $ entrou_cena = False

    call screen investigacao_quintal_vizinho


##-----

label invest_papagaio:    
    $ invest_papagaio = True
    "{i}{alpha=.5}{cps=25}Pobre coitado,{/cps}{w} o mundo externo é feito de dor e sofrimento, e este animal conhece os dois intimamente.{/alpha}{/i}"
    "{i}{alpha=.5}Não quero imaginar o que acontece por aqui, apenas os gritos constantes, cantorias estranhas e palavras sem sentido são suficientes para alimentar meus pesadelos.{/alpha}{/i}"
    "{i}{alpha=.5}O que quer que tenha o deixado assim,{w}{cps=20} jamais quero encontrar.{/cps}{/alpha}{/i}"

    jump quintal_vizinho


label invest_bolinha:
    $ invest_bolinha = True    
    "{i}{alpha=.5}Lá está,{w} brilhante como sempre com sua cor única. Logo te salvarei, apenas preciso de um plano.{/alpha}{/i}"

    jump quintal_vizinho


label invest_semente_girassol:
    $ invest_semente_girassol = True
    "{i}{alpha=.5}{cps=25}Sementes por todos os lados.{/cps}{w} Isso pode ser um problema,{w} mas por outro lado, Billie acabou de se alimentar.{/alpha}{/i}"    

    jump quintal_vizinho


label quintal_vizinho_plano:
    play sound "sounds/beeh-simples.mp3" #Som: Barulho da campainha
    "{i}{alpha=.5}Eu conheço esse som. É a entrada. Deixei a casa desprotegida. Preciso voltar!{/alpha}{/i}"
    ##pisa nas sementes e o papagaio acorda
    c_caramelo "Mas qu{cps=5}e...{/cps}"
    c_billy "atrasaaAARRRRGHHH! Atrasado! Yada! Yada! Atrasado! Yada! Sementes! Cão! Yada! Yada!"
    "{i}{alpha=.5}Não tenho tempo para isso, há alguém na casa!{/alpha}{/i}"
    c_caramelo "Saia da minha frente!"
    c_billy "Yada! Cão! Cão! Atrasado! Yada, Yada!"
    "{i}{alpha=.5}Ele é insano, fala como um dos humanos.{/alpha}{/i}"
    c_caramelo "Saia da frente!"

    menu:
        "esquerda ou direita":
            ##Menu de escolha direita ou esquerda, independente da escolha gera *esbarrar no papagaio*
            c_caramelo "Você é louco!"
            c_billy "Yada! Yada! Yada! Yada! Yada!"

    ##Escolhe o outro lado
    "outro lado"
    jump quintal_noir