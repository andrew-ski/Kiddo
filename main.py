@namespace
class SpriteKind:
    Timer = SpriteKind.create()
    Sword = SpriteKind.create()
    HUD = SpriteKind.create()
    bear = SpriteKind.create()
    squirrel = SpriteKind.create()
    exit2 = SpriteKind.create()
    fire = SpriteKind.create()
    reward = SpriteKind.create()
    bush = SpriteKind.create()
    treatkind = SpriteKind.create()
    Wolf = SpriteKind.create()
    PyBadge = SpriteKind.create()
def rewardHUD():
    global rewardHUD1, rewardHUD2, WolfHPHUD
    if hasReward > 0:
        rewardHUD1 = sprites.create(img("""
                b b b b b b b b b b b b b b b b b c 
                            b . . . f f f f f f f . . . . . b c 
                            b . . f c c c c c c c f . . 1 1 b c 
                            b . f f c f f f f f c f f . 1 1 b c 
                            b f c c f f f f f f f c c f 2 f b c 
                            b f c f f f c c c f f f c f 2 f b c 
                            b f c f f c f f f c f f c f 2 f b c 
                            b f c f f c f f f c f f c f 2 f b c 
                            b f c f f c f f f c f f c f 2 f b c 
                            b f c f f f c c c f f f c f 2 f b c 
                            b f c c f f f f f f f c c f 2 f b c 
                            b . f f c f f f f f c f f 2 2 f b c 
                            b . . f c c c c c c c f f f f f b c 
                            b . . . f f f f f f f . . . . . b c 
                            b b b b b b b b b b b b b b b b b c
            """),
            SpriteKind.HUD)
        rewardHUD1.top = scene.screen_height() - 16
        initHUDtitle(rewardHUD1)
        rewardHUD1.left = 45
    if hasReward > 1:
        rewardHUD2 = sprites.create(img("""
                b b b b b b b b b b b b b b b b b c 
                            b d d f f f f f f f f f b . . . b c 
                            b d d f 5 4 4 4 4 4 4 f b . 1 1 b c 
                            b d f 5 4 4 4 4 4 f f d b . 1 1 b c 
                            b d f 5 4 4 4 4 f d d d b . 2 f b c 
                            b f 5 4 4 4 4 f d d d d b . 2 f b c 
                            b f 4 4 4 4 4 f f f d d b . 2 f b c 
                            b f f f f 5 4 4 4 f d d b . 2 f b c 
                            b d d d f 5 4 4 f d d d b . 2 f b c 
                            b d d f 5 4 4 f d d d d b . 2 f b c 
                            b d d f 5 4 f d d d d d b . 2 f b c 
                            b d f 5 4 f d d d d d d b 2 2 f b c 
                            b f 4 4 f d d d d d d d b f f f b c 
                            b f f f d d d d d d d d b . . . b c 
                            b b b b b b b b b b b b b b b b b c
            """),
            SpriteKind.HUD)
        rewardHUD2.top = scene.screen_height() - 16
        initHUDtitle(rewardHUD2)
        rewardHUD2.left = 63
    if WolfyIs == 1:
        WolfHPHUD = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.HUD)
        WolfHPHUD.top = scene.screen_height() - 110
        initHUDtitle(WolfHPHUD)
        WolfHPHUD.left = 10
        WolfHPHUD.set_image(image.create(scene.screen_width() - 20, 8))

def on_on_overlap(sprite, otherSprite):
    global healthPercent
    healthPercent += -10
    BearSprite.say("CHOMP", 350)
    pause(1000)
sprites.on_overlap(SpriteKind.bear, SpriteKind.player, on_on_overlap)

# 0 - up
# 
# 1 - right
# 
# 2 - down
# 
# 3 - left

def on_up_pressed():
    global lastDirection
    lastDirection = 0
    walk()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    global hungerPercent, healthPercent
    game.splash("You go to sleep ", "and dream about batteries")
    game.splash("You wake-up", "feeling refreshed!")
    hungerPercent += 40
    healthPercent += 40
    if hungerPercent >= 100:
        hungerPercent = 100
    if healthPercent >= 100:
        healthPercent = 100
    level3()
scene.on_overlap_tile(SpriteKind.player, myTiles.tile46, on_overlap_tile)

def squirrelPath():
    Squirrel.follow(Kiddo)

def on_on_overlap2(sprite, otherSprite):
    global BearHealth, bearIs, bearSteak
    if BearHealth > 1:
        BearHealth += -1
    elif BearHealth == 1:
        BearSprite.destroy()
        bearIs = 0
        bearSteak = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . f f 3 3 3 3 3 3 f f f . . . 
                            . . f 3 3 2 2 2 2 3 3 3 f f . . 
                            . f f 3 2 2 2 2 2 2 2 3 3 f . . 
                            f f 3 3 2 2 1 1 2 2 2 2 3 f f . 
                            f 3 3 2 2 1 1 1 1 1 1 2 3 3 3 f 
                            f 3 3 2 2 1 1 d d d 1 2 2 3 3 f 
                            . f 3 3 2 2 2 2 2 d 2 2 2 3 3 f 
                            . f f 3 3 2 2 2 2 2 2 3 3 3 f . 
                            . . f f 3 3 3 3 3 3 3 3 f f . . 
                            . . . f f f f f f f f f . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.treatkind)
        bearSteak.set_position(Kiddo.x + 0, Kiddo.y + 0)
    pause(500)
sprites.on_overlap(SpriteKind.Sword, SpriteKind.bear, on_on_overlap2)

def wolfAnimate():
    Wolfy.set_image(Wolfy.image)
    if Wolfy.vx > 0:
        animation.run_image_animation(Wolfy,
            [img("""
                    ..................cb.c......
                                ..................cb.c......
                                ..................cccb......
                                .................ccdffb.....
                                .................cdcc4fc....
                                .ddcc............cddcccddf..
                                ...dcc..........cccddddddd..
                                ....dcccccc...ccccdddddd....
                                .....ddccccccccccddbb.......
                                .......ddcccccccddcb........
                                .......ccdccccccdccb........
                                ......cccdddbcccddcb........
                                .....bcccbfbb.bccbcc........
                                .....bcccff......fbccdd.....
                                ....bcccff........ffccdd....
                                ...ddcfff..........ffff.....
                                ..ddfff.....................
                                ..df........................
                                ............................
                """),
                img("""
                    ....................c.c.....
                                ...................cb.c.....
                                ...................cb.c.....
                                ...................cccb.....
                                ..................ccdffb....
                                ................cccdcc4fc...
                                ddcc...ccccc.ccccccddcccddf.
                                ..dcccccccccccccddccddddddd.
                                ...dcddccdcccccddcccbddddd..
                                ....d.ccccdccccdcccbbb......
                                ......ccccdddbcdccccb.......
                                ......cccbff..bbccccb.......
                                ......ccccf....bccccb.......
                                .....ccccf......cccbf.......
                                .....dcff.......dcff........
                                .....ddff.......ddff........
                                ......ddff.......ddff.......
                                ............................
                                ............................
                """),
                img("""
                    .....................c.c....
                                ....................cb.c....
                                ....................cb.c....
                                ....................cccb....
                                ................cc.ccdffb...
                                ......ccccc...ccccccdcc4fc..
                                ....ccdcccccccccddccddcccddf
                                .dccdd.dcccccccddccccddddddd
                                ..dd...ccccdcccdccccbdddddd.
                                .......ccccdcccbccccbb......
                                .......cccb.ddbbccccb.......
                                ........cccf....cccb........
                                .........ccf....dcff........
                                ..........dcf..ddff.........
                                ..........ddf.ddff..........
                                ...........ddf..............
                                ............................
                                ............................
                                ............................
                """)],
            200,
            True)
    else:
        animation.run_image_animation(Wolfy,
            [img("""
                    ......c.bc..................
                                ......c.bc..................
                                ......bccc..................
                                .....bffdcc.................
                                ....cf4ccdc.................
                                ..fddcccddc............ccdd.
                                ..dddddddccc..........ccd...
                                ....ddddddcccc...ccccccd....
                                .......bbddccccccccccdd.....
                                ........bcddcccccccdd.......
                                ........bccdccccccdcc.......
                                ........bcddcccbdddccc......
                                ........ccbccb.bbfbcccb.....
                                .....ddccbf......ffcccb.....
                                ....ddccff........ffcccb....
                                .....ffff..........fffcdd...
                                .....................fffdd..
                                ........................fd..
                                ............................
                """),
                img("""
                    .....c.c.....................
                                .....c.bc....................
                                .....c.bc....................
                                .....bccc....................
                                ....bffdcc...................
                                ...cf4ccdccc.................
                                .fddcccddcccccc.ccccc...ccdd.
                                .dddddddccddcccccccccccccd...
                                ..dddddbcccddcccccdccddcd....
                                ......bbbcccdccccdcccc.d.....
                                .......bccccdcbdddcccc.......
                                .......bccccbb..ffbccc.......
                                .......bccccb....fcccc.......
                                .......fbccc......fcccc......
                                ........ffcd.......ffcd......
                                ........ffdd.......ffdd......
                                .......ffdd.......ffdd.......
                                .............................
                                .............................
                """),
                img("""
                    ....c.c.....................
                                ....c.bc....................
                                ....c.bc....................
                                ....bccc....................
                                ...bffdcc.cc................
                                ..cf4ccdcccccc...ccccc......
                                fddcccddccddcccccccccdcc....
                                dddddddccccddcccccccd.ddccd.
                                .ddddddbccccdcccdcccc...dd..
                                ......bbccccbcccdcccc.......
                                .......bccccbbdd.bccc.......
                                ........bccc....fccc........
                                ........ffcd....fcc.........
                                .........ffdd..fcd..........
                                ..........ffdd.fdd..........
                                ..............fdd...........
                                ............................
                                ............................
                                ............................
                """)],
            200,
            True)

