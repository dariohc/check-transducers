__author__ = 'Dario Hermida'
import csv

line_limit = 10000
line_counter = 0
my_serial_list = []

with open('Transducers - Copy.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        # print(row)
        # print(row['Serial Number'])
        my_serial_list.append(row['Serial Number'])
        line_counter += 1
print('Total lines read:', len(my_serial_list))
for index in range(len(my_serial_list)):
    # print('estoy viendo el elemento', my_serial_list[index])
    # print(my_serial_list.count(my_serial_list[index]))
    if my_serial_list.count(my_serial_list[index]) > 1 and my_serial_list[index] != '0':
        print('there is something wrong with:', my_serial_list[index])
input('If Jappy with the result, press any key to finish')
