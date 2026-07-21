import sys

if __name__ == '__main__':
    args = sys.argv
    args = [bool(int(i)) for i in args[1:]]
    print("This is an example script which can be used in the markdown as a code template")