def on_on_overlap3(sprite, otherSprite):
    global healthPercent
    healthPercent += -7.5
    pause(500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Wolf, on_on_overlap3)

def spawnPocky():
    global Pocky, pockyIs
    Pocky = sprites.create(img("""
            f f f f f f f f f d 
                    2 2 2 2 2 2 2 2 2 d 
                    2 2 2 2 2 2 2 2 2 d 
                    2 4 2 2 4 2 2 4 2 d 
                    2 4 2 2 4 2 2 4 2 d 
                    2 f 2 2 f 2 2 f 2 d 
                    2 2 f 2 f 2 f 2 2 d 
                    2 2 f 2 f 2 f 2 2 d 
                    2 2 2 f f f 2 2 2 d 
                    2 2 2 2 f 2 2 2 2 d 
                    2 2 2 2 f 2 2 2 2 d 
                    2 2 2 f f f 2 2 2 d 
                    2 2 2 f f f 2 2 2 d 
                    2 2 f 2 f 2 f 2 2 d 
                    2 2 f 2 f 2 f 2 2 d 
                    2 f 2 2 f 2 2 f 2 d
        """),
        SpriteKind.treatkind)
    pockyIs = 1
    for value in tiles.get_tiles_by_type(myTiles.tile3):
        tiles.place_on_tile(Pocky, value)

def on_on_overlap4(sprite, otherSprite):
    global WolfyHealth, PyBadge2
    if WolfyHealth > 1:
        WolfyHealth += -10
    else:
        Wolfy.destroy(effects.disintegrate, 500)
        WolfHPHUD.destroy()
        PyBadge2 = sprites.create(img("""
                8888bbf888888888881111181888bbf88
                            888888888888888881111181888888888
                            8888888ffffffffffffffffffffb88888
                            8888888fffffffffffffffffffff88888
                            88bbf88ffffffffffffffffffff488888
                            88bbf88ffffffffffffffffffff488bbf
                            bbf8bbfffffffffffffffffffff488bbf
                            bbf8bbfffffffffffffffffffff4bbf88
                            88bbf88ffffffffffffffffffff4bbf88
                            88bbf88ffffffffffffffffffff488888
                            8888888ffffffffffffffffffff488888
                            8888888ffffffffffffffffffff488888
                            8888881ffffffffffffffffffff488888
                            8888811ffffffffffffffffffff488888
                            8888111fffffffffffffffffffff11888
                            8881111ffffffffffffffffffffb11888
                            8811111bbbbbbbbbbbbbbbbbbbbb81888
                            811111818888888888888888888881188
                            811118188818818818818818888118818
                            811181888888888888888888888111188
            """),
            SpriteKind.PyBadge)
        PyBadge2.z = 3
        PyBadge2.set_position(Kiddo.x + 0, Kiddo.y - 100)
        PyBadge2.follow(Kiddo, 10)
    pause(500)
sprites.on_overlap(SpriteKind.Sword, SpriteKind.Wolf, on_on_overlap4)

def spawnFire():
    global firePit
    firePit = sprites.create(img("""
            . . . . . . . . f . . . . . . . 
                    . . . . . . . f 2 f . . . . . . 
                    . . . . . . f 2 4 2 f . . . . . 
                    . . . . . f 2 2 4 2 2 f . . . . 
                    . . . . f 2 2 4 4 4 2 2 f . . . 
                    . . . f 2 2 4 4 5 4 4 2 2 f . . 
                    . . f 2 2 4 4 5 5 5 4 4 2 2 f . 
                    . . f 2 2 4 4 5 5 5 4 4 2 2 f . 
                    . . . f 2 2 4 4 4 4 4 2 2 f . . 
                    . f f . f 2 2 2 2 2 2 2 f . f . 
                    f e e f f f f 2 2 2 f f f f e f 
                    . f f e e e e f f f e e e e f . 
                    f . . f f f f e e e f f f f . . 
                    . f f e e e e f f f e e e e f . 
                    f e e f f f f . . . f f f f e f 
                    . f f . . . . . . . . . . . f .
        """),
        SpriteKind.fire)
    animation.run_image_animation(firePit,
        [img("""
                . . . . . . . . f . . . . . . . 
                        . . . . . . . f 2 f . . . . . . 
                        . . . . . . f 2 2 2 f . . . . . 
                        . . . . . f 2 2 4 2 2 f . . . . 
                        . . . . f 2 2 4 4 4 2 2 f . . . 
                        . . . f 2 2 4 4 4 4 4 2 2 f . . 
                        . . f 2 2 4 4 4 5 4 4 4 2 2 f . 
                        . . f 2 2 4 4 5 5 5 4 4 2 2 f . 
                        . . . f 2 2 4 5 1 5 4 2 2 f . . 
                        . f f . f 2 2 2 2 2 2 2 f . f . 
                        f e e f f f f 2 2 2 f f f f e f 
                        . f f e e e e f f f e e e e f . 
                        f . . f f f f e e e f f f f . . 
                        . f f e e e e f f f e e e e f . 
                        f e e f f f f . . . f f f f e f 
                        . f f . . . . . . . . . . . f .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . f . . . . . . . 
                        . . . . . . . f 2 f . . . . . . 
                        . . . . . . f 2 2 2 f . . . . . 
                        . . . . . f 2 2 4 2 2 f . . . . 
                        . . . . f 2 2 4 4 4 2 2 f . . . 
                        . . . f 2 2 4 4 4 4 4 2 2 f . . 
                        . . f 2 2 2 4 4 5 4 4 2 2 2 f . 
                        . . . f 2 2 4 5 5 5 4 2 2 f . . 
                        . f f . f 2 2 2 2 2 2 2 f . f . 
                        f e e f f f f 2 2 2 f f f f e f 
                        . f f e e e e f f f e e e e f . 
                        f . . f f f f e e e f f f f . . 
                        . f f e e e e f f f e e e e f . 
                        f e e f f f f . . . f f f f e f 
                        . f f . . . . . . . . . . . f .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . f . . . . . . . 
                        . . . . . . . f 2 f . . . . . . 
                        . . . . . . f 2 2 2 f . . . . . 
                        . . . . . f 2 2 2 2 2 f . . . . 
                        . . . . f 2 2 2 4 2 2 2 f . . . 
                        . . . f 2 2 2 4 5 4 2 2 2 f . . 
                        . . . f 2 2 4 5 5 5 4 2 2 f . . 
                        . f f . f 2 2 2 2 2 2 2 f . f . 
                        f e e f f f f 2 2 2 f f f f e f 
                        . f f e e e e f f f e e e e f . 
                        f . . f f f f e e e f f f f . . 
                        . f f e e e e f f f e e e e f . 
                        f e e f f f f . . . f f f f e f 
                        . f f . . . . . . . . . . . f .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . f . . . . . . . 
                        . . . . . . . f 2 f . . . . . . 
                        . . . . . . f 2 2 2 f . . . . . 
                        . . . . . f 2 2 4 2 2 f . . . . 
                        . . . . f 2 2 4 4 4 2 2 f . . . 
                        . . . f 2 2 4 4 4 4 4 2 2 f . . 
                        . . f 2 2 2 4 4 5 4 4 2 2 2 f . 
                        . . . f 2 2 4 5 5 5 4 2 2 f . . 
                        . f f . f 2 2 2 2 2 2 2 f . f . 
                        f e e f f f f 2 2 2 f f f f e f 
                        . f f e e e e f f f e e e e f . 
                        f . . f f f f e e e f f f f . . 
                        . f f e e e e f f f e e e e f . 
                        f e e f f f f . . . f f f f e f 
                        . f f . . . . . . . . . . . f .
            """)],
        200,
        True)
    for value2 in tiles.get_tiles_by_type(myTiles.tile43):
        tiles.place_on_tile(firePit, value2)
        tiles.set_tile_at(value2, myTiles.transparency16)
