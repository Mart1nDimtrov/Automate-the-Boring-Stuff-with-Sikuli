while(True):
    if (exists(Pattern("1509655746108.png").similar(0.95))):
        hover(Pattern("1509655746108.png").similar(0.95))
        click("1509970666634.png")
        wait(1)
        wheel(WHEEL_DOWN, 5)
    elif(exists("1509970886044.png")):
        hover("1509970886044.png")
        click("1509970941285.png")
    else:
        wheel(WHEEL_DOWN, 5)
        