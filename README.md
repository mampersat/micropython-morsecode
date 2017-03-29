MicroPython Morse Code
======================

Blink an LED with morse coded message

```
import morsecode
import network

while True:
  # get last 3 digits of IP address
  s = network.WLAN().ifconfig()[0].split('.')[3] + ' '

  # send morse code
  morsecode.send(s)
```
