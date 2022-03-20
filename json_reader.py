# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def json_reader(x, y):
    print(f'Hi, {x, y}')  # Press ⌘F8 to toggle the breakpoint.

    with open('test_payload.json', 'r') as myfile:
        jsonfile = myfile.read()

    jsondata = json.loads(jsonfile)
    print(jsondata)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    json_reader(1, 2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
