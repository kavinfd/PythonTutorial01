continueLoop = True
while(continueLoop):
    value = raw_input("Type a number >> ")
    print value
    continueLoop = (not value == "42")
