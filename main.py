def on_forever():
    if led.brightness() < 200:
        basic.show_string("sombre")
    else:
        basic.show_string("lumineux")
basic.forever(on_forever)
