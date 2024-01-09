controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    encrypt(game.askForString("decryption", 6), false, mySprite)
})
function encrypt (color: string, code: boolean, image2: Sprite) {
    index = 0
    for (let column = 0; column <= image2.height - 1; column++) {
        for (let row = 0; row <= image2.width - 1; row++) {
            if (code) {
                image2.image.setPixel(column, row, (image2.image.getPixel(column, row) + how(color.charAt(index))) % 16)
            } else {
                image2.image.setPixel(column, row, (image2.image.getPixel(column, row) - how(color.charAt(index))) % 16)
            }
            index += 3
            if (index >= color.length) {
                index = 0
            }
        }
        pause(1)
    }
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    encrypt(game.askForString("encrypt", 6), true, mySprite)
})
function how (text: string) {
    j = "abcdefghijklmnopqrstuvwxyz"
    return j.indexOf(text)
}
let j = ""
let index = 0
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.y = 70
