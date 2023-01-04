from organizer import Organizer

whos_organizer = Organizer("mj.c")

while True:
    print(
        """
        Please choose action:
        1) Add note
        2) Add business card
        3) show notes
        4) show business cards
        
        0) Close organizer
        """
    )
    choice = input()
    match choice:
        case '0': break
        case '1': whos_organizer.AddNote()
        case '2': whos_organizer.AddBusinessCard()
        case '3': whos_organizer.ShowNotes()
        case '4': whos_organizer.ShowBusinessCard()
