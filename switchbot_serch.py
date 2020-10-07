import binascii
from bluepy.btle import Peripheral
 

p = Peripheral("E0:F6:18:B6:3F:9A", "random")
hand_service = p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")
hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]
hand.write(binascii.a2b_hex("570100"))
p.disconnect()
