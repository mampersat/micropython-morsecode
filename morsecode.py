import machine,time

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
}

def flash(led,t):
    led.low()
    time.sleep(t)
    led.high()
    time.sleep(t)
    return

def send(msg="SOS",pin=2,tdot = 0.1):
    led = machine.Pin(pin,machine.Pin.OUT)

    tdash = tdot * 3
    tspace = tdot * 2
    tword = tdot * 6

    for l in msg:
        c = CODE.get(l.upper())
        for e in c:
           if e==".":flash(led,tdot)
           if e=="-":flash(led,tdash)
           if e==" ":flash(led,tspace)
        time.sleep(tword)
