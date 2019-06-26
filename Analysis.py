import tensorflow
import Server as myserver

list = []


def add(ch1, ch2, ch3, ch4, ch5):
    temp = [ch1, ch2, ch3, ch4, ch5]
    list.append(temp)
    print(list)


def main():
    print("running main method in Analysis Class")
    myserver.main()
    print("i'm here")
    while True:
        print(list)


if __name__ == "__main__":
    main()
