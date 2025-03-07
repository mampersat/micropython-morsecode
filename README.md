MicroPython Morse Code
======================

## Blink an LED with morse coded message
The library contains a class called Morse, this class has 2 functions, `flash()` which flashes the the pin specified when initializing the class for a the period of time specified in the arguments of the function, and the second function, `send()` that takes in the message you want to flash as an argument and flashes it the pin specified when initializing the class.

### Default values
| Function | Value       | Value 2  |
|----------|-------------|----------|
| __init__ | pin = 25    | wpm = 15 |
| flash    | t = 0.5     |          |
| send     | msg = "SOS" |          |

## Example main.py
Blink the phrase 'Hello World!" in morse code

```py
from morsecode import Morse

def main() -> None:
    code = Morse(12, 20) # Initialize with pin 12 and 20 WPM
    code.send("Hello World!") # Send the message "Hello World!" in Morse code

if __name__ == "__main__":
    main() # Run the main function
```
