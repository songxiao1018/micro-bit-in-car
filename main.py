def on_received_number(receivedNumber):
    if receivedNumber == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    if receivedNumber == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    if receivedNumber == 2:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
    if receivedNumber == 3:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    if receivedNumber == 4:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
radio.on_received_number(on_received_number)

radio.set_group(1)

def on_forever():
    basic.show_leds("""
                . . # . .
                . # # . .
                . . # . .
                . . # . .
                . # # # .
    """)
basic.forever(on_forever)