def Bushes():
    global berrybush
    for value3 in tiles.get_tiles_by_type(myTiles.tile17):
        berrybush = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . f f f . . . . . . . 
                            . . . . . f 7 2 7 f . . . . . . 
                            . . . . f 7 7 7 7 7 f . . . . . 
                            . . f f 7 8 7 2 7 7 7 f f . . . 
                            . f 7 7 7 7 7 7 7 7 2 7 7 f . . 
                            . f 7 7 7 8 7 7 2 7 7 7 7 f . . 
                            . f 7 8 7 7 7 7 7 7 7 2 7 f . . 
                            . f f 7 7 7 7 8 7 7 7 7 f f . . 
                            . . f 7 7 f 7 7 7 f 7 7 f . . . 
                            . . . f f f . . . f f f . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.bush)
        tiles.place_on_tile(berrybush, value3)
        berrybush.z = 4
        tiles.set_tile_at(value3, myTiles.tile50)
def initHUDtitle(hudSprite: Sprite):
    hudSprite.z = 200
    hudSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    hudSprite.left = 0

def on_overlap_tile2(sprite, location):
    global hungerPercent, healthPercent
    game.splash("You go to sleep ", "and dream about speakers")
    game.splash("You wake-up", "feeling refreshed!")
    hungerPercent += 40
    healthPercent += 40
    if hungerPercent >= 100:
        hungerPercent = 100
    if healthPercent >= 100:
        healthPercent = 100
    Level2()
scene.on_overlap_tile(SpriteKind.player, myTiles.tile42, on_overlap_tile2)

def spawnHUD():
    global hungerBar, healthBar, hungerTitle, meterWidth, hungerPercent, healthPercent
    hungerBar = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.HUD)
    healthBar = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.HUD)
    hungerTitle = sprites.create(img("""
            bbbbbbbbbbbbbbbbbbbbbbc
                    b111ff1fff1ff11ffffffbc
                    b1fff1f1f1f1f1f1fffffbc
                    b1fff1f1f1f1f1f1fffffbc
                    b111f1f1f1f1f1f1fffffbc
                    b1fff1f1f1f1f1f1fffffbc
                    b1ffff1fff1ff11ffffffbc
                    bffffffffffffffffffffbc
                    b1f1f11ff1ff1f111f1f1bc
                    b1f1f1ff1f1f1ff1ff1f1bc
                    b111f11f111f1ff1ff111bc
                    b1f1f1ff1f1f1ff1ff1f1bc
                    b1f1f11f1f1f11f1ff1f1bc
                    bbbbbbbbbbbbbbbbbbbbbbc
        """),
        SpriteKind.HUD)
    hungerTitle.top = scene.screen_height() - 16
    hungerBar.top = scene.screen_height() - 16
    healthBar.top = scene.screen_height() - 8
    meterWidth = scene.screen_width() - 140
    initHUDSprite(hungerBar)
    initHUDSprite(healthBar)
    initHUDtitle(hungerTitle)
    hungerPercent = 100
    healthPercent = 100
def Level2():
    global CurrentLevel
    Kiddo.destroy()
    CurrentLevel = 2
    tiles.set_tilemap(tilemap("""
        level_1
    """))
    startLevel()
    spawnFire()
    spawnBattery()

