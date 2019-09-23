import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import datetime as dta
'''configuring the plot'''
style.use('ggplot')
fig, axs = plt.subplots(7)
# fig, axs = plt.subplots(7,sharex=True)



def animate(i):
    dateconv = dta.datetime.fromtimestamp
    '''define the function that gonna convert the unix time to date'''
    graph_data = open('output.txt','r').read()
    '''read the data from the txt file'''
    lines = graph_data.split('\n') #split the lines as a list
    temp1s = [] # y axis the tempurature1
    temp2s = [] # y axis the tempurature2
    v1s = [] # y axis for voltages1
    v2s = [] # y axis for voltages2
    v3s = [] # y axis for voltages3
    v4s = [] # y axis for voltages4
    v5s = [] # y axis for voltages5
    dates = [] # x axis the date

    for line in lines:
        ''' read the lines and append the data to ys ans xs'''
        if len(line) > 1:
            '''get only the non-empty line'''
            v1,v2,v3,v4,v5,temp1,temp2, date = line.split(',')
            # temp1=float(temp1)
            # temps.append(temp1)

            temp1s.append(float(temp1))

            # temp1=float(temp2)
            temp2s.append(float(temp2))


            v1s.append(float(v1))
            v2s.append(float(v2))
            v3s.append(float(v3))
            v4s.append(float(v4))
            v5s.append(float(v5))
            # # v1=float(v1)
            # # v1s.append(v1)

            # v2=float(v2)
            # v2s.append(v2)

            date=float(date)
            date = dateconv(date) #converte the unix time
            dates.append(date)
    
    '''plot the data'''
    axs[0].clear()
    axs[0].plot(dates[-1000:], temp1s[-1000:],label='temperature')
    axs[1].clear()
    axs[1].plot(dates[-1000:], temp2s[-1000:],label='temperature')

    axs[2].clear()
    axs[2].plot(dates[-1000:], v1s[-1000:],label='v1')
    axs[3].clear()
    axs[3].plot(dates[-1000:], v2s[-1000:],label='v2')
    axs[4].clear()
    axs[4].plot(dates[-1000:], v3s[-1000:],label='v3')
    axs[5].clear()
    axs[5].plot(dates[-1000:], v4s[-1000:],label='v4')
    axs[6].clear()
    axs[6].plot(dates[-1000:], v5s[-1000:],label='v5')

    # for label in axs[1].xaxis.get_ticklabels():
    #     '''set the rotation of the date into 45 degree in order to be readable'''
    #     label.set_rotation(45)
    
    axs.flat[0].set(ylabel='temp1')
    axs.flat[1].set(ylabel='temp2')

    axs.flat[2].set(ylabel='v1')
    axs.flat[3].set(ylabel='v2')
    axs.flat[4].set(ylabel='v3')
    axs.flat[5].set(ylabel='v4')
    axs.flat[6].set(ylabel='v5')

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()