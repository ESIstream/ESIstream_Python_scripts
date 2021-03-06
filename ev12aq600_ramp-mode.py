#!/usr/bin/env python
import os
import sys
import time
from ev12aq600 import ev12aq600

app=ev12aq600()

app.start_serial()

app.deactivate_ev12aq600_rstn()

app.spi_ss_ev12aq600()
app.ev12aq600_configuration_ramp_mode()
app.rst_check_pulse()

app.stop_serial()