def on_a_pressed():
    if lastDirection == 0:
        animation.run_image_animation(Trekking_Pole,
            [img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                b . . . . . . . . . . . . . . 
                                . f . . . . . . . . . . . . . 
                                . . f . . . . . . . . . . . . 
                                . . f . . . . . . . . . . . . 
                                . . . f . . . . . . . . . . . 
                                . . . . e . . . . . . . . . . 
                                . . . . e . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . b . . . . . . . 
                                . . . . 1 1 . b . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . 1 1 . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . e . . . . . . . 
                                . . . . . . . e . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . 1 1 1 . . . 
                                . . . . . . . . . . . 1 . . . 
                                . . . . . . . . . . . . 1 . . 
                                . . . . . . . . . . . . 1 . . 
                                . . . . . . . . . . . . . . b 
                                . . . . . . . . . . . . . f . 
                                . . . . . . 1 1 1 1 . . f . . 
                                . . . . . . . . . . . . f . . 
                                . . . . . . . . . . . f . . . 
                                . . . . . . . . . . f . . . . 
                                . . . . . . . . . . e . . . . 
                                . . . . . . . . . e . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """)],
            100,
            False)
    elif lastDirection == 1:
        animation.run_image_animation(Trekking_Pole,
            [img("""
                    . . . . . . . . b . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . f . . . . . . . . 
                                . . . . . f . . . . . . . . . 
                                . . . . f . . . . . . . . . . 
                                . . . e . . . . . . . . . . . 
                                . . e . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . 1 . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . 1 . . 1 . . . 
                                . . . . . . . . 1 . . . . . . 
                                . . . . . . . . . f f f f b . 
                                . . . . e e f f f . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . 1 . . . . . 
                                . . . . . . . . 1 1 . . . . . 
                                . . . . . . . 1 . . . . . . . 
                                e . . . . . 1 1 . . . 1 . . . 
                                . e f . . . 1 . . . 1 1 . . . 
                                . . . f f . . . . . 1 . . . . 
                                . . . . . f f . . . . . . . . 
                                . . . . . . . f f . . . . . . 
                                . . . . . . . . . f b . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """)],
            100,
            False)
    elif lastDirection == 2:
        animation.run_image_animation(Trekking_Pole,
            [img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . e . . . . . . . . . . 
                                . . . . e . . . . . . . . . . 
                                . . . f . . . . . . . . . . . 
                                . . . f . . . . . . . . . . . 
                                . . f . . . . . . . . . . . . 
                                . . f . . . . . . . . . . . . 
                                . f . . . . . . . . . . . . . 
                                . f . . . . . . . . . . . . . 
                                b . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . e . . . . . . . 
                                . . . . . . . e . . . . . . . 
                                . . . . 1 1 . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . . . . . f . . . . . . . 
                                . . . 1 1 1 . f . . . . . . . 
                                . . . . . . . b . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . e . . . . . . 
                                . . . . . . . . . e . . . . . 
                                . . . . . . . . . . f . . . . 
                                . . . . . . . 1 . . f . . . . 
                                . . . . . 1 1 . . . . f . . . 
                                . . . . 1 . . . . . . . f . . 
                                . . . . . . . . . . . . . f . 
                                . . . . . . . . . . . . . . b 
                                . . . . . . . . . . . . 1 . . 
                                . . . . . . . . . . 1 1 . . . 
                                . . . . . . . . . . 1 . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """)],
            100,
            False)
    else:
        animation.run_image_animation(Trekking_Pole,
            [img("""
                    . . . . . . . . . . . . . . . 
                                . . . b . . . . . . . . . . . 
                                . . . . f f . . . . . . . . . 
                                . . . . . . f f . . . . . . . 
                                . . . . . . . . f f . . . . . 
                                . . . . . . . . . . e . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . 1 . . . . . . . . . . . . . 
                                . 1 . . . 1 . . . . . . . . . 
                                . 1 . . . 1 . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                b f f f f . . . . . . . . . . 
                                . . . . . f f e e . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . 1 . . . . . . . . . . . . 
                                . . 1 . . . 1 . . . . . . . . 
                                . . 1 . . . 1 1 . . . . . e . 
                                . . . 1 . . . 1 . . . f e . . 
                                . . . 1 . . . . . f f . . . . 
                                . . . . 1 . . f f . . . . . . 
                                . . . . . f f . . . . . . . . 
                                . . . . b . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . .
                """)],
            100,
            False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap5(sprite, otherSprite):
    global Berries, berriesIs
    if randint(0, 1) == 0:
        Berries = sprites.create(img("""
                . . . . . . . . . f . . . . . . 
                            . . . . . f f . f 7 f . f . . . 
                            . . . f f 8 8 f f 7 f f 7 f . . 
                            . . . f 8 8 8 a f 7 f 7 f . . . 
                            . . f f 8 8 8 a f 7 7 f . . . . 
                            . f 8 8 f 8 a a f f f . . . . . 
                            f 8 8 8 8 f f f 8 8 f f . . . . 
                            f 8 8 8 a f 8 8 8 8 8 f . . . . 
                            f 8 8 8 a f f 8 8 8 a f . . . . 
                            . f a a f . . f a a f . . . . . 
                            . . f f . . . . f f . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
    else:
        Berries = sprites.create(img("""
                . . . . . . . f . . . . . . . . 
                            . . . . . f f 7 f f . . . . . . 
                            . . . . f 7 7 7 7 7 f . . . . . 
                            . . f f 2 f f 7 f f 2 f f . . . 
                            . . f 2 3 2 2 f 2 4 2 4 f . . . 
                            . . f 3 2 3 2 3 2 1 4 2 f . . . 
                            . . f 2 3 2 3 2 4 1 2 4 f . . . 
                            . . . f 2 4 2 4 2 4 2 f . . . . 
                            . . . f 4 2 4 2 4 2 4 f . . . . 
                            . . . f 2 4 2 4 2 4 2 f . . . . 
                            . . . . f 2 4 2 4 2 f . . . . . 
                            . . . . f 4 2 4 2 4 f . . . . . 
                            . . . . f 2 4 2 4 2 f . . . . . 
                            . . . . . f 2 4 2 f . . . . . . 
                            . . . . . . f f f . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
    if Kiddo.x > otherSprite.x:
        Berries.set_position(otherSprite.x - 8, otherSprite.y - 8)
    else:
        Berries.set_position(otherSprite.x + 8, otherSprite.y + 8)
    otherSprite.destroy()
    berriesIs += 1
    if squirrelIs == 0 and bearIs == 0:
        if randint(0, 1) == 0:
            spawnSquirrel()
        elif randint(0, 3) == 0:
            spawnBear()
sprites.on_overlap(SpriteKind.Sword, SpriteKind.bush, on_on_overlap5)

def Level11():
    global CurrentLevel
    Kiddo.destroy()
    CurrentLevel = 1
    tiles.set_tilemap(tilemap("""
        level_2
    """))
    startLevel()
    spawnSpeaker()
    spawnFire()
def intro():
    global daddoIntro, kiddoIntro
    daddoIntro = sprites.create(img("""
            . e e e . . 
                    e e e e e . 
                    e e e d . . 
                    . e e e e . 
                    . . d e e . 
                    . . 6 . e . 
                    . . 6 . . . 
                    . . 6 6 d . 
                    . . e . . . 
                    . . 8 . . . 
                    . . 8 . . . 
                    . . 8 . . . 
                    . . e . . . 
                    . . e e . .
        """),
        SpriteKind.player)
    daddoIntro.set_position(32, 16)
    kiddoIntro = sprites.create(img("""
            . 6 6 6 6 6 . . . . . . . . . . 
                    e e e 6 6 6 6 . . . . . . . . . 
                    e f e 6 6 6 6 . . . . . . . . . 
                    . 6 e 6 6 6 6 . . . . . . . . . 
                    . d e 6 6 6 . . . . . . . . . . 
                    . d d e 6 6 . . . . . . . . . . 
                    . . e e 6 9 . . . . . . . . . . 
                    . . 6 6 9 9 9 . . . . . . . . . 
                    . . e 6 6 9 9 9 . . . . . . . . 
                    . . 8 6 6 9 9 9 . . . . . . . . 
                    . d 6 6 6 9 9 9 . . . . . . . . 
                    . . 8 6 . 9 9 . . . . . . . . . 
                    . . e 8 . . . . . . . . . . . . 
                    . . e 8 . . . . . . . . . . . . 
                    . . . 8 . . . . . . . . . . . . 
                    . . 3 3 . . . . . . . . . . . .
        """),
        SpriteKind.player)
    kiddoIntro.set_position(128, 31)
    game.splash("Kiddo", "Enough screen time...")
    game.splash("Grab your backpack", "and trekking poles")
    game.splash("You're taking a hike")
    kiddoIntro.destroy()
    daddoIntro.destroy()
    Level1()
def walk():
    if lastDirection == 0:
        animation.run_image_animation(Kiddo,
            [img("""
                    . . . . . 6 6 6 6 6 6 . . . . . 
                                . . . . 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 e 6 6 6 . . . 
                                . . . 6 6 6 6 9 9 e 6 6 6 . . . 
                                . . . 6 6 6 9 9 9 f 6 6 6 . . . 
                                . . . . 6 6 9 9 9 f 6 6 . . . . 
                                . . . . . 6 9 9 9 f 6 . . . . . 
                                . . . . . 6 9 9 9 f 6 . . . . . 
                                . . . . . 6 . 9 9 b 6 . . . . . 
                                . . . . . d . 8 8 . d . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 3 3 . . . . . . .
                """),
                img("""
                    . . . . . 6 6 6 6 6 6 . . . . . 
                                . . . . 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 e 6 6 6 . . . 
                                . . . 6 6 6 6 9 9 e 6 6 6 . . . 
                                . . . 6 6 6 9 9 9 f 6 6 6 . . . 
                                . . . . 6 6 9 9 9 f 6 6 . . . . 
                                . . . . . 6 9 9 9 f 6 . . . . . 
                                . . . . . 6 9 9 9 f 6 . . . . . 
                                . . . . . 6 . 9 9 b 6 . . . . . 
                                . . . . . d . 8 8 . d . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 8 3 . . . . . . . 
                                . . . . . . . 3 . . . . . . . .
                """),
                img("""
                    . . . . . 6 6 6 6 6 6 . . . . . 
                                . . . . 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 e 6 6 6 . . . 
                                . . . 6 6 6 6 9 9 e 6 6 6 . . . 
                                . . . 6 6 6 9 9 9 f 6 6 6 . . . 
                                . . . . 6 6 9 9 9 f 6 6 . . . . 
                                . . . . . 6 9 9 9 f 6 . . . . . 
                                . . . . . 6 9 9 9 f 6 . . . . . 
                                . . . . . 6 . 9 9 b 6 . . . . . 
                                . . . . . d . 8 8 . d . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 3 3 . . . . . . .
                """),
                img("""
                    . . . . . 6 6 6 6 6 6 . . . . . 
                                . . . . 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 6 6 6 6 . . . 
                                . . . 6 6 6 6 6 6 e 6 6 6 . . . 
                                . . . 6 6 6 6 9 9 e 6 6 6 . . . 
                                . . . 6 6 6 9 9 9 f 6 6 6 . . . 
                                . . . . 6 6 9 9 9 f 6 6 . . . . 
                                . . . . . 6 9 9 9 f 6 . . . . . 
                                . . . . . 6 9 9 9 f 6 . . . . . 
                                . . . . . 6 . 9 9 b 6 . . . . . 
                                . . . . . d . 8 8 . d . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 3 8 . . . . . . . 
                                . . . . . . . . 3 . . . . . . .
                """)],
            200,
            True)
    elif lastDirection == 1:
        animation.run_image_animation(Kiddo,
            [img("""
                    . . 6 6 6 6 6 . 
                                . 6 6 6 6 e e e 
                                6 6 6 6 6 e f e 
                                . 6 6 6 6 e 6 . 
                                . 6 6 6 6 e d . 
                                . e 6 6 e d d . 
                                . e 9 6 e e . . 
                                . f 9 9 6 . . . 
                                9 f 9 6 6 . . . 
                                9 f 9 6 6 . . . 
                                9 f 9 6 6 6 d . 
                                . f 9 . 6 . . . 
                                . b . . 8 . . . 
                                . . . . 8 8 . . 
                                . . . 8 . 8 3 . 
                                . . . 3 . 3 . .
                """),
                img("""
                    . . 6 6 6 6 6 . 
                                . 6 6 6 6 e e e 
                                6 6 6 6 6 e f e 
                                . 6 6 6 6 e 6 . 
                                . 6 6 6 6 e d . 
                                . e 6 6 e d d . 
                                . e 9 6 e e . . 
                                . f 9 9 6 . . . 
                                9 f 9 6 6 . . . 
                                9 f 9 6 6 . . . 
                                9 f 9 6 6 6 d . 
                                . f 9 . 6 . . . 
                                . b . . 8 . . . 
                                . . . . 8 . . . 
                                . . . 8 . 8 . . 
                                . . . 3 . 3 3 .
                """),
                img("""
                    . . 6 6 6 6 6 . 
                                . 6 6 6 6 e e e 
                                6 6 6 6 6 e f e 
                                . 6 6 6 6 e 6 . 
                                . 6 6 6 6 e d . 
                                . e 6 6 e d d . 
                                . e 9 6 e e . . 
                                . f 9 9 6 . . . 
                                9 f 9 6 6 . . . 
                                9 f 9 6 6 . . . 
                                9 f 9 6 6 6 d . 
                                . f 9 . 6 . . . 
                                . b . . 8 . . . 
                                . . . . 8 . . . 
                                . . . . 8 . . . 
                                . . . . 3 3 . .
                """)],
            200,
            True)
    elif lastDirection == 2:
        animation.run_image_animation(Kiddo,
            [img("""
                    . . . . 6 6 6 6 6 6 6 . . . . . 
                                . . . 6 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 6 6 e d d d 6 6 6 . . . 
                                . . . 6 6 e f d d f d e 6 . . . 
                                . . . 6 e e 6 d d 6 d e 6 . . . 
                                . . . 6 e d d d d d d e 6 . . . 
                                . . . 6 e e d d d d e e 6 . . . 
                                . . . 6 6 e e d d e e 6 6 . . . 
                                . . . . 6 6 9 6 6 9 6 6 . . . . 
                                . . . . . 6 9 6 6 9 6 . . . . . 
                                . . . . . 6 9 6 6 9 6 . . . . . 
                                . . . . . 6 . 6 6 . 6 . . . . . 
                                . . . . . d . 8 8 . d . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 3 3 . . . . . . .
                """),
                img("""
                    . . . . 6 6 6 6 6 6 6 . . . . . 
                                . . . 6 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 6 6 e d d d 6 6 6 . . . 
                                . . . 6 6 e f d d f d e 6 . . . 
                                . . . 6 e e 6 d d 6 d e 6 . . . 
                                . . . 6 e d d d d d d e 6 . . . 
                                . . . 6 e e d d d d e e 6 . . . 
                                . . . 6 6 e e d d e e 6 6 . . . 
                                . . . . 6 6 9 6 6 9 6 6 . . . . 
                                . . . . . 6 9 6 6 9 6 . . . . . 
                                . . . . . 6 9 6 6 9 6 . . . . . 
                                . . . . . 6 . 6 6 . 6 . . . . . 
                                . . . . . d . 8 8 . d . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 8 3 . . . . . . . 
                                . . . . . . . 3 . . . . . . . .
                """),
                img("""
                    . . . . 6 6 6 6 6 6 6 . . . . . 
                                . . . 6 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 6 6 e d d d 6 6 6 . . . 
                                . . . 6 6 e f d d f d e 6 . . . 
                                . . . 6 e e 6 d d 6 d e 6 . . . 
                                . . . 6 e d d d d d d e 6 . . . 
                                . . . 6 e e d d d d e e 6 . . . 
                                . . . 6 6 e e d d e e 6 6 . . . 
                                . . . . 6 6 9 6 6 9 6 6 . . . . 
                                . . . . . 6 9 6 6 9 6 . . . . . 
                                . . . . . 6 9 6 6 9 6 . . . . . 
                                . . . . . 6 . 6 6 . 6 . . . . . 
                                . . . . . d . 8 8 . d . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 3 3 . . . . . . .
                """),
                img("""
                    . . . . 6 6 6 6 6 6 6 . . . . . 
                                . . . 6 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 6 6 e d d d 6 6 6 . . . 
                                . . . 6 6 e f d d f d e 6 . . . 
                                . . . 6 e e 6 d d 6 d e 6 . . . 
                                . . . 6 e d d d d d d e 6 . . . 
                                . . . 6 e e d d d d e e 6 . . . 
                                . . . 6 6 e e d d e e 6 6 . . . 
                                . . . . 6 6 9 6 6 9 6 6 . . . . 
                                . . . . . 6 9 6 6 9 6 . . . . . 
                                . . . . . 6 9 6 6 9 6 . . . . . 
                                . . . . . 6 . 6 6 . 6 . . . . . 
                                . . . . . d . 8 8 . d . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . . 3 8 . . . . . . . 
                                . . . . . . . . 3 . . . . . . .
                """)],
            200,
            True)
    else:
        animation.run_image_animation(Kiddo,
            [img("""
                    . 6 6 6 6 6 . . 
                                e e e 6 6 6 6 . 
                                e f e 6 6 6 6 . 
                                . 6 e 6 6 6 6 . 
                                . d e 6 6 6 . . 
                                . d d e 6 6 . . 
                                . . e e 6 9 . . 
                                . . . 6 9 9 9 . 
                                . . . 6 6 9 9 9 
                                . . . 6 6 9 9 9 
                                . d 6 6 6 9 9 9 
                                . . . 6 . 9 9 . 
                                . . . 8 . . . . 
                                . . 8 8 . . . . 
                                . 3 8 . 8 . . . 
                                . . 3 . 3 . . .
                """),
                img("""
                    . 6 6 6 6 6 . . 
                                e e e 6 6 6 6 . 
                                e f e 6 6 6 6 . 
                                . 6 e 6 6 6 6 . 
                                . d e 6 6 6 . . 
                                . d d e 6 6 . . 
                                . . e e 6 9 . . 
                                . . . 6 9 9 9 . 
                                . . . 6 6 9 9 9 
                                . . . 6 6 9 9 9 
                                . d 6 6 6 9 9 9 
                                . . . 6 . 9 9 . 
                                . . . 8 . . . . 
                                . . . 8 . . . . 
                                . . 8 . 8 . . . 
                                . 3 3 . 3 . . .
                """),
                img("""
                    . 6 6 6 6 6 . . 
                                e e e 6 6 6 6 . 
                                e f e 6 6 6 6 . 
                                . 6 e 6 6 6 6 . 
                                . d e 6 6 6 . . 
                                . d d e 6 6 . . 
                                . . e e 6 9 . . 
                                . . . 6 9 9 9 . 
                                . . . 6 6 9 9 9 
                                . . . 6 6 9 9 9 
                                . d 6 6 6 9 9 9 
                                . . . 6 . 9 9 . 
                                . . . 8 . . . . 
                                . . . 8 . . . . 
                                . . . 8 . . . . 
                                . . 3 3 . . . .
                """)],
            200,
            True)

def on_left_pressed():
    global lastDirection
    lastDirection = 3
    walk()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def createTimer(ms: number):
    global timer
    timer = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Timer)
    timer.set_flag(SpriteFlag.GHOST, True)
    timer.lifespan = ms
def level3():
    global CurrentLevel
    Kiddo.destroy()
    tiles.set_tilemap(tilemap("""
        level_3
    """))
    startLevel()
    spawnFire()
    CurrentLevel = 3
def Level1():
    tiles.set_tilemap(tilemap("""
        level_0
    """))
    startLevel()
def Level5():
    global CurrentLevel, WolfyHealth, WolfyIs
    Kiddo.destroy()
    CurrentLevel = 5
    tiles.set_tilemap(tilemap("""
        level_4
    """))
    startLevel()
    spawnWolf()
    WolfyHealth = 100
    WolfyIs = 1
    rewardHUD()
def drawHUDMeter(percent: number, hudSprite: Sprite, onColor: number, offColor: number):
    global fillWidth
    hudSprite.image.fill(offColor)
    fillWidth = percent * meterWidth / 100
    hudSprite.image.fill_rect(0, 0, fillWidth, hudSprite.height, onColor)

def on_on_overlap6(sprite, otherSprite):
    Berries.follow(Squirrel, 100)
    Squirrel.follow(squirrelExit, 48)
sprites.on_overlap(SpriteKind.squirrel, SpriteKind.food, on_on_overlap6)

def on_on_overlap7(sprite, otherSprite):
    global squirrelIs
    Squirrel.destroy()
    squirrelIs = 0
sprites.on_overlap(SpriteKind.Sword, SpriteKind.squirrel, on_on_overlap7)

def on_overlap_tile3(sprite, location):
    if CurrentLevel == 3:
        Level4()
    else:
        Level11()
scene.on_overlap_tile(SpriteKind.player, myTiles.tile26, on_overlap_tile3)

def spawnRandGrass():
    for value22 in tiles.get_tiles_by_type(myTiles.tile1):
        if randint(1, 3) == 1:
            tiles.set_tile_at(value22, myTiles.tile9)
        elif randint(1, 2) == 1:
            tiles.set_tile_at(value22, myTiles.tile7)
        elif randint(1, 2) == 1:
            tiles.set_tile_at(value22, myTiles.tile4)
        elif randint(1, 6) == 1:
            tiles.set_tile_at(value22, myTiles.tile40)
        elif randint(1, 6) == 1:
            tiles.set_tile_at(value22, myTiles.tile6)
        elif randint(1, 6) == 1:
            tiles.set_tile_at(value22, myTiles.tile5)
        else:
            tiles.set_tile_at(value22, myTiles.tile8)
def initHUDSprite(hudSprite: Sprite):
    hudSprite.z = 200
    hudSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    hudSprite.set_image(image.create(meterWidth, 6))
    hudSprite.left = 24

def on_right_pressed():
    global lastDirection
    lastDirection = 1
    walk()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def spawnSquirrel():
    global squirrelExit, squirrelExitIs, Squirrel, squirrelHealth, squirrelIs
    squirrelExit = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . e b b b b . . . . . . . 
                    . . . e b b f f b b . . . . . . 
                    . . . e b f f f f b . . . . . . 
                    . . . e b f f f f b . . . . . . 
                    . . . e b f f f f b . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.exit2)
    squirrelExitIs = 1
    squirrelExit.set_position(Kiddo.x + 80, Kiddo.y + 32)
    squirrelExit.z = 1
    Squirrel = sprites.create(img("""
            . . . c . b . . . . . b b b b . 
                    . . b b b . . . . . b b b b b b 
                    . b f b b . . . . . b b b d d b 
                    b b b b b . . . . b b b d d d b 
                    . . . d b . . . b b b d d . . . 
                    . . b b b b b . b b d d . . . . 
                    . . . d b b b . b b d . . . . . 
                    . . . d d d b b b b . . . . . . 
                    . . . . d d b b b . . . . . . . 
                    . . . . b b b b . . . . . . . .
        """),
        SpriteKind.squirrel)
    Squirrel.set_position(squirrelExit.x - 16, squirrelExit.y - 16)
    Squirrel.follow(Berries, 70)
    squirrelHealth = 1
    squirrelIs = 1

def on_down_pressed():
    global lastDirection
    lastDirection = 2
    walk()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap8(sprite, otherSprite):
    game.over(True, effects.clouds)
sprites.on_overlap(SpriteKind.player, SpriteKind.PyBadge, on_on_overlap8)

def drawHUDMeter2(percent: number, hudSprite: Sprite, onColor: number, offColor: number):
    global fillWidth
    hudSprite.image.fill(offColor)
    fillWidth = percent * (scene.screen_width() - 20) / 100
    hudSprite.image.fill_rect(0, 0, fillWidth, hudSprite.height, onColor)

def on_hit_wall(sprite, location):
    global squirrelIs, squirrelExitIs
    Squirrel.destroy()
    squirrelExit.destroy()
    Berries.destroy()
    squirrelIs = 0
    squirrelExitIs = 0
scene.on_hit_wall(SpriteKind.squirrel, on_hit_wall)

def spawnSpeaker():
    global speaker
    speaker = sprites.create(img("""
            ...................
                    ....fffffff.....11.
                    .fffcccccccfff.1111
                    .fccfffffffccf.1111
                    ffcfcccccccfcff.2f.
                    fcfccfffffccfcf.2f.
                    fcfcfffffffcfcf.2f.
                    fcfcfffffffcfcf.2f.
                    fcfcfffffffcfcf.2f.
                    fcfcfffffffcfcf.2f.
                    fcfcfffffffcfcf.2f.
                    fcfccfffffccfcf.2f.
                    ffcfcccccccfcff22f.
                    .fccfffffffccfffff.
                    .fffcccccccfff.....
                    ...fffffffff.......
        """),
        SpriteKind.reward)
    for value32 in tiles.get_tiles_by_type(myTiles.tile41):
        tiles.place_on_tile(speaker, value32)
        tiles.set_tile_at(value32, myTiles.tile11)

def on_on_overlap9(sprite, otherSprite):
    global hasReward
    game.splash("You found some trash!")
    game.splash("You love trash!")
    otherSprite.destroy()
    hasReward += 1
    rewardHUD()
sprites.on_overlap(SpriteKind.player, SpriteKind.reward, on_on_overlap9)

def on_on_overlap10(sprite, otherSprite):
    global hungerPercent, healthPercent, berriesIs
    hungerPercent += 10
    if hungerPercent >= 100:
        hungerPercent = 100
        healthPercent += 10
        if healthPercent >= 100:
            healthPercent = 100
    hungerPercent += 5
    if healthPercent >= 100:
        healthPercent = 100
    otherSprite.destroy(effects.disintegrate, 200)
    pause(200)
    if berriesIs > 0:
        berriesIs += -1
        if squirrelIs > 0:
            squirrelPath()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap10)

