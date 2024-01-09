def on_b_pressed():
    doSomething2(mySprite, mySprite, True)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    doSomething2(mySprite, mySprite, False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def doSomething2(colors: Sprite, image2: Sprite, code: bool):
    global index
    index = 0
    row = 0
    while row <= image2.height - 1:
        column = 0
        while column <= image2.width - 1:
            if code:
                image2.image.set_pixel(column,
                    row,
                    (image2.image.get_pixel(column, row) + colors.image.get_pixel(index, 0)) % 32)
            else:
                picture = 0
                image2.image.set_pixel(column,
                    row,
                    (image2.image.get_pixel(column, picture) - (colors.image.get_pixel(index, 0) + 32)) % 32)
            index += 1
            if index == colors.width:
                index = 0
            pause(1)
            column += 1
        row += 1
index = 0
mySprite: Sprite = None
mySprite = sprites.create(img("""
        .............6666...............
            ..........666667766.6666........
            .........677777777767776........
            ......66667775577757777666......
            .....677666675557557776777666...
            .....6776777775555577777766776..
            ...66666777777775777777766666...
            .66667767777755757555777776776..
            6666777677775577557555777767766.
            .6667767777777775577777777767666
            .c6766777677777775777777677766..
            cc77666667777777777777777666666c
            cc76666677777777777777777766776c
            c6666776777777777777766677666776
            66667766667776777767767766766666
            ccc76677677776677766767776776ccc
            cc7766776777677677676667767766cc
            .666c676667677766667766666666cc.
            .ccc66676666776666677677666cccc.
            ...ccc77c6767666676676677666ccc.
            ...cc676c7766676677666666c666cc.
            ....c6cc676c6677677c66c666ccc...
            ....ccccc6c66667667cc6ccc6ccc...
            ......ccccc66c66c66cccccccc.....
            .......cc.cc6c6ccc6cccc.cc......
            ...........cccccccccc...........
            .............feeeeee............
            ............feeeeeefe...........
            .........eeeeefeeeffee..........
            ............ffffeef..ee.........
            ...............fee..............
            ................e...............
    """),
    SpriteKind.player)
key = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . 3 2 9 7 5 6 a 4 b e c f . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
key.top = 0
game.show_long_text("press b and a right after each other to encrypt.",
    DialogLayout.BOTTOM)