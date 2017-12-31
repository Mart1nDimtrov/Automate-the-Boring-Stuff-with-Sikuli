while(True):
    if (exists(Pattern("1509989491046.png").similar(0.97))):
        click(Pattern("1509989491046.png").similar(0.97).targetOffset(-41,-2))
    else:
        wheel(WHEEL_DOWN, 5)
    