def Level4():
    global CurrentLevel
    Kiddo.destroy()
    tiles.set_tilemap(tilemap("""
        level_5
    """))
    startLevel()
    CurrentLevel = 4

def on_on_overlap11(sprite, otherSprite):
    global randSpawn
    randSpawn = randint(1, 4)
    if randSpawn == 1:
        Wolfy.follow(WolfSpawn1)
    elif randSpawn == 2:
        Wolfy.follow(WolfSpawn2)
    elif randSpawn == 3:
        Wolfy.follow(WolfSpawn3)
    else:
        Wolfy.follow(WolfSpawn4)
sprites.on_overlap(SpriteKind.Wolf, SpriteKind.exit2, on_on_overlap11)

def on_on_overlap12(sprite, otherSprite):
    global hungerPercent, healthPercent
    hungerPercent += 20
    if hungerPercent > 100:
        hungerPercent = 100
        healthPercent += 20
        if healthPercent >= 100:
            healthPercent = 100
    healthPercent += 10
    if healthPercent >= 100:
        healthPercent = 100
    otherSprite.destroy(effects.disintegrate, 200)
sprites.on_overlap(SpriteKind.player, SpriteKind.treatkind, on_on_overlap12)

def spawnBear():
    global BearSprite, BearHealth, bearIs
    BearSprite = sprites.create(img("""
            .....fff...ff...................
                    ....ffff..ffff..................
                    ....ffffffffff..fffffffff.......
                    ..ffffffffffffffffffffffffff....
                    ..ff1fff1ffffffffffffffffffff...
                    ffddddffffffffffffffffffffffff..
                    fdddddffffffffffffffffffffffffff
                    .dddddffffffffffffffffffffffffff
                    .dddddffffffffffffffffffffffffff
                    ..dddffffffffffffffffffffffffff.
                    ....fffffffffffffffffffffffffff.
                    .....cfffffffffcfffffffffffffff.
                    .....cfffffffffcffffffffffcffff.
                    .....cffffffffccfffffffffccffff.
                    .....bbffffffcccfffffffcccbffff.
                    .....bbbffffbcccccccccccbbbffff.
                    .....bbbbbbbbcccccbbbbbbbffffff.
                    .....bbbbb...ccccc..bbbbffffff..
                    .....bbbbb...ccccc..bbbbffffff..
                    .....bbbbb...ccccc..bbbbbfffff..
                    .....bbbbb...cccc...bbbbbfffff..
                    .....bbbb....cccc..bbbbbbffff...
                    ....bbbb....ccccc..bbbbbfffff...
                    ................................
        """),
        SpriteKind.bear)
    BearSprite.set_position(Kiddo.x + 50, Kiddo.y + 50)
    BearSprite.follow(Kiddo, 55)
    BearHealth = 4
    bearIs = 1
