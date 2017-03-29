MicroPython Morse Code
======================

Blink an LED with morse coded message

.. code-block:: python

  import morsecode
  import network

  while True:
    # get last 3 digits of IP address
    s = network.WLAN().ifconfig()[0].split('.')[3] + ' '
    led.flash_msg(s)
