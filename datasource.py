#  datasource.py
#
#  Copyright 2013 Gary Slopsema
#
#  This file is part of poscope.
#
#  poscope is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  poscope is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with poscope. If not, see <http://www.gnu.org/licenses/>.


import numpy as np
import PyDAQmx
import PyDAQmx.DAQmxConstants as daqc
import PyDAQmx.DAQmxTypes as daqt

class GeneratedData:
    def __init__(self):
        self.xs = np.arange(0, 10, 0.1)
        self.acc = 0
        self.incrementor = 0.1

    def data(self):
        self.acc += self.incrementor
        return (self.xs, np.sin(self.xs + self.acc))

class NI6009:
    def __init__(self):
        # How many samples for each Task()?
        self.reads_per_run = 1000
        # samples/second
        self.sample_rate = 1000
        # (min, max) I *think* the NI 6009 only handles 0 to 5.
        self.voltages = (0.0, 5.0)
        # Holds the sample data
        self.raw_data = np.zeros(self.reads_per_run, dtype = np.float64)
        # Main task instance. Currently we're creating a new one for each
        # read, check if can reuse.
        self.task = None
        self.dev = 'Dev1/ai0'
        self.timeout = 10.0
        self.have_read = daqt.int32()

    def _setup_task(self):
        self.task = PyDAQmx.Task()
        self.task.CreateAIVoltageChan(self.dev, '',
                                      daqc.DAQmx_Val_Cfg_Default,
                                      self.voltages[0], self.voltages[1],
                                      daqc.DAQmx_Val_Volts, None)
        self.task.CfgSampClkTiming(None, self.sample_rate,
                                   daqc.DAQmx_Val_Rising,
                                   daqc.DAQmx_Val_FiniteSamps,
                                   self.reads_per_run)

    def data(self):
        self._setup_task()
        self.task.StartTask()
        self.task.ReadAnalogF64(self.reads_per_run, self.timeout,
                                daqc.DAQmx_Val_GroupByChannel,
                                self.raw_data, self.reads_per_run,
                                daqt.byref(self.have_read), None)
        return self.raw_data