def bearAnimate():
    BearSprite.set_image(BearSprite.image)
    if BearSprite.vx > 0:
        animation.run_image_animation(BearSprite,
            [img("""
                    ...................ff...fff.....
                                ..................ffff..ffff....
                                .......fffffffff..ffffffffff....
                                ....ffffffffffffffffffffffffff..
                                ...ffffffffffffffffffff1fff1ff..
                                ..ffffffffffffffffffffffffddddff
                                ffffffffffffffffffffffffffdddddf
                                ffffffffffffffffffffffffffddddd.
                                ffffffffffffffffffffffffffddddd.
                                .ffffffffffffffffffffffffffddd..
                                .fffffffffffffffffffffffffff....
                                .fffffffffffffffcfffffffffc.....
                                .ffffcffffffffffcfffffffffc.....
                                .ffffccfffffffffccffffffffc.....
                                .ffffbcccfffffffcccffffffbb.....
                                .ffffbbbcccccccccccbffffbbb.....
                                .ffffffbbbbbbbcccccbbbbbbbb.....
                                ..ffffffbbbb..ccccc...bbbbb.....
                                ..ffffffbbbb..ccccc...bbbbb.....
                                ..fffffbbbbb..ccccc...bbbbb.....
                                ..fffffbbbbb...cccc...bbbbb.....
                                ...ffffbbbbbb..cccc....bbbb.....
                                ...fffffbbbbb..ccccc....bbbb....
                                ................................
                """),
                img("""
                    ...................ff...fff.....
                                ..................ffff..ffff....
                                .......fffffffff..ffffffffff....
                                ....ffffffffffffffffffffffffff..
                                ...ffffffffffffffffffff1fff1ff..
                                ..ffffffffffffffffffffffffddddff
                                ffffffffffffffffffffffffffdddddf
                                ffffffffffffffffffffffffffddddd.
                                ffffffffffffffffffffffffffddddd.
                                .ffffffffffffffffffffffffffddd..
                                .fffffffffffffffffffffffffff....
                                .fffffffffffffffcfffffffffc.....
                                .ffffcffffffffffcfffffffffc.....
                                .ffffccfffffffffccffffffffc.....
                                .ffffbcccfffffffcccffffffbb.....
                                .ffffbbbcccccccccccbffffbbb.....
                                .ffffffbbbbbbbcccccbbbbbbbb.....
                                ..ffffffbb....ccccc...bbbbb.....
                                ..ffffffb.....ccccc...bbbbb.....
                                ..fffffbb.....ccccc...bbbbb.....
                                ..ffffffb......cccc...bbbbb.....
                                ...fffffbb.....cccc....bbbb.....
                                ...ffffffbb....ccccc....bbbb....
                                ................................
                """),
                img("""
                    ...................ff...fff.....
                                ..................ffff..ffff....
                                .......fffffffff..ffffffffff....
                                ....ffffffffffffffffffffffffff..
                                ...ffffffffffffffffffff1fff1ff..
                                ..ffffffffffffffffffffffffddddff
                                ffffffffffffffffffffffffffdddddf
                                ffffffffffffffffffffffffffddddd.
                                ffffffffffffffffffffffffffddddd.
                                .ffffffffffffffffffffffffffddd..
                                .fffffffffffffffffffffffffff....
                                .fffffffffffffffcfffffffffc.....
                                .ffffcffffffffffcfffffffffc.....
                                .ffffccfffffffffccffffffffc.....
                                .ffffbcccfffffffcccffffffbb.....
                                .ffffbbbcccccccccccbffffbbb.....
                                .ffffffbbbbbbbcccccbbbbbbbbb....
                                ..fffffff.....ccccc...bbbbbb....
                                ..fffffff....ccccc.....bbbbb....
                                ...bfffff....ccccc......bbbb....
                                ...bbffff.....cccc.......bbbb...
                                .....fffff....cccc..............
                                ..............ccccc.............
                                ................................
                """)],
            200,
            True)
    else:
        animation.run_image_animation(BearSprite,
            [img("""
                    .....fff...ff...................
                                ....ffff..ffff..................
                                ....ffffffffff..fffffffff.......
                                ..ffffffffffffffffffffffffff....
                                ..ff1fff1ffffffffffffffffffff...
                                ffddddffffffffffffffffffffffff..
                                fdddddffffffffffffffffffffffffff
                                .dddddffffffffffffffffffffffffff
                                .dddddffffffffffffffffffffffffff
                                ..dddffffffffffffffffffffffffff.
                                ....fffffffffffffffffffffffffff.
                                .....cfffffffffcfffffffffffffff.
                                .....cfffffffffcffffffffffcffff.
                                .....cffffffffccfffffffffccffff.
                                .....bbffffffcccfffffffcccbffff.
                                .....bbbffffbcccccccccccbbbffff.
                                ......bbbbbbbcccccbbbbbbbffffff.
                                .......bbbccccc...bbbbbbbfffff..
                                .......bbbccccc...bbbbb..ffffff.
                                .......bbbccccc...bbbbb...fffff.
                                .......bbbcccc....bbbbb...fffff.
                                .......bbccccc...bbbbb....ffff..
                                ......bbbb...............fffff..
                                ................................
                """),
                img("""
                    .....fff...ff...................
                                ....ffff..ffff..................
                                ....ffffffffff..fffffffff.......
                                ..ffffffffffffffffffffffffff....
                                ..ff1fff1ffffffffffffffffffff...
                                ffddddffffffffffffffffffffffff..
                                fdddddffffffffffffffffffffffffff
                                .dddddffffffffffffffffffffffffff
                                .dddddffffffffffffffffffffffffff
                                ..dddffffffffffffffffffffffffff.
                                ....fffffffffffffffffffffffffff.
                                .....cfffffffffcfffffffffffffff.
                                .....cfffffffffcffffffffffcffff.
                                .....cffffffffccfffffffffccffff.
                                .....bbffffffcccfffffffcccbffff.
                                .....bbbffffbcccccccccccbbbffff.
                                .....bbbbbbbbcccccbbbbbbbffffff.
                                .....bbbbb...ccccc....bbffffff..
                                .....bbbbb...ccccc.....bffffff..
                                .....bbbbb...ccccc.....bbfffff..
                                .....bbbbb...cccc......bffffff..
                                .....bbbb....cccc.....bbfffff...
                                ....bbbb....ccccc....bbffffff...
                                ................................
                """),
                img("""
                    .....fff...ff...................
                                ....ffff..ffff..................
                                ....ffffffffff..fffffffff.......
                                ..ffffffffffffffffffffffffff....
                                ..ff1fff1ffffffffffffffffffff...
                                ffddddffffffffffffffffffffffff..
                                fdddddffffffffffffffffffffffffff
                                .dddddffffffffffffffffffffffffff
                                .dddddffffffffffffffffffffffffff
                                ..dddffffffffffffffffffffffffff.
                                ....fffffffffffffffffffffffffff.
                                .....cfffffffffcfffffffffffffff.
                                .....cfffffffffcffffffffffcffff.
                                .....cffffffffccfffffffffccffff.
                                .....bbffffffcccfffffffcccbffff.
                                .....bbbffffbcccccccccccbbbffff.
                                ....bbbbbbbbbcccccbbbbbbbffffff.
                                ....bbbbbb...ccccc.....fffffff..
                                ....bbbbb.....ccccc....fffffff..
                                ....bbbb......ccccc....fffffb...
                                ...bbbb.......cccc.....ffffbb...
                                ..............cccc....fffff.....
                                .............ccccc..............
                                ................................
                """)],
            200,
            True)

