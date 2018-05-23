from numpy import sin, linspace, pi, append
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import arange
from scipy.fftpack import fft, fftfreq
from scipy.interpolate import interp1d


def plot_spectrum(y, timestep):
    frq = fftfreq(len(y), timestep)
    Y = fft(y)

    # two sides -> one side frequency range
    n = len(y)
    frq = frq[range(n / 2)]
    Y = Y[range(n / 2)]

    # get natural frequency
    Y_list = list(abs(item) for item in Y)
    f_n = frq[Y_list.index(max(Y_list))]
    print('Abaqus frequency : ' + str(f_n))
    print('Abaqus wavelength : ' + str(1/f_n))

    plot(frq, abs(Y), 'r')  # plotting the spectrum
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')

def test():
    Fs = 150.0;  # sampling rate
    Ts = 1.0 / Fs;  # sampling interval
    t = arange(0, 6, Ts)  # time vector

    ff = 5.5;  # frequency of the signal
    y = sin(2 * pi * ff * t)
    #y = sin(2 * pi * 10 * t) + sin(2 * pi * 15 * t) + sin(2 * pi * 20 * t) + sin(2 * pi * 25 * t)

    #t = append(t, arange(5,6,Ts))
    #y = append(y, [0 for a in arange(5,6,Ts)])

    subplot(2, 1, 1)
    plot(t, y)
    xlabel('Time')
    ylabel('Amplitude')
    subplot(2, 1, 2)
    plot_spectrum(y, 1/Fs)
    show()

def plot_results(x, y):
    y_f = interp1d(x,y)

    timestep = 0.001
    x_ = arange(min(x), max(x), timestep)
    y_ = y_f(x_)

    x_ = append(x_, arange(max(x), max(x)+1, timestep))
    y_ = append(y_, [0 for a in arange(max(x), max(x)+1, 0.001)])
    #y_ = append(y_, y_)

    subplot(2, 1, 1)
    plot(x_, y_)
    xlabel('Time')
    ylabel('Amplitude')
    subplot(2, 1, 2)
    plot_spectrum(y_, timestep)
    show()

#plot_results('results/2018_5_14--15_13_807000.txt')
