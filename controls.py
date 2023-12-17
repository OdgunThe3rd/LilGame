import uai
ind = None
ui = None
def ui():
    global ui
    ui = input(": ")
def run():
    class buttons:
        def __init__(self):
            pass
        def yes(self):
            global ind
            ind = True
        def no(self):
            global ind
            ind = False
        def settings(self):
            options = ['Controls', 'Credits', 'Save', 'Quit']
            w = {
                f"{options[0]}:": "the controls, issa workin",
                f"{options[1]}:": "Guy who had the idea for game and like the first 3 seconds of story: Darrien, Guy who did literally all of the work: James ;)"
                }
            try:
                ui = int(input(f"{options} #?: "))
                print(list(w.items())[ui - 1])
                
            except (ValueError, IndexError) as err:
                print("error works, now to see what i messed up on: ", err)
                
    b = buttons()       
    if ui == "y":
        b.yes()
        print("this button also works")
    elif ui == "n":
        b.no()
    elif ui == "s":
        b.settings()
        