def on_overlap_tile4(sprite, location):
    global hungerPercent, healthPercent
    game.splash("You go to sleep ", "and dream about howling...")
    game.splash("You wake-up", "feeling refreshed!")
    hungerPercent += 40
    healthPercent += 40
    if hungerPercent >= 100:
        hungerPercent = 100
    if healthPercent >= 100:
        healthPercent = 100
    Level5()
scene.on_overlap_tile(SpriteKind.player, myTiles.tile52, on_overlap_tile4)

def on_on_overlap13(sprite, otherSprite):
    global squirrelIs
    otherSprite.destroy()
    Berries.destroy()
    Squirrel.destroy()
    squirrelIs = 0
sprites.on_overlap(SpriteKind.squirrel, SpriteKind.exit2, on_on_overlap13)

def destroySprites():
    global berriesIs, squirrelIs, squirrelExitIs, bearIs, pockyIs, firePitIs
    for value4 in sprites.all_of_kind(SpriteKind.reward):
        value4.destroy()
    for value42 in sprites.all_of_kind(SpriteKind.exit2):
        value42.destroy()
    for value5 in sprites.all_of_kind(SpriteKind.fire):
        value5.destroy()
    if berriesIs > 0:
        berriesIs = 0
        Berries.destroy()
    if squirrelIs > 0:
        squirrelIs = 0
        Squirrel.destroy()
    if squirrelExitIs > 0:
        squirrelExitIs = 0
        squirrelExit.destroy()
    if bearIs > 0:
        bearIs = 0
        BearSprite.destroy()
    if pockyIs > 0:
        pockyIs = 0
        Pocky.destroy()
    if firePitIs > 0:
        firePitIs = 0
        firePit.destroy()
    for value6 in sprites.all_of_kind(SpriteKind.bush):
        value6.destroy()
def startLevel():
    global CurrentLevel, berriesIs
    CurrentLevel = 0
    destroySprites()
    scene.set_background_color(7)
    spawnRandGrass()
    spawnPocky()
    spawnKiddo()
    Bushes()
    berriesIs = 0
    tiles.place_on_random_tile(Kiddo, myTiles.tile48)
    for value62 in tiles.get_tiles_by_type(myTiles.tile48):
        tiles.set_tile_at(value62, myTiles.tile10)

def on_on_overlap14(sprite, otherSprite):
    global healthPercent
    healthPercent += -2.5
    pause(250)
sprites.on_overlap(SpriteKind.player, SpriteKind.squirrel, on_on_overlap14)

def on_on_destroyed(sprite):
    animation.stop_animation(animation.AnimationTypes.ALL, Kiddo)
    walk()
sprites.on_destroyed(SpriteKind.Timer, on_on_destroyed)

def spawnBattery():
    global battery
    battery = sprites.create(img("""
            ddddffffffffddb....
                    ddddf544444fddb.11.
                    dddf544444fdddb1111
                    dddf54444fddddb1111
                    ddf54444fdddddb.2f.
                    ddf5444ffffdddb.2f.
                    df44444444fdddb.2f.
                    dffff5444fddddb.2f.
                    ddddf544fdddddb.2f.
                    dddf544fddddddb.2f.
                    dddf44fdddddddb.2f.
                    ddf54fddddddddb.2f.
                    ddf4fdddddddddb22f.
                    df4fddddddddddbfff.
                    dffdddddddddddb....
                    44444444444444c....
        """),
        SpriteKind.reward)
    for value7 in tiles.get_tiles_by_type(myTiles.tile47):
        tiles.place_on_tile(battery, value7)
        tiles.set_tile_at(value7, myTiles.tile11)
def spawnWolf():
    global WolfSpawn1, WolfSpawn2, WolfSpawn3, WolfSpawn4, Wolfy
    WolfSpawn1 = sprites.create(img("""
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 5 5 4 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 5 5 4 8 8 9 7 7 7 7 7 7 
                    7 7 7 7 7 6 7 8 8 9 7 7 7 7 7 7 
                    7 7 7 7 7 6 7 6 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 6 6 8 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 8 6 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 6 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 8 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
        """),
        SpriteKind.exit2)
    WolfSpawn2 = sprites.create(img("""
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 a a b 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 a a b d d 3 7 7 7 7 7 7 
                    7 7 7 7 7 6 7 d d 3 7 7 7 7 7 7 
                    7 7 7 7 7 6 7 6 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 6 6 8 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 8 6 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 6 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 8 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
        """),
        SpriteKind.exit2)
    WolfSpawn3 = sprites.create(img("""
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 2 2 4 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 2 2 4 2 2 3 7 7 7 7 7 7 
                    7 7 7 7 7 6 7 2 2 3 7 7 7 7 7 7 
                    7 7 7 7 7 6 7 6 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 6 6 8 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 8 6 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 6 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 8 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
        """),
        SpriteKind.exit2)
    WolfSpawn4 = sprites.create(img("""
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                    f e 7 e e 7 e e e 7 e e e e 7 e 
                    e e e e e 7 e e e 5 e e e e e e 
                    e e e e e e e e e e e e e e e e 
                    e e e e e e e e e f e e e e e e 
                    e e e e e e e e e e e e e e e e 
                    e e e e f e e e e e e e e e e e 
                    e e e e e e e e e e e e e e f e 
                    e e e e e e e e e e e e e e e e 
                    e e e e e e e e e e e e e e e e 
                    e e e f e e e e f e e e e e e e 
                    e e e e e e e e e e e e e e e e 
                    e e e e e e e e e e e e e f e e 
                    e e e e c e e e 7 7 e e e e 7 e 
                    e 7 e e 7 e e e e 7 e e e e 7 e 
                    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
        """),
        SpriteKind.exit2)
    WolfSpawn1.set_position(Kiddo.x + 0, Kiddo.y + 72)
    WolfSpawn2.set_position(Kiddo.x + 72, Kiddo.y + 0)
    WolfSpawn3.set_position(Kiddo.x + 0, Kiddo.y - 72)
    WolfSpawn4.set_position(Kiddo.x - 72, Kiddo.y - 0)
    WolfSpawn1.z = 1
    WolfSpawn2.z = 1
    WolfSpawn3.z = 1
    WolfSpawn4.z = 1
    Wolfy = sprites.create(img("""
            ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
        """),
        SpriteKind.Wolf)
    Wolfy.z = 2
    Wolfy.set_position(WolfSpawn1.x - 0, WolfSpawn1.y - 0)
    Wolfy.follow(WolfSpawn2, 80)
