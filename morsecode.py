from machine import Pin
from time import sleep

CODE = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '.' : '.-.-.-',
    ',' : '--..--',
    '?' : '..--..',
    '/' : '--..-.',
    '@' : '.--.-.',
    '!' : '-.-.--',
    ' ' : ' '
}

class Morse:
    def __init__(self, pin = 25, wpm = 15):
        self.led = Pin(pin, Pin.OUT)
        self.wpm = wpm

    def flash(self, t = 0.5):
        self.led.on()
        sleep(t)
        self.led.off()
        return

    def send(self, msg = "SOS"):
        tdot = 1.2/self.wpm
        tdash = tdot * 3
        tspace = tdot * 2
        tword = tdot * 6

        self.led.off()
        for l in msg:
            c = CODE.get(l.upper())
            for e in c:
                if e==".":
                    self.flash(tdot)
                    sleep(tdot)
                if e=="-":
                    self.flash(tdash)
                    sleep(tdot)
                if e==" ": sleep(tword)
                sleep(tword)
        self.led.off()    
