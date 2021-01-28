#Personagens
define a = Character('Investigador')
define b = Character('Bartender')
define c = Character('')

#Imagens Personagens
image dog1 = "dog 1.png"
image dog2 = "dog 2.png"

#Backgorunds
image bar = "bar.jpg"
image rua = "rua.jpg"

#O jogo começa aqui:
label start:
    scene bar
    play music "takefive.mp3" fadein(2)
    c ""
    show dog1
    a "Testando a fala do investigador"
    play sound "beeh-simples.mp3"
    show dog2
    b "testando a fala do bartender"
    stop music fadeout(2)
    scene rua with dissolve
    show dog1
    a "é isso por enquanto"