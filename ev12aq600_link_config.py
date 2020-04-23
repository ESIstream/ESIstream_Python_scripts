#!/usr/bin/env python
import os
import sys
import time
from ev12aq600 import ev12aq600

app=ev12aq600()

app.start_serial()

app.ev12aq600_rstn_pulse()
app.rx_prbs_enable()
app.ev12aq600_sync_sampling_on_negative_edge()
app.sync_mode_training()
app.sync_pulse()

app.stop_serial()

