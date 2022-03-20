import datetime
import csv


def read_jtl_with_csv():

    successful_records = []
    failed_records = []
    print_message = []
    files = ['Jmeter_log1.jtl','Jmeter_log2.jtl']
    for file in files:
        with open('Jmeter_log1.jtl', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for line in csv_reader:
                # print(line[3])
                if '200' in line:
                    successful_records.append(line)
                else:
                    failed_records.append(line)
                    print_message = (line[2] + " failed with response code:" + line[3] + " and response message is:" + line[4] + " Failure message is:" + line[8] + " at " + str(convert_timestamp(line[0])) + ' PST')
                    print(print_message)


def convert_timestamp(timestamp):

    number = int(timestamp)
    coverted_number = number % 1e7
    converted_timestamp = convert_timestamp_to_pst(coverted_number)
    return converted_timestamp


def convert_timestamp_to_pst(a):

    date_time = datetime.datetime.fromtimestamp(a)
    return date_time


if __name__ == '__main__':
    read_jtl_with_csv()
    # convert_timestamp_to_pst(161287.9363730)
