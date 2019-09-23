#saves values from serial to file and print to terminal



from serial import Serial
import time



ser =Serial(
    port='/dev/ttyACM0',
    baudrate = 115200,
    timeout=None)
def adddata(data):
    '''a function to add the data to the text file'''
    date=time.time()
    h=str(data)+','+str(date)+'\n'
    fh = open('output.txt', 'a')
    fh.write(h) 
    fh.close 
while 1:
    ''' infinit loop'''
    while(ser.inWaiting()==0):
        '''wait for the data from serial'''
        pass
    # a=float(ser.readline().decode('utf-8'))
    '''read and decode the data'''
    line=ser.readline().decode('utf-8')
    line=line.rstrip()
    count = line.count(",")

    #parse if theres enough values
    if (count==6):
        print(line)
        '''add the data to the txt file'''
        adddata(line)
    else:
        print("The count is:", count)