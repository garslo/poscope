# poscope #

poscope is a software-based oscilloscope written as part of an
advanced physics laboratory project at Grand Valley State University. It
was part of my final project in the course in lieu of an independent
experiment. It exists here simply as a curiosity.

# Purpose #

poscope measures voltage changes over time and displays a real-time
graph of these in the gui interface. The program uses a National
Instruments NI6009 data acquisition device (DAQ) to read the voltages
via the the [NiDAQmx](http://www.ni.com/dataacquisition/nidaqmx.htm)
API, adapted to Python by the
[PyDAQmx](http://pythonhosted.org/PyDAQmx/) bindings. The interface is
written in [Qt4](http://qt.digia.com/) using
[PyQt4](http://www.riverbankcomputing.com/software/pyqt/download), and
the raw data is crunched using [NumPy](http://www.numpy.org/).

poscope was written mainly to grasp an understanding of how
oscilloscopes work and *not* to be a practical oscilloscope. As such,
programming best practices were not necessarily followed. While I
tried to keep things sane, inevitably the learning-oriented focus
interfered with proper program design. So, **don't use poscope if you
need something dependable.** Use a real oscilloscope, software or
otherwise.

It has been a while since I've written this and I don't have access to
an NI6009 to test things, so I don't know the state of the program. It
works to a satisfactory degree, else I would not have passed my class
:) but beyond that I'm not sure. If you're curious, feel free to poke
around!

# More Information #

In the `report/` directory you can find my lab report on poscope. It's
a short analysis and explanation of what poscope is, what it can do,
how it does some of those things, and what it's shortcomings
are. Please look through it if you're at all interested. You can
download a pdf version or the original LaTeX source.
