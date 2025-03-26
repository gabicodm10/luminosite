basic.forever(function () {
    if (input.lightLevel() < 200) {
        basic.showString("sombre")
    } else {
        basic.showString("lumineux")
    }
})
