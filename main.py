import datetime
import json
import xml.etree.ElementTree as et
from dateutil.relativedelta import *
import datetime as dt


def read_xml_using_elementtree(x, y):

    print(f'Updating Departure Date and Return Date in test_payload.xml')  # Press ⌘F8 to toggle the breakpoint.

    my_tree = et.parse('test_payload1.xml')
    my_root = my_tree.getroot()

    for x in my_root[0]:
        if 'TP' in str(x.tag):
            depart_date = x.find('DEPART').text
            # print(f'Current Departure date is : ' + depart_date)
            depart_date = generate_future_date(10)
            print(f'Future Departure date is : ' + depart_date)
            x.find('DEPART').text = str(depart_date)

            return_date = x.find('RETURN').text
            # print(f'Current Return date is : ' + return_date)
            return_date = generate_future_date(40)
            print(f'Future Return date is : ' + return_date)
            x.find('RETURN').text = str(return_date)
        my_tree.write('updated_test_payload1.xml')


def generate_future_date(a):

    date_generated = (datetime.date.today() + relativedelta(days=+a)).strftime('%Y%m%d')
    # print(f'Date Generated: '+date_generated)
    return date_generated


def replace_json_element(list_obj, key):

    with open('test_payload.json') as json_data:
        data = json.load(json_data)

    if isinstance(data, dict):
        for a in list_obj:
            if a in data:
                json_data = data[a]
                if isinstance(json_data, dict):
                    for y in json_data:
                        if key in y:
                            print(key)
                            del data[a][key]
                            break
                elif isinstance(json_data, list):
                    del data[a]

    with open('updated.json', 'w') as f:
        json.dump(data, f, indent=2)

