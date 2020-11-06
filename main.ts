namespace SpriteKind {
    export const Timer = SpriteKind.create()
    export const Sword = SpriteKind.create()
    export const HUD = SpriteKind.create()
    export const bear = SpriteKind.create()
    export const squirrel = SpriteKind.create()
    export const exit = SpriteKind.create()
    export const fire = SpriteKind.create()
    export const reward = SpriteKind.create()
    export const bush = SpriteKind.create()
    export const treatkind = SpriteKind.create()
    export const Wolf = SpriteKind.create()
    export const PyBadge = SpriteKind.create()
}
function rewardHUD () {
    if (hasReward > 0) {
        rewardHUD1 = sprites.create(img`
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
            `, SpriteKind.HUD)
        rewardHUD1.top = scene.screenHeight() - 16
        initHUDtitle(rewardHUD1)
        rewardHUD1.left = 45
    }
    if (hasReward > 1) {
        rewardHUD2 = sprites.create(img`
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
            `, SpriteKind.HUD)
        rewardHUD2.top = scene.screenHeight() - 16
        initHUDtitle(rewardHUD2)
        rewardHUD2.left = 63
    }
    if (WolfyIs == 1) {
        WolfHPHUD = sprites.create(img`
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
            `, SpriteKind.HUD)
        WolfHPHUD.top = scene.screenHeight() - 110
        initHUDtitle(WolfHPHUD)
        WolfHPHUD.left = 10
        WolfHPHUD.setImage(image.create(scene.screenWidth() - 20, 8))
    }
}
sprites.onOverlap(SpriteKind.bear, SpriteKind.Player, function (sprite, otherSprite) {
    healthPercent += -10
    BearSprite.say("CHOMP", 350)
    pause(350)
})
// 0 - up
// 
// 1 - right
// 
// 2 - down
// 
// 3 - left
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    lastDirection = 0
    walk()
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile46, function (sprite, location) {
    game.splash("You go to sleep ", "and dream about batteries")
    game.splash("You wake-up", "feeling refreshed!")
    hungerPercent += 40
    healthPercent += 40
    if (hungerPercent >= 100) {
        hungerPercent = 100
    }
    if (healthPercent >= 100) {
        healthPercent = 100
    }
    level3()
})
function squirrelPath () {
    Squirrel.follow(Kiddo)
}
sprites.onOverlap(SpriteKind.Sword, SpriteKind.bear, function (sprite, otherSprite) {
    if (BearHealth > 1) {
        BearHealth += -1
    } else if (BearHealth == 1) {
        BearSprite.destroy()
        bearIs = 0
        bearSteak = sprites.create(img`
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
            `, SpriteKind.treatkind)
        bearSteak.setPosition(Kiddo.x + 0, Kiddo.y + 0)
    }
    pause(500)
})
function wolfAnimate () {
    Wolfy.setImage(Wolfy.image)
    if (Wolfy.vx > 0) {
        animation.runImageAnimation(
        Wolfy,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    } else {
        animation.runImageAnimation(
        Wolfy,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Wolf, function (sprite, otherSprite) {
    healthPercent += -10
    pause(500)
})
function spawnPocky () {
    Pocky = sprites.create(img`
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
        `, SpriteKind.treatkind)
    pockyIs = 1
    for (let value of tiles.getTilesByType(myTiles.tile3)) {
        tiles.placeOnTile(Pocky, value)
    }
}
sprites.onOverlap(SpriteKind.Sword, SpriteKind.Wolf, function (sprite, otherSprite) {
    if (WolfyHealth > 1) {
        WolfyHealth += -10
    } else {
        Wolfy.destroy(effects.disintegrate, 500)
        WolfHPHUD.destroy()
        PyBadge2 = sprites.create(img`
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
            `, SpriteKind.PyBadge)
        PyBadge2.z = 3
        PyBadge2.setPosition(Kiddo.x + 0, Kiddo.y - 100)
        PyBadge2.follow(Kiddo, 10)
    }
    pause(500)
})
function spawnFire () {
    firePit = sprites.create(img`
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
        `, SpriteKind.fire)
    animation.runImageAnimation(
    firePit,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
    for (let value2 of tiles.getTilesByType(myTiles.tile43)) {
        tiles.placeOnTile(firePit, value2)
        tiles.setTileAt(value2, myTiles.transparency16)
    }
}
function initHUDtitle (hudSprite: Sprite) {
    hudSprite.z = 200
    hudSprite.setFlag(SpriteFlag.RelativeToCamera, true)
    hudSprite.left = 0
}
scene.onOverlapTile(SpriteKind.Player, myTiles.tile42, function (sprite, location) {
    game.splash("You go to sleep ", "and dream about speakers")
    game.splash("You wake-up", "feeling refreshed!")
    hungerPercent += 40
    healthPercent += 40
    if (hungerPercent >= 100) {
        hungerPercent = 100
    }
    if (healthPercent >= 100) {
        healthPercent = 100
    }
    Level2()
})
function spawnHUD () {
    hungerBar = sprites.create(img`
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
        `, SpriteKind.HUD)
    healthBar = sprites.create(img`
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
        `, SpriteKind.HUD)
    hungerTitle = sprites.create(img`
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
        `, SpriteKind.HUD)
    hungerTitle.top = scene.screenHeight() - 16
    hungerBar.top = scene.screenHeight() - 16
    healthBar.top = scene.screenHeight() - 8
    meterWidth = scene.screenWidth() - 140
    initHUDSprite(hungerBar)
    initHUDSprite(healthBar)
    initHUDtitle(hungerTitle)
    hungerPercent = 100
    healthPercent = 100
}
function Level2 () {
    Kiddo.destroy()
    CurrentLevel = 2
    tiles.setTilemap(tilemap`level_1`)
    startLevel()
    spawnFire()
    spawnBattery()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (lastDirection == 0) {
        animation.runImageAnimation(
        Trekking_Pole,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        false
        )
    } else if (lastDirection == 1) {
        animation.runImageAnimation(
        Trekking_Pole,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        false
        )
    } else if (lastDirection == 2) {
        animation.runImageAnimation(
        Trekking_Pole,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        false
        )
    } else {
        animation.runImageAnimation(
        Trekking_Pole,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        false
        )
    }
})
function Level11 () {
    Kiddo.destroy()
    CurrentLevel = 1
    tiles.setTilemap(tilemap`level_2`)
    startLevel()
    spawnSpeaker()
    spawnFire()
}
function intro () {
    daddoIntro = sprites.create(img`
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
        `, SpriteKind.Player)
    daddoIntro.setPosition(32, 16)
    kiddoIntro = sprites.create(img`
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
        `, SpriteKind.Player)
    kiddoIntro.setPosition(128, 31)
    game.splash("Kiddo", "Enough screen time...")
    game.splash("Grab your backpack and trekking poles")
    game.splash("You're taking a hike")
    kiddoIntro.destroy()
    daddoIntro.destroy()
    Level1()
}
function walk () {
    if (lastDirection == 0) {
        animation.runImageAnimation(
        Kiddo,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    } else if (lastDirection == 1) {
        animation.runImageAnimation(
        Kiddo,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    } else if (lastDirection == 2) {
        animation.runImageAnimation(
        Kiddo,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    } else {
        animation.runImageAnimation(
        Kiddo,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    }
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    lastDirection = 3
    walk()
})
function createTimer (ms: number) {
    timer = sprites.create(img`
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
        `, SpriteKind.Timer)
    timer.setFlag(SpriteFlag.Ghost, true)
    timer.lifespan = ms
}
function level3 () {
    Kiddo.destroy()
    tiles.setTilemap(tilemap`level_3`)
    startLevel()
    spawnFire()
    CurrentLevel = 3
}
function Level1 () {
    tiles.setTilemap(tilemap`level_0`)
    startLevel()
}
function Level5 () {
    Kiddo.destroy()
    CurrentLevel = 5
    tiles.setTilemap(tilemap`level_4`)
    startLevel()
    spawnWolf()
    WolfyHealth = 100
    WolfyIs = 1
    rewardHUD()
}
function drawHUDMeter (percent: number, hudSprite: Sprite, onColor: number, offColor: number) {
    hudSprite.image.fill(offColor)
    fillWidth = percent * meterWidth / 100
    hudSprite.image.fillRect(0, 0, fillWidth, hudSprite.height, onColor)
}
sprites.onOverlap(SpriteKind.squirrel, SpriteKind.Food, function (sprite, otherSprite) {
    Berries.follow(Squirrel, 100)
    Squirrel.follow(squirrelExit, 48)
})
sprites.onOverlap(SpriteKind.Sword, SpriteKind.squirrel, function (sprite, otherSprite) {
    Squirrel.destroy()
    squirrelIs = 0
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile26, function (sprite, location) {
    if (CurrentLevel == 3) {
        Level4()
    } else {
        Level11()
    }
})
function spawnRandGrass () {
    for (let value22 of tiles.getTilesByType(myTiles.tile1)) {
        if (randint(1, 3) == 1) {
            tiles.setTileAt(value22, myTiles.tile9)
        } else if (randint(1, 2) == 1) {
            tiles.setTileAt(value22, myTiles.tile7)
        } else if (randint(1, 2) == 1) {
            tiles.setTileAt(value22, myTiles.tile4)
        } else if (randint(1, 6) == 1) {
            tiles.setTileAt(value22, myTiles.tile5)
        } else if (randint(1, 6) == 1) {
            tiles.setTileAt(value22, myTiles.tile6)
        } else if (randint(1, 6) == 1) {
            tiles.setTileAt(value22, myTiles.tile40)
        } else {
            tiles.setTileAt(value22, myTiles.tile8)
        }
    }
}
function initHUDSprite (hudSprite: Sprite) {
    hudSprite.z = 200
    hudSprite.setFlag(SpriteFlag.RelativeToCamera, true)
    hudSprite.setImage(image.create(meterWidth, 6))
    hudSprite.left = 24
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    lastDirection = 1
    walk()
})
function spawnSquirrel () {
    squirrelExit = sprites.create(img`
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
        `, SpriteKind.exit)
    squirrelExitIs = 1
    squirrelExit.setPosition(Kiddo.x + 80, Kiddo.y + 32)
    squirrelExit.z = 1
    Squirrel = sprites.create(img`
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
        `, SpriteKind.squirrel)
    Squirrel.setPosition(squirrelExit.x - 16, squirrelExit.y - 16)
    Squirrel.follow(Berries, 70)
    squirrelHealth = 1
    squirrelIs = 1
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    lastDirection = 2
    walk()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.PyBadge, function (sprite, otherSprite) {
    game.over(true, effects.clouds)
})
function drawHUDMeter2 (percent: number, hudSprite: Sprite, onColor: number, offColor: number) {
    hudSprite.image.fill(offColor)
    fillWidth = percent * (scene.screenWidth() - 20) / 100
    hudSprite.image.fillRect(0, 0, fillWidth, hudSprite.height, onColor)
}
scene.onHitWall(SpriteKind.squirrel, function (sprite, location) {
    Squirrel.destroy()
    squirrelExit.destroy()
    Berries.destroy()
    squirrelIs = 0
    squirrelExitIs = 0
})
function spawnSpeaker () {
    speaker = sprites.create(img`
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
        `, SpriteKind.reward)
    for (let value3 of tiles.getTilesByType(myTiles.tile41)) {
        tiles.placeOnTile(speaker, value3)
        tiles.setTileAt(value3, myTiles.tile11)
    }
}
scene.onHitWall(SpriteKind.Sword, function (sprite, location) {
    if (controller.A.isPressed()) {
        for (let value32 of [CollisionDirection.Left, CollisionDirection.Right, CollisionDirection.Top, CollisionDirection.Bottom]) {
            if (tiles.tileIs(tiles.locationInDirection(tiles.locationOfSprite(Trekking_Pole), value32), myTiles.tile17)) {
                tiles.setWallAt(location, false)
                if (randint(0, 1) == 0) {
                    Berries = sprites.create(img`
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
                        `, SpriteKind.Food)
                } else {
                    Berries = sprites.create(img`
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
                        `, SpriteKind.Food)
                }
                tiles.placeOnTile(Berries, location)
                tiles.setTileAt(location, myTiles.tile7)
                berriesIs += 1
                if (squirrelIs == 0 && bearIs == 0) {
                    if (randint(0, 1) == 0) {
                        spawnSquirrel()
                    } else if (randint(0, 3) == 0) {
                        spawnBear()
                    }
                }
            }
        }
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.reward, function (sprite, otherSprite) {
    game.splash("You found some trash!")
    game.splash("You love trash!")
    otherSprite.destroy()
    hasReward += 1
    rewardHUD()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    hungerPercent += 10
    if (hungerPercent >= 100) {
        hungerPercent = 100
        healthPercent += 20
        if (healthPercent >= 100) {
            healthPercent = 100
        }
    }
    otherSprite.destroy(effects.disintegrate, 200)
    pause(200)
    if (berriesIs > 0) {
        berriesIs += -1
        if (squirrelIs > 0) {
            squirrelPath()
        }
    }
})
function Level4 () {
    Kiddo.destroy()
    tiles.setTilemap(tilemap`level_5`)
    startLevel()
    CurrentLevel = 4
}
sprites.onOverlap(SpriteKind.Wolf, SpriteKind.exit, function (sprite, otherSprite) {
    randSpawn = randint(1, 4)
    if (randSpawn == 1) {
        Wolfy.follow(WolfSpawn1)
    } else if (randSpawn == 2) {
        Wolfy.follow(WolfSpawn2)
    } else if (randSpawn == 3) {
        Wolfy.follow(WolfSpawn3)
    } else {
        Wolfy.follow(WolfSpawn4)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.treatkind, function (sprite, otherSprite) {
    hungerPercent += 20
    if (hungerPercent > 100) {
        hungerPercent = 100
        healthPercent += 40
        if (healthPercent >= 100) {
            healthPercent = 100
        }
    }
    otherSprite.destroy(effects.disintegrate, 200)
})
function spawnBear () {
    BearSprite = sprites.create(img`
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
        `, SpriteKind.bear)
    BearSprite.setPosition(Kiddo.x + 50, Kiddo.y + 50)
    BearSprite.follow(Kiddo, 55)
    BearHealth = 4
    bearIs = 1
}
function bearAnimate () {
    BearSprite.setImage(BearSprite.image)
    if (BearSprite.vx > 0) {
        animation.runImageAnimation(
        BearSprite,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    } else {
        animation.runImageAnimation(
        BearSprite,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    }
}
scene.onOverlapTile(SpriteKind.Player, myTiles.tile52, function (sprite, location) {
    game.splash("You go to sleep ", "and dream about howling...")
    game.splash("You wake-up", "feeling refreshed!")
    hungerPercent += 40
    healthPercent += 40
    if (hungerPercent >= 100) {
        hungerPercent = 100
    }
    if (healthPercent >= 100) {
        healthPercent = 100
    }
    Level5()
})
sprites.onOverlap(SpriteKind.squirrel, SpriteKind.exit, function (sprite, otherSprite) {
    otherSprite.destroy()
    Berries.destroy()
    Squirrel.destroy()
    squirrelIs = 0
})
function destroySprites () {
    for (let value4 of sprites.allOfKind(SpriteKind.reward)) {
        value4.destroy()
    }
    for (let value42 of sprites.allOfKind(SpriteKind.exit)) {
        value42.destroy()
    }
    for (let value5 of sprites.allOfKind(SpriteKind.fire)) {
        value5.destroy()
    }
    if (berriesIs > 0) {
        berriesIs = 0
        Berries.destroy()
    }
    if (squirrelIs > 0) {
        squirrelIs = 0
        Squirrel.destroy()
    }
    if (squirrelExitIs > 0) {
        squirrelExitIs = 0
        squirrelExit.destroy()
    }
    if (bearIs > 0) {
        bearIs = 0
        BearSprite.destroy()
    }
    if (pockyIs > 0) {
        pockyIs = 0
        Pocky.destroy()
    }
    if (firePitIs > 0) {
        firePitIs = 0
        firePit.destroy()
    }
}
function startLevel () {
    CurrentLevel = 0
    destroySprites()
    scene.setBackgroundColor(7)
    spawnRandGrass()
    spawnPocky()
    spawnKiddo()
    berriesIs = 0
    tiles.placeOnRandomTile(Kiddo, myTiles.tile48)
    for (let value6 of tiles.getTilesByType(myTiles.tile48)) {
        tiles.setTileAt(value6, myTiles.tile10)
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.squirrel, function (sprite, otherSprite) {
    healthPercent += -5
    pause(250)
})
sprites.onDestroyed(SpriteKind.Timer, function (sprite) {
    animation.stopAnimation(animation.AnimationTypes.All, Kiddo)
    walk()
})
function spawnBattery () {
    battery = sprites.create(img`
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
        `, SpriteKind.reward)
    for (let value7 of tiles.getTilesByType(myTiles.tile47)) {
        tiles.placeOnTile(battery, value7)
        tiles.setTileAt(value7, myTiles.tile11)
    }
}
function spawnWolf () {
    WolfSpawn1 = sprites.create(img`
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
        `, SpriteKind.exit)
    WolfSpawn2 = sprites.create(img`
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
        `, SpriteKind.exit)
    WolfSpawn3 = sprites.create(img`
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
        `, SpriteKind.exit)
    WolfSpawn4 = sprites.create(img`
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
        `, SpriteKind.exit)
    WolfSpawn1.setPosition(Kiddo.x + 0, Kiddo.y + 72)
    WolfSpawn2.setPosition(Kiddo.x + 72, Kiddo.y + 0)
    WolfSpawn3.setPosition(Kiddo.x + 0, Kiddo.y - 72)
    WolfSpawn4.setPosition(Kiddo.x - 72, Kiddo.y - 0)
    WolfSpawn1.z = 1
    WolfSpawn2.z = 1
    WolfSpawn3.z = 1
    WolfSpawn4.z = 1
    Wolfy = sprites.create(img`
        ................................
        ................................
        ................................
        ................................
        ........ff......................
        .......fbf....................ff
        ......fbbf...................fbf
        .....ffbbf..................fbbf
        ...ffbbbbbf................fbbbf
        ..fbbbbbbbbfffffff........fbbbf.
        ..fbbbbbbbbbbbbbbbffffffffbbbbf.
        ...fbbffbbbbbbbbbbbbbbbbbbbbbf..
        ....ffbbbbbbbbbbbbbbbbbbbbbbf...
        ......fbbbbbbbbbbbbbbbbbbbbf....
        .......fbbbbbbbbbbbbbbbbbbbf....
        ........fbfbbbbbbbbbbbbbbbbf....
        ........fbffffffffbbbbbbfbbf....
        ........fbf.......ffbbbfbbbf....
        ........fbf.........ffbfbbf.....
        ........fbf..........fbfbbf.....
        .......ffbf.........fbbfbbf.....
        ......fbbbf.........fbfbbbf.....
        ......ffff.........fffffff......
        ................................
        `, SpriteKind.Wolf)
    Wolfy.z = 2
    Wolfy.setPosition(WolfSpawn1.x - 0, WolfSpawn1.y - 0)
    Wolfy.follow(WolfSpawn2, 80)
}
function spawnKiddo () {
    Kiddo = sprites.create(img`
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
        `, SpriteKind.Player)
    Kiddo.z = 3
    controller.moveSprite(Kiddo, 50, 50)
    Trekking_Pole = sprites.create(img`
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
        `, SpriteKind.Sword)
    scene.cameraFollowSprite(Kiddo)
}
function squirrelAnimate () {
    Squirrel.setImage(Squirrel.image)
    if (Squirrel.vx > 0) {
        animation.runImageAnimation(
        Squirrel,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    } else {
        animation.runImageAnimation(
        Squirrel,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    }
}
let moving = false
let battery: Sprite = null
let firePitIs = 0
let WolfSpawn4: Sprite = null
let WolfSpawn3: Sprite = null
let WolfSpawn2: Sprite = null
let WolfSpawn1: Sprite = null
let randSpawn = 0
let berriesIs = 0
let speaker: Sprite = null
let squirrelHealth = 0
let squirrelExitIs = 0
let squirrelIs = 0
let squirrelExit: Sprite = null
let Berries: Sprite = null
let fillWidth = 0
let timer: Sprite = null
let kiddoIntro: Sprite = null
let daddoIntro: Sprite = null
let Trekking_Pole: Sprite = null
let meterWidth = 0
let hungerTitle: Sprite = null
let healthBar: Sprite = null
let hungerBar: Sprite = null
let firePit: Sprite = null
let PyBadge2: Sprite = null
let WolfyHealth = 0
let pockyIs = 0
let Pocky: Sprite = null
let Wolfy: Sprite = null
let bearSteak: Sprite = null
let bearIs = 0
let BearHealth = 0
let Kiddo: Sprite = null
let Squirrel: Sprite = null
let hungerPercent = 0
let lastDirection = 0
let BearSprite: Sprite = null
let healthPercent = 0
let WolfHPHUD: Sprite = null
let WolfyIs = 0
let rewardHUD2: Sprite = null
let rewardHUD1: Sprite = null
let hasReward = 0
let CurrentLevel = 0
CurrentLevel = 0
intro()
spawnHUD()
game.onUpdate(function () {
    moving = controller.left.isPressed() || (controller.right.isPressed() || (controller.up.isPressed() || controller.down.isPressed()))
    if (!(moving)) {
        animation.stopAnimation(animation.AnimationTypes.All, Kiddo)
    }
    if (lastDirection == 0) {
        Trekking_Pole.bottom = Kiddo.top
        Trekking_Pole.x = Kiddo.x
    } else if (lastDirection == 1) {
        Trekking_Pole.left = Kiddo.right
        Trekking_Pole.y = Kiddo.y
    } else if (lastDirection == 2) {
        Trekking_Pole.top = Kiddo.bottom
        Trekking_Pole.x = Kiddo.x
    } else {
        Trekking_Pole.right = Kiddo.left
        Trekking_Pole.y = Kiddo.y
    }
    if (hungerPercent == 50) {
        Kiddo.say("Can I have a snack?", 1000)
    } else if (hungerPercent == 30) {
        Kiddo.say("HUNGER!", 1000)
    } else if (hungerPercent == 15) {
        Kiddo.say("I'M DYING...", 1000)
    }
    if (healthPercent == 50) {
        Kiddo.say("Ouch!", 1000)
    } else if (healthPercent == 25) {
        Kiddo.say("Double-Ouch!", 2000)
    } else if (healthPercent < 1) {
        game.over(false, effects.melt)
    }
})
game.onUpdateInterval(500, function () {
    hungerPercent += -1
    drawHUDMeter(hungerPercent, hungerBar, 4, 14)
    drawHUDMeter(healthPercent, healthBar, 3, 2)
    if (bearIs == 1) {
        bearAnimate()
    }
    if (squirrelIs == 1) {
        squirrelAnimate()
    }
    if (WolfyIs == 1) {
        wolfAnimate()
    }
    if (hungerPercent <= 0) {
        healthPercent += -5
    }
    if (WolfyIs == 1) {
        drawHUDMeter2(WolfyHealth, WolfHPHUD, 11, 15)
    }
})
