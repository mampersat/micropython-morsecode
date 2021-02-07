import machine,time

wpm=15
CODE = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
    'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
    'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
    'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
    '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
    '.':'.-.-.-',
    ',':'--..--',
    '?':'..--..',
    '/':'--..-.',
    '@':'.--.-.',
    ' ':' ',
}

def flash(led,t):
#    led.low()
#    time.sleep(t)
    led.high()
    time.sleep(t)
    led.low()
    return

def send(msg="SOS",pin=25,tdot = 1.2/wpm):
    led = machine.Pin(pin,machine.Pin.OUT)

    tdash = tdot * 3
    tspace = tdot * 2
    tword = tdot * 6

    led.low()
    for l in msg:
        c = CODE.get(l.upper())
        for e in c:
           if e==".":
               flash(led,tdot)
               time.sleep(tdot)
           if e=="-":
               flash(led,tdash)
               time.sleep(tdot)
           if e==" ": time.sleep(tword)
        time.sleep(tword)
    led.low()    
