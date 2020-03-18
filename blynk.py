import blynklib

BLYNK_AUTH = '9HIeo403qLUzAKi5UYIpCCiAy7C7nJeK'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"


# register handler for virtual pin V4 write event
@blynk.handle_event('write V0')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))


###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()


