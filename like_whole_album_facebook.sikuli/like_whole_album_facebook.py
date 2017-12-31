loc = Location(920, 400)
while(True):
    if (exists("1509787646234.png")):
        click("1509787646234.png")
        click(Pattern("1509787646234.png").targetOffset(-98,103))
    else:
        click(loc)
        #print(find(Pattern("1509787646234.png").targetOffset(-98,103)))
        
        
   