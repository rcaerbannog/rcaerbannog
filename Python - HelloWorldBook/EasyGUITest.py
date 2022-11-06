import easygui
flavour = easygui.integerbox("What is your favourite number?", 4, 8)
easygui.msgbox("You picked " + str(flavour))
