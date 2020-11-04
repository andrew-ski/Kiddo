namespace SpriteKind {
    export const Timer = SpriteKind.create()
    export const Sword = SpriteKind.create()
    export const HUD = SpriteKind.create()
    export const bear = SpriteKind.create()
    export const squirrel = SpriteKind.create()
    export const exit = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.bear, SpriteKind.Player, function (sprite, otherSprite) {
    healthPercent += -10
    BearSprite.say("CHOMP", 500)
    pause(1000)
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
            `, SpriteKind.Food)
        bearSteak.setPosition(Kiddo.x + 0, Kiddo.y + 0)
    }
    pause(1000)
})
function spawnPocky () {
    Pocky = sprites.create(img`
        f f f f f f f f f 
        2 2 2 2 2 2 2 2 2 
        2 2 2 2 2 2 2 2 2 
        2 4 4 2 4 2 2 4 2 
        2 4 4 2 4 2 2 4 2 
        2 f f 2 f 2 2 f 2 
        2 f 1 1 f 2 f f 2 
        2 2 1 f 1 1 f f 2 
        2 2 1 f f f 1 2 2 
        2 2 1 f f 1 1 2 2 
        2 2 1 1 1 f 2 2 2 
        2 2 1 f f f 2 2 2 
        2 2 1 f f f 2 2 2 
        2 2 1 f f f f 2 2 
        2 f f 2 f f f 2 2 
        f f 2 2 f 2 f f 2 
        `, SpriteKind.Food)
    pockyIs = 1
    for (let value of tiles.getTilesByType(myTiles.tile3)) {
        tiles.placeOnTile(Pocky, value)
    }
}
function initHUDtitle (hudSprite: Sprite) {
    hudSprite.z = 200
    hudSprite.setFlag(SpriteFlag.RelativeToCamera, true)
    hudSprite.left = 0
}
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
function Level1 () {
    scene.setBackgroundColor(7)
    tiles.setTilemap(tilemap`level_0`)
    spawnRandGrass()
    spawnKiddo()
    spawnPocky()
    tiles.placeOnTile(Kiddo, tiles.getTileLocation(0, 1))
    berriesIs = 0
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
    Level11()
})
function spawnRandGrass () {
    for (let value2 of tiles.getTilesByType(myTiles.tile1)) {
        if (randint(1, 3) == 1) {
            tiles.setTileAt(value2, myTiles.tile9)
        } else if (randint(1, 2) == 1) {
            tiles.setTileAt(value2, myTiles.tile7)
        } else if (randint(1, 2) == 1) {
            tiles.setTileAt(value2, myTiles.tile4)
        } else if (randint(1, 6) == 1) {
            tiles.setTileAt(value2, myTiles.tile5)
        } else if (randint(1, 6) == 1) {
            tiles.setTileAt(value2, myTiles.tile6)
        } else {
            tiles.setTileAt(value2, myTiles.tile8)
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
function Level11 () {
    destroySprites()
    scene.setBackgroundColor(7)
    tiles.setTilemap(tiles.createTilemap(hex`20002000030303030303030303030303030303050701010101010101010101010101010107010101010101010101010101010104010101010101010101010101010101010101080303030303030303030303030f03030303030303030303030305010101010104010e01010e01010e01010e01010e01010e01010e01010e0101040101010101040b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0104010101010104010a01010a01010a01010a01010a01010a01010a01010a010104010101010104010e01010e01010e01010e01010e01010e01010e01010e0107040101010101040b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0104010101010104010a01010a01010a01010a01010a01010a01010a01010a010104010101010104010e01010e01010e01010e01010e01010e01010e01010e0101040101010101040b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0104010101010104010a01010a01010a01010a01010a01010a01010a01010a0101040101010101060303030303030305010e0101010101070101010101010101010401010101010107010101010101040b0d0c0101010101010101010701010101040101010101010101010101010104010a010101010101010101010101010101040101010101010101010101010104010e0102030303030303030303030303030901010101010101010101010101040b0d0c010e01010e01010e01010e01010e01010e010101010101010107010104010a010b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0101010101010101010104010101010a01010a01010a01010a01010a01010a010107010101010101010104010e01010e01010e01010e01010e01010e0101010101010101010101010101040b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0101010101010803030303030309010a01010a01010a01010a01010a01010a0101010101010104010e01010e01010e01010e01010e01010e0101010101010101010101010101040b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0101010101010101010101010104010a01010a01010a01010a01010a01010a0101010e01010e01010e0107010104010e01010e01010e01010e01010e01010e01010b0d0c0b0d0c0b0d0c010101040b0d0c0b0d0c0b0d0c0b0d0c0b0d0c0b0d0c01010a01010a01010a0101010104010a01010a01010a01010a01010a01010a0101010e01010e01010e0101070104010101010101010101010101010101010101010b0d0c0b0d0c0b0d0c0101010401010101010101010101010101010101010101010a01010a01010a0101010106030303030303030303030303030303030303030303030303030303030101010101010101010101010101010101010101010101010101010101010101`, img`
        ................2...............
        2...............................
        ................................
        ................................
        ...222222222222222222222222.....
        ...2......................2.....
        ...2......................22....
        ...222222222222222222222222.....
        ...2......................2.....
        ...2......................2.....
        ...222222222222222222222222.....
        ...2.......222............2.....
        ...........2.2....2.............
        ...2.......222.........2........
        ...........222..................
        ...........2.2..................
        ...........222222222222222222222
        .......2...222222222222222222222
        ...........2.222.22.22.22.22.222
        .2.........222222222222222222...
        ...........222222222222222222...
        ...........22222.22.22.22.222...
        ....222222222222222222..........
        ....222222222222222222..........
        ....22.22222.22.22.222.222222222
        2...222222222222222222.222222222
        ....222222222222222222.22.22.222
        ....22.22222.22222.222.222222222
        .2.....................222222222
        .......................222222222
        ................................
        ................................
        `, [myTiles.transparency16,myTiles.tile1,myTiles.tile3,myTiles.tile10,myTiles.tile11,myTiles.tile12,myTiles.tile13,myTiles.tile17,myTiles.tile18,myTiles.tile19,myTiles.tile20,myTiles.tile21,myTiles.tile22,myTiles.tile23,myTiles.tile24,myTiles.tile25], TileScale.Sixteen))
    spawnRandGrass()
    spawnKiddo()
    spawnPocky()
    tiles.placeOnTile(Kiddo, tiles.getTileLocation(0, 0))
    berriesIs = 0
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    lastDirection = 2
    walk()
})
scene.onHitWall(SpriteKind.squirrel, function (sprite, location) {
    Squirrel.destroy()
    Berries.destroy()
    squirrelExit.destroy()
    squirrelIs = 0
})
scene.onHitWall(SpriteKind.Sword, function (sprite, location) {
    if (controller.A.isPressed()) {
        for (let value3 of [CollisionDirection.Left, CollisionDirection.Right, CollisionDirection.Top, CollisionDirection.Bottom]) {
            if (tiles.tileIs(tiles.locationInDirection(tiles.locationOfSprite(Trekking_Pole), value3), myTiles.tile17)) {
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
                    if (randint(0, 2) == 0) {
                        spawnSquirrel()
                    } else if (randint(0, 4) == 0) {
                        spawnBear()
                    }
                }
            }
        }
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    hungerPercent += 10
    if (hungerPercent > 100) {
        hungerPercent = 100
        healthPercent += 20
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
    BearHealth = 3
    bearIs = 1
}
function bearAnimate () {
    BearSprite.setImage(BearSprite.image)
    if (BearSprite.vx > 0 && BearSprite.x < Kiddo.x) {
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
sprites.onOverlap(SpriteKind.squirrel, SpriteKind.exit, function (sprite, otherSprite) {
    otherSprite.destroy()
    Berries.destroy()
    Squirrel.destroy()
    squirrelIs = 0
})
function destroySprites () {
    Kiddo.destroy()
    if (berriesIs > 0) {
        berriesIs = 0
        Berries.destroy()
    }
    if (squirrelIs > 0) {
        squirrelIs = 0
        Squirrel.destroy()
    }
    if (bearIs > 0) {
        bearIs = 0
        BearSprite.destroy()
    }
    if (pockyIs > 0) {
        pockyIs = 0
        Pocky.destroy()
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.squirrel, function (sprite, otherSprite) {
    healthPercent += -5
    pause(1000)
})
sprites.onDestroyed(SpriteKind.Timer, function (sprite) {
    animation.stopAnimation(animation.AnimationTypes.All, Kiddo)
    walk()
})
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
    if (Squirrel.vx > 0 && Squirrel.x < Kiddo.x) {
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
    } else {
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
    }
}
let moving = false
let squirrelHealth = 0
let squirrelIs = 0
let squirrelExit: Sprite = null
let Berries: Sprite = null
let fillWidth = 0
let berriesIs = 0
let timer: Sprite = null
let kiddoIntro: Sprite = null
let daddoIntro: Sprite = null
let Trekking_Pole: Sprite = null
let hungerPercent = 0
let meterWidth = 0
let hungerTitle: Sprite = null
let healthBar: Sprite = null
let hungerBar: Sprite = null
let pockyIs = 0
let Pocky: Sprite = null
let bearSteak: Sprite = null
let bearIs = 0
let BearHealth = 0
let Kiddo: Sprite = null
let Squirrel: Sprite = null
let lastDirection = 0
let BearSprite: Sprite = null
let healthPercent = 0
intro()
Level1()
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
        Kiddo.say("I literally didn't eat anything today", 2000)
    } else if (hungerPercent == 15) {
        Kiddo.say("I'M DYING...", 1000)
    }
    if (healthPercent == 50) {
        Kiddo.say("I'm bleeding!", 1000)
    } else if (healthPercent == 25) {
        Kiddo.say("Tell the cats I love them!", 2000)
    } else if (healthPercent == 0) {
        game.over(false, effects.melt)
    }
})
game.onUpdateInterval(500, function () {
    hungerPercent += -0.75
    drawHUDMeter(hungerPercent, hungerBar, 4, 14)
    drawHUDMeter(healthPercent, healthBar, 3, 2)
    if (bearIs == 1) {
        bearAnimate()
    }
    if (squirrelIs == 1) {
        squirrelAnimate()
    }
    if (hungerPercent <= 0) {
        healthPercent += -5
    }
})
