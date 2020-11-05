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
def rewardHUD():
    global rewardHUD1, rewardHUD2
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

def on_on_overlap(sprite, otherSprite):
    global healthPercent
    healthPercent += -10
    BearSprite.say("CHOMP", 350)
    pause(350)
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
    game.splash("You go to sleep ", "and dream about batteries")
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
    pause(750)
sprites.on_overlap(SpriteKind.Sword, SpriteKind.bear, on_on_overlap2)

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
def initHUDtitle(hudSprite: Sprite):
    hudSprite.z = 200
    hudSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    hudSprite.left = 0

def on_overlap_tile2(sprite, location):
    game.splash("You go to sleep ", "and dream about speakers")
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
    Kiddo.destroy()
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
    game.splash("Grab your backpack and trekking poles")
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
    Kiddo.destroy()
    tiles.set_tilemap(tiles.create_tilemap(hex("""
                28002000010703030303030303030303030303030303030303030303030303030303030303030303030303100f040201110c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0b010401011216161616161616161616161616161616161616161616161616161616161616161616150f0401011216161616161616161616161616161616161616161616161616161616161616161616150104010112161616161616161616161616161616161616161616161616161616161616161616161501040101130a0a0a0a0a0a0a16161616161616161616161616161616161616161616161616161615010401010109090909090909130a0a0a0a0a0a0a0a161616161616161616161616161616161616140104110c0c0c0b010f0f01010109090909090909091216161616161509090909090909090909090101041216161615010101010101010101010101010112161616161615010101010101010101010101010412161616150101010101070303030303030305121616161616150101010101010101010101010104121616161502030303030801010101010101041216161616161501010f0f0101010101010101010412161616170c0c0c0c0c0c0c0c0c0c0c0c0b041216161616161501010101010101010101010101041216161616161616161616161616161616150412161616161615010f0101010101010101010101041216161616161616161616161616161616150412161616161615010f0101020303030303030501041216161616161616161616161616161616150412161616161615010101010101010101010104010412161616161616161616161616161616161504121616161616150101010101010101010101040104121616161616161616161616161616161615041216161616161501010101010101010101010401041216161616161616161616161616161616150412161616161615010101010101010101010104010412161616161616161616161616161616161504121616161616170c0c0c0c0c0c0c0c0c0c0b04010412161616161616161616161616161616161504121616161616161616161616161616161615040104130a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a1404130a0a0a0a0a0a0a0a0a0a16161616161615040104010909090909090909090909090909090901040109090909090909090909121616161616150401060303030303030303030303030303030303031803030303030303030303051216161616161504010101010101010101010101010101010101010104010101010101010101010412161616161615040101010101010101010101010101010101010101040101010f0101010101010412161616161615040303050101010101010f010101010101010f010104010101010101010101010412161616161615040102040101010101010101010f01010101010101040f010101010101010101041216161616161504010104010d01010101010101010101010101010104010101010101010101010412161616161615040101060e030303030303030303030303030303030801010101010f010101010412161616161615040c0c0c0c0b010101010f01010101010101010101010101010101010101010104130a0a0a0a0a14040a0a0a0a0a010101010101010101010101010101010101010101010101010104010909090909010409090909090101010101010101010101010101010101010101010101010101060303030303030308
            """),
            img("""
                ........................................
                        ....222222222222222222222222222222222222
                        ....2..................................2
                        ....2..................................2
                        ....2..................................2
                        ....2..................................2
                        .....22222222..........................2
                        ..22222.......2222222......222222222222.
                        ..2...2..............2.....2............
                        ..2...2..............2.....2............
                        ..2...2..............2.....2............
                        ..2....2222222222222.2.....2............
                        ..2................2.2.....2............
                        ..2................2.2.....2............
                        ..2................2.2.....2............
                        ..2................2.2.....2............
                        ..2................2.2.....2............
                        ..2................2.2.....2............
                        ..2................2.2.....222222222222.
                        ..2................2.2................2.
                        ..2................2.2................2.
                        ...2222222222222222...22222222222.....2.
                        ................................2.....2.
                        ................................2.....2.
                        ................................2.....2.
                        ................................2.....2.
                        ................................2.....2.
                        ................................2.....2.
                        ................................2.....2.
                        22222...........................22....2.
                        ....2............................22222..
                        22222...................................
            """),
            [myTiles.transparency16,
                myTiles.tile1,
                myTiles.tile3,
                myTiles.tile10,
                myTiles.tile11,
                myTiles.tile12,
                myTiles.tile13,
                myTiles.tile18,
                myTiles.tile19,
                myTiles.tile20,
                myTiles.tile31,
                myTiles.tile34,
                myTiles.tile36,
                myTiles.tile43,
                myTiles.tile48,
                myTiles.tile17,
                myTiles.tile26,
                myTiles.tile28,
                myTiles.tile29,
                myTiles.tile30,
                myTiles.tile32,
                myTiles.tile33,
                myTiles.tile35,
                myTiles.tile37,
                myTiles.tile49],
            TileScale.SIXTEEN))
    startLevel()
    spawnFire()
def Level1():
    tiles.set_tilemap(tilemap("""
        level_0
    """))
    startLevel()
def drawHUDMeter(percent: number, hudSprite: Sprite, onColor: number, offColor: number):
    global fillWidth
    hudSprite.image.fill(offColor)
    fillWidth = percent * meterWidth / 100
    hudSprite.image.fill_rect(0, 0, fillWidth, hudSprite.height, onColor)

def on_on_overlap3(sprite, otherSprite):
    Berries.follow(Squirrel, 100)
    Squirrel.follow(squirrelExit, 48)
