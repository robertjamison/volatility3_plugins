"""
Sample python file that some python strings and dictionaries in memory.
"""

from time import sleep

string1 = "This is a python string that should be extracted"
string2 = "This is another python string that should be extracted"

the_dict = {"this is the key": "this is the value",
            "this is another key": "this is another value"}

if __name__ == "__main__":
    while True:
        print(string1, string2)
        print(string2)
        print(the_dict)
        sleep(60)
