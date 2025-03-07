from morsecode import Morse

def main() -> None:
    code = Morse(12, 20)
    code.send("Hello World!")

if __name__ == "__main__":
    main()