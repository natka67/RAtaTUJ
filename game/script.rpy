# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Remy")
define p = Character("Profesor")
default ocena_profesora = 0
    

label start:

    scene cue
    with dissolve

    "Paryż. Restauracja UEP."
    "Remy, utalentowany szef kuchni, dowiaduje się, że pewien profesor z UEP znany ze swojej krytyki zagościł w jego restauracji."
    "Remy postanawia przygotować wyjątkowe danie, aby zdobyć uznanie profesora."

    scene kitchen with dissolve
    show remy normal
    with dissolve

    "W kuchni restauracji, Remy zastanawia się, jakie danie zaskoczy profesora."

    menu:
        "Przygotuj coś lekkiego i eleganckiego.":
            $ danie = "Krewetki z mango"
            show shrimps
            $ ocena_profesora += 2  # cena może wpływać na ocenę
        "Zaskocz go czymś nieoczekiwanym.":
            $ danie = "Kaczka w sosie borówkowym"
            show duck
            $ ocena_profesora += 4
        "Postaw na klasyczną francuską kuchnię.":
            $ danie = "Filet z kurczaka po francusku"
            show chicken
            $ ocena_profesora += 6 

    show remy happy
    r "Najlepszym wyborem będzie [danie]."

    "Remy zaczyna przygotowywać danie. W trakcie gotowania masz dwie ważne decyzje do podjęcia."
    
    r "Czy dodać sól?"
    menu:
        "Tak dodaj sól":
            "Remy dodaje sól do potrawy."
            $ ocena_profesora += 1  # wpływ na ocenę zależny od dodania soli
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

    "Danie jest gotowe. Pora na ocenę profesora."
    
    scene restaurant with dissolve

    
    show profesor normal
    p "To miejsce jest naprawdę wyjątkowe, Remy. Podoba mi się panująca tu atmosfera."

    show remy happy with dissolve
    r "Mam nadzieję, ze równiez danie przypadnie Panu do gustu."

    "Remy z uśmiechem prezentuje danie profesorowi."

    show profesor normal with dissolve

    p "Hmm, wygląda naprawdę apetycznie."
    
    if ocena_profesora < 7:
        show profesor unhappy
        p "Niestety, Remy, ale to danie mi nie przypadło do gustu. Możesz jeszcze popracować nad smakiem."
        show remy unhappy
        menu:
            "Przyjmij krytykę z pokorą.":
                "Remy przyjmuje krytykę z pokorą, obiecując poprawę."
                r "Dziękuję za opinię, profesorze. Postaram się bardziej sprostać Pańskim oczekiwaniom."
                "Profesor wychodzi z restauracji z postanowieniem o powrocie w najbliszej przyszłości."
            "Wybuchnij z gniewem.":
                "Remy nie potrafi ukryć swojego rozgoryczenia."
                r "To nieprawda! To jedno z najlepszych dań, jakie kiedykolwiek stworzyłem! Może Pan nie zna się na jedzeniu!"
                "Profesor wychodzi z restauracji z postanowieniem, ze nigdy juz tu nie wróci."
        
    else:
        show profesor happy
        p "Doskonałe! To jedno z najlepszych dań, jakie kiedykolwiek próbowałem. Jesteś prawdziwym mistrzem kulinarnym!"
        "Remy jest zadowolony z pozytywnej oceny profesora. Teraz musi zadecydować, jaki deser zaproponować."
        menu:
            "Tiramisu":
                "Remy proponuje klasyczne tiramisu jako deser."
                r "Mam dla Pana coś wyjątkowego - klasyczne tiramisu z własnym akcentem."
                $ wybrany_deser = "Tiramisu"
            "Koktajl owocowy":
                "Remy proponuje lekki koktajl owocowy jako deser."
                r "Może coś orzeźwiającego? Proszę spróbować naszego koktajlu owocowego."
                $ wybrany_deser = "Koktajl owocowy"

        "Profesor entuzjastycznie zgadza się spróbować [wybrany_deser] jako deseru."
        if ocena_profesora = "Koktajl owocowy":
            show profesor sick
            "Niestety, po zjedzeniu deseru profesor nagle zaczyna odczuwać dziwne objawy. Okazuje się, że ma alergię na składniki zawarte w deserze."

            p "O nie, coś tu nie gra. Muszę natychmiast udać się do lekarza!"

            "Remy, przerażony, patrzy, jak profesor opuszcza restaurację w pośpiechu."
        else:
            show profesor happy
            p "Profesor delektuje się deserem, wyrażając pełne zadowolenie."
            "Remy jest zadowolony z udanej kolacji i pozytywnej reakcji profesora."


        "Koniec."