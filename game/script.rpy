# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Remy")
define p = Character("Profesor")
default ocena_profesora = 0
    
image remy happy = "remy_happy.png"
image remy normal = "remy_normal.png"
image remy unhappy = "remy_unhappy.png"

image profesor happy = "profesor_happy.png"
image profesor normal = "profesor_neutral.png"
image profesor unhappy = "profesor_unhappy.png"
image profesor sick = "profesor_sick.png"

image ceue = "ceue.png"
image restaurant = "restaurant.png"
image kitchen = "kitchen.png"

image duck = "duck.png"
image chicken = "chicken.png"
image shrimp = "shrimps.png"
image coctail = "coctail.png"
image tiramisu = "tiramisu.png"

define music_kitchen = "audio/kitchen_theme.mp3"
define music_restaurant = "audio/restaurant_theme.mp3"

transform center:
    xalign 0.5 yalign 0.5

transform right_side:
    xalign 0.8 yalign 0.5

transform left_side:
    xalign 0.2 yalign 0.5

transform resize_1920_1080:
    size (1920, 1080)

label start:

    scene ceue at resize_1920_1080
    with dissolve

    "Paryż. Restauracja UEP."
    "Remy, utalentowany szef kuchni, dowiaduje się, że pewien profesor z UEP zagościł w jego restauracji."
    "Remy postanawia przygotować wyjątkowe danie, aby zdobyć uznanie Profesora."
    
    scene kitchen  at resize_1920_1080 with dissolve
    play music music_kitchen loop
    show remy happy at center
    with dissolve

    "W kuchni, Remy zastanawia się, jakie danie zaskoczy profesora."
    hide remy happy
    menu:
        "Przygotuj coś lekkiego i eleganckiego.":
            $ danie = "Krewetki z mango"
            show shrimp at center
            $ ocena_profesora += 2  
            r "Najlepszym wyborem będzie [danie]."
            hide shrimp   
        "Zaskocz go czymś nieoczekiwanym.":
            $ danie = "Kaczka w sosie borówkowym"
            show duck at center
            r "Najlepszym wyborem będzie [danie]."
            hide duck   
            $ ocena_profesora += 4
        "Postaw na klasyczną francuską kuchnię.":
            $ danie = "Filet z kurczaka po francusku"
            show chicken at center
            $ ocena_profesora += 6 
            r "Najlepszym wyborem będzie [danie]."
            hide chicken   

    "Remy zaczyna przygotowywać danie. W trakcie potrzebuje wsparcia w dwóch decyzjach.."
    show remy happy at center
    r "Czy dodać sól?"
    menu:
        "Tak dodaj sól":
            "Remy dodaje sól do potrawy."
            $ ocena_profesora += 1  
        "Nie, nie dodawaj sól.":
            "Remy kontynuuje gotowanie bez soli."

    r "Teraz czas na decyzję dotyczącą pieczenia mięsa w piekarniku."
    menu:
        "Piec [danie] krócej.":
            "Remy piecze mięso krócej, zachowując soczystość."
            $ ocena_profesora += 2
        "Piec [danie] dłużej.":
            "Remy decyduje się na dłuższe pieczenie, uzyskując intensywniejszy smak."
            $ ocena_profesora += 3
    hide remy happy
    "Danie jest gotowe. Pora na ocenę profesora."
    stop music fadeout 1.0  # Stop current music with 1 second fadeout
    play music music_restaurant loop
    scene restaurant  at resize_1920_1080 with dissolve
    show profesor normal at right_side
    p "To miejsce jest naprawdę wyjątkowe, Remy. Podoba mi się panująca tu atmosfera."
    
    show remy happy at left_side with dissolve
    r "Mam nadzieję, ze równiez danie przypadnie Panu do gustu."

    "Remy z uśmiechem prezentuje danie profesorowi."
    hide remy happy
    p "Hmm, wygląda naprawdę apetycznie."
    hide profesor normal
    if ocena_profesora < 7:
        
        show profesor unhappy at right_side
        
        p "Niestety, Remy, ale to danie mi nie przypadło do gustu. Musisz jeszcze popracować nad smakiem."
        hide profesor unhappy
        show remy unhappy at left_side
        menu:
            "Przyjmij krytykę z pokorą.":
                "Remy przyjmuje krytykę z pokorą, obiecując poprawę."
                r "Dziękuję za opinię, profesorze. Postaram się bardziej sprostać Pańskim oczekiwaniom."
                hide remy unhappy
                "Profesor wychodzi z restauracji z postanowieniem o powrocie w najbliszej przyszłości."
            "Wybuchnij z gniewem.":
                "Remy nie potrafi ukryć swojego rozgoryczenia."
                r "To nieprawda! To jedno z najlepszych dań, jakie kiedykolwiek stworzyłem! Może Pan nie zna się na jedzeniu!"
                hide remy unhappy
                "Profesor wychodzi z restauracji z postanowieniem, ze nigdy juz tu nie wróci."
        
    else:
        show profesor happy at right_side
        p "Doskonałe! To jedno z najlepszych dań, jakie kiedykolwiek próbowałem. Jesteś prawdziwym mistrzem kulinarnym!"
        "Remy jest zadowolony z pozytywnej oceny profesora. Teraz musi zadecydować, jaki deser zaproponować."
        hide profesor happy
        menu:
            "Tiramisu":
                "Remy proponuje klasyczny deser."
                show remy happy at left_side
                show tiramisu at right_side
                r "Mam dla Pana coś wyjątkowego - klasyczne tiramisu z własnym akcentem."
                $ wybrany_deser = "Tiramisu"
                hide tiramisu
            "Koktajl owocowy":
                "Remy proponuje lekki deser."
                show remy happy at left_side
                show coctail at right_side
                r "Może coś orzeźwiającego? Proszę spróbować naszego koktajlu owocowego."
                $ wybrany_deser = "Koktajl owocowy"
                hide coctail
        hide remy happy
        "Profesor entuzjastycznie zgadza się spróbować [wybrany_deser] jako deseru."
        if wybrany_deser == "Koktajl owocowy":
            show profesor sick at right_side
            "Niestety, po zjedzeniu deseru profesor nagle zaczyna odczuwać dziwne objawy. Okazuje się, że ma alergię na składniki zawarte w deserze."

            p "O nie, coś tu nie gra. Muszę natychmiast udać się do lekarza!"
            hide profesor sick
            "Remy, przerażony, patrzy, jak profesor opuszcza restaurację w pośpiechu."
        else:
            show profesor happy at right_side
            p "Profesor delektuje się deserem, wyrażając pełne zadowolenie."
            hide profesor happy
            "Remy jest zadowolony z udanej kolacji i pozytywnej reakcji profesora."
    stop music fadeout 1.0 
    "Koniec."