sprites.on_overlap(SpriteKind.squirrel, SpriteKind.food, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    global squirrelIs
    Squirrel.destroy()
    squirrelIs = 0
sprites.on_overlap(SpriteKind.Sword, SpriteKind.squirrel, on_on_overlap4)

def on_overlap_tile3(sprite, location):
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
            tiles.set_tile_at(value22, myTiles.tile5)
        elif randint(1, 6) == 1:
            tiles.set_tile_at(value22, myTiles.tile6)
        elif randint(1, 6) == 1:
            tiles.set_tile_at(value22, myTiles.tile40)
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
def Level11():
    Kiddo.destroy()
    tiles.set_tilemap(tilemap("""
        level_2
    """))
    startLevel()
    spawnSpeaker()
    spawnFire()

def on_down_pressed():
    global lastDirection
    lastDirection = 2
    walk()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

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
    for value3 in tiles.get_tiles_by_type(myTiles.tile41):
        tiles.place_on_tile(speaker, value3)
        tiles.set_tile_at(value3, myTiles.tile11)

def on_hit_wall2(sprite, location):
    global Berries, berriesIs
    if controller.A.is_pressed():
        for value32 in [CollisionDirection.LEFT,
            CollisionDirection.RIGHT,
            CollisionDirection.TOP,
            CollisionDirection.BOTTOM]:
            if tiles.tile_is(tiles.location_in_direction(tiles.location_of_sprite(Trekking_Pole), value32),
                myTiles.tile17):
                tiles.set_wall_at(location, False)
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
                tiles.place_on_tile(Berries, location)
                tiles.set_tile_at(location, myTiles.tile7)
                berriesIs += 1
                if squirrelIs == 0 and bearIs == 0:
                    if randint(0, 1) == 0:
                        spawnSquirrel()
                    elif randint(0, 3) == 0:
                        spawnBear()
scene.on_hit_wall(SpriteKind.Sword, on_hit_wall2)

def on_on_overlap5(sprite, otherSprite):
    global hasReward
    game.splash("You found some trash!")
    game.splash("You love trash!")
    otherSprite.destroy()
    hasReward += 1
    rewardHUD()
sprites.on_overlap(SpriteKind.player, SpriteKind.reward, on_on_overlap5)

def on_on_overlap6(sprite, otherSprite):
    global hungerPercent, healthPercent, berriesIs
    hungerPercent += 10
    if hungerPercent >= 100:
        hungerPercent = 100
        healthPercent += 20
    otherSprite.destroy(effects.disintegrate, 200)
    pause(200)
    if berriesIs > 0:
        berriesIs += -1
        if squirrelIs > 0:
            squirrelPath()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap6)

def on_on_overlap7(sprite, otherSprite):
    global hungerPercent, healthPercent
    hungerPercent += 20
    if hungerPercent > 100:
        hungerPercent = 100
        healthPercent += 40
    otherSprite.destroy(effects.disintegrate, 200)
sprites.on_overlap(SpriteKind.player, SpriteKind.treatkind, on_on_overlap7)

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
    if BearSprite.vx > 0 and BearSprite.x < Kiddo.x:
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

def on_on_overlap8(sprite, otherSprite):
    global squirrelIs
    otherSprite.destroy()
    Berries.destroy()
    Squirrel.destroy()
    squirrelIs = 0
sprites.on_overlap(SpriteKind.squirrel, SpriteKind.exit2, on_on_overlap8)

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
def startLevel():
    global berriesIs
    destroySprites()
    scene.set_background_color(7)
    spawnRandGrass()
    spawnPocky()
    spawnKiddo()
    berriesIs = 0
    tiles.place_on_random_tile(Kiddo, myTiles.tile48)
    for value6 in tiles.get_tiles_by_type(myTiles.tile48):
        tiles.set_tile_at(value6, myTiles.tile10)

def on_on_overlap9(sprite, otherSprite):
    global healthPercent
    healthPercent += -5
    pause(250)
sprites.on_overlap(SpriteKind.player, SpriteKind.squirrel, on_on_overlap9)

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
    if Squirrel.vx > 0 and Squirrel.x < Kiddo.x:
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
    else:
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
moving = False
battery: Sprite = None
firePitIs = 0
berriesIs = 0
speaker: Sprite = None
squirrelHealth = 0
squirrelExitIs = 0
squirrelIs = 0
squirrelExit: Sprite = None
Berries: Sprite = None
fillWidth = 0
timer: Sprite = None
kiddoIntro: Sprite = None
daddoIntro: Sprite = None
Trekking_Pole: Sprite = None
hungerPercent = 0
meterWidth = 0
hungerTitle: Sprite = None
healthBar: Sprite = None
hungerBar: Sprite = None
firePit: Sprite = None
pockyIs = 0
Pocky: Sprite = None
bearSteak: Sprite = None
bearIs = 0
BearHealth = 0
Kiddo: Sprite = None
Squirrel: Sprite = None
lastDirection = 0
BearSprite: Sprite = None
healthPercent = 0
rewardHUD2: Sprite = None
rewardHUD1: Sprite = None
hasReward = 0
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
        Kiddo.say("I literally didn't eat anything today", 2000)
    elif hungerPercent == 15:
        Kiddo.say("I'M DYING...", 1000)
    if healthPercent == 50:
        Kiddo.say("I'm bleeding!", 1000)
    elif healthPercent == 25:
        Kiddo.say("Tell the cats I love them!", 2000)
    elif healthPercent == 0:
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
    if hungerPercent <= 0:
        healthPercent += -5
game.on_update_interval(500, on_update_interval)
