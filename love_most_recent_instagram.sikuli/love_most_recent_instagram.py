click("1509957472915.png")
site_opened = False
while(True):
    if(not site_opened and exists("1509957556912.png")): #:
            type("instagram.com")
            type(Key.ENTER)
            site_opened = True
    if(exists("1509957732220.png")):
        click("1509957918731.png")
        type("#travel")
        click(Pattern("1509961774610.png").targetOffset(2,63))
        while(not exists("1509958190329.png")):
                wheel(WHEEL_DOWN, 5)
        click(Pattern("1509958190329.png").targetOffset(79,130))
        while(True):
            click(Pattern("1508838307929.png").similar(0.90))
            click("1508838505048.png")

        
    