def spawnKiddo():
    global Kiddo, Trekking_Pole
    Kiddo = sprites.create(img("""
            . . . . 6 6 6 6 6 6 6 . . . . . 
                    . . . 6 6 6 6 6 6 6 6 6 . . . . 
                    . . . 6 6 6 e d d d 6 6 6 . . . 
                    . . . 6 6 e f d d f d e 6 . . . 
                    . . . 6 e e 6 d d 6 d e 6 . . . 
                    . . . 6 e d d d d d d e 6 . . . 
                    . . . 6 e e d d d d e e 6 . . . 
                    . . . 6 6 e e d d e e 6 6 . . . 
                    . . . . 6 6 9 6 6 9 6 6 . . . . 
                    . . . . . 6 9 6 6 9 6 . . . . . 
                    . . . . . 6 9 6 6 9 6 . . . . . 
                    . . . . . 6 . 6 6 . 6 . . . . . 
                    . . . . . d . 8 8 . d . . . . . 
                    . . . . . . . 8 8 . . . . . . . 
                    . . . . . . . 8 8 . . . . . . . 
                    . . . . . . . 3 3 . . . . . . .
        """),
        SpriteKind.player)
    Kiddo.z = 3
    controller.move_sprite(Kiddo, 50, 50)
    Trekking_Pole = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Sword)
    scene.camera_follow_sprite(Kiddo)
def squirrelAnimate():
    Squirrel.set_image(Squirrel.image)
    if Squirrel.vx > 0:
        animation.run_image_animation(Squirrel,
            [img("""
                    ....................
                                ....................
                                ....................
                                ....................
                                ..bbbb..............
                                .bbbbbb.............
                                .bddbbb......b.c....
                                .bdddbbb......bbb...
                                ....ddbbb.....bbfb..
                                .....ddbb.....bbbbb.
                                ......dbb..bbbbd....
                                .......bbbbbbbbd....
                                ........bbbbddbb....
                                .........bbbb..bb...
                                ....................
                                ....................
                """),
                img("""
                    ....................
                                ....................
                                ....................
                                ....................
                                ....................
                                ..bbbb..............
                                .bbbbbb....b.c......
                                .bddbbb.....bbb.....
                                .bdddbbb....bbfb....
                                ....ddbbb...bbbbb...
                                .....ddbb...bb......
                                ......dbb.bbbbb.....
                                .......bbbbbbdb.....
                                ........bbbddd......
                                .........bbbb.......
                                ....................
                """),
                img("""
                    ....................
                                ....................
                                ....................
                                ....................
                                ....................
                                ....bbbb.....b.c....
                                ...bbbbbb.....bbb...
                                ...bddbbb.....bbfb..
                                ...bdddbbb....bbbbb.
                                ......ddbbb...bd....
                                .......ddbb.bbbbb...
                                ........dbb.bbbd....
                                .........bbbbddd....
                                ..........bbbdd.....
                                ...........bbbb.....
                                ....................
                """)],
            200,
            True)
    else:
        animation.run_image_animation(Squirrel,
            [img("""
                    ....................
                                ....................
                                ....................
                                ....................
                                ..............bbbb..
                                .............bbbbbb.
                                ....c.b......bbbddb.
                                ...bbb......bbbdddb.
                                ..bfbb.....bbbdd....
                                .bbbbb.....bbdd.....
                                ....dbbbb..bbd......
                                ....dbbbbbbbb.......
                                ....bbddbbbb........
                                ...bb..bbbb.........
                                ....................
                                ....................
                """),
                img("""
                    ....................
                                ....................
                                ....................
                                ....................
                                ....................
                                ..............bbbb..
                                ......c.b....bbbbbb.
                                .....bbb.....bbbddb.
                                ....bfbb....bbbdddb.
                                ...bbbbb...bbbdd....
                                ......bb...bbdd.....
                                .....bbbbb.bbd......
                                .....bdbbbbbb.......
                                ......dddbbb........
                                .......bbbb.........
                                ....................
                """),
                img("""
                    ....................
                                ....................
                                ....................
                                ....................
                                ....................
                                ....c.b.....bbbb....
                                ...bbb.....bbbbbb...
                                ..bfbb.....bbbddb...
                                .bbbbb....bbbdddb...
                                ....db...bbbdd......
                                ...bbbbb.bbdd.......
                                ....dbbb.bbd........
                                ....dddbbbb.........
                                .....ddbbb..........
                                .....bbbb...........
                                ....................
                """)],
            200,
            True)
moving = False
battery: Sprite = None
firePitIs = 0
WolfSpawn4: Sprite = None
WolfSpawn3: Sprite = None
WolfSpawn2: Sprite = None
WolfSpawn1: Sprite = None
randSpawn = 0
speaker: Sprite = None
squirrelHealth = 0
squirrelExitIs = 0
squirrelExit: Sprite = None
fillWidth = 0
timer: Sprite = None
kiddoIntro: Sprite = None
daddoIntro: Sprite = None
squirrelIs = 0
berriesIs = 0
Berries: Sprite = None
Trekking_Pole: Sprite = None
meterWidth = 0
hungerTitle: Sprite = None
healthBar: Sprite = None
hungerBar: Sprite = None
berrybush: Sprite = None
firePit: Sprite = None
PyBadge2: Sprite = None
WolfyHealth = 0
pockyIs = 0
Pocky: Sprite = None
Wolfy: Sprite = None
bearSteak: Sprite = None
bearIs = 0
BearHealth = 0
Kiddo: Sprite = None
Squirrel: Sprite = None
hungerPercent = 0
lastDirection = 0
BearSprite: Sprite = None
healthPercent = 0
WolfHPHUD: Sprite = None
WolfyIs = 0
rewardHUD2: Sprite = None
rewardHUD1: Sprite = None
hasReward = 0
CurrentLevel = 0
CurrentLevel = 0
intro()
spawnHUD()

def on_on_update():
    global moving
    moving = controller.left.is_pressed() or (controller.right.is_pressed() or (controller.up.is_pressed() or controller.down.is_pressed()))
    if not (moving):
        animation.stop_animation(animation.AnimationTypes.ALL, Kiddo)
    if lastDirection == 0:
        Trekking_Pole.bottom = Kiddo.top
        Trekking_Pole.x = Kiddo.x
    elif lastDirection == 1:
        Trekking_Pole.left = Kiddo.right
        Trekking_Pole.y = Kiddo.y
    elif lastDirection == 2:
        Trekking_Pole.top = Kiddo.bottom
        Trekking_Pole.x = Kiddo.x
    else:
        Trekking_Pole.right = Kiddo.left
        Trekking_Pole.y = Kiddo.y
    if hungerPercent == 50:
        Kiddo.say("Can I have a snack?", 1000)
    elif hungerPercent == 30:
        Kiddo.say("So HUNGRY!", 1000)
    elif hungerPercent == 15:
        Kiddo.say("I'M DYING...", 1000)
    if healthPercent == 50:
        Kiddo.say("Ouch!", 1000)
    elif healthPercent == 25:
        Kiddo.say("Double-Ouch!", 2000)
    elif healthPercent < 1:
        game.over(False, effects.melt)
game.on_update(on_on_update)

def on_update_interval():
    global hungerPercent, healthPercent
    hungerPercent += -1
    drawHUDMeter(hungerPercent, hungerBar, 4, 14)
    drawHUDMeter(healthPercent, healthBar, 3, 2)
    if bearIs == 1:
        bearAnimate()
    if squirrelIs == 1:
        squirrelAnimate()
    if WolfyIs == 1:
        wolfAnimate()
    if hungerPercent <= 0:
        healthPercent += -5
    if WolfyIs == 1:
        drawHUDMeter2(WolfyHealth, WolfHPHUD, 11, 15)
game.on_update_interval(500, on_update_interval)
