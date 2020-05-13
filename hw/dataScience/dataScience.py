import socket
from threading import *

def get_title(line_lst):
    res = line_lst[4].split()
    return res[0] + ','
def get_cabin(line_lst):
    return line_lst[11] != '' + ','
def over_30(line_lst):
    if(isinstance(line_lst[6], int)):
        return int(line_lst[6]) >= 30 + ','
    return "n/a,"
def under_30(line_lst):
    if(isinstance(line_lst[6], int)):
        return int(line_lst[6]) < 30 + ','
    return "n/a,"
def fare_over_50(line_lst):
    if(isinstance(line_lst[10], int)):
        return int(line_lst[10]) >= 50
    return 'n/a'

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.s = socket
        self.addr = address
        self.start()
    def run(self):
        while 1:
            print('Message Received: ', self.s.recv(1024).decode())



def main():
    file = open('train.csv', 'r')
    lst = []
    header = file.readline().split(',')
    #print(header)
    header.insert(4, 'First Name')
    header.insert(4, 'Last Name')
    header.pop(6)

    #modify header
    header.append('Title')
    header.append('Had Cabin')
    header.append('Age >= 30')
    header.append('Age < 30')
    header.append('Fare >= 50')

    #turn header into string and add to lst
    string_header = ','.join(header)
    string_header.rstrip(',')
    string_header+='\n'
    #print("header: ", string_header)
    lst.append(''.join(string_header))

    next(file)
    for line in file:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('chalbroker.cs1122.engineering.nyu.edu', 3545))
        line_lst = line.split(',')

        #get 5 columns
        title = str(get_title(line_lst))
        had_cabin = str(get_cabin(line_lst))
        over_30_var = str(over_30(line_lst))
        under_30_var = str(under_30(line_lst))
        fare_over_50_var = str(fare_over_50(line_lst))

        #add 5 columns
        curr_line = file.readline().split(',')
        curr_line.append(title)
        curr_line.append(had_cabin)
        curr_line.append(over_30_var)
        curr_line.append(under_30_var)
        curr_line.append(fare_over_50_var)

        curr_line_str = ','.join(curr_line)+','

        curr_line_str.rstrip(',')
        curr_line_str+='\n'
        s.send(bytes(curr_line_str, 'utf-8'))

    s.send(bytes('...x\n', 'utf-8'))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025))
s.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = s.accept()
    client(clientsocket, address)











main()
