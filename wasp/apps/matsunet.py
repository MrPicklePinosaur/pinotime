# SPDX-License-Identifier: MY-LICENSE
# Copyright (C) YEAR(S), AUTHOR

"""MatsuNet
~~~~~~~~~~~~~~~

Control devices using smartwatch.

    .. figure:: res/MatsuNetApp.png
        :width: 179

"""

import wasp
import icons
import time
from widgets import Button

class MatsuNetApp(object):
    """App to control devices"""
    NAME = "MatsuNet"
    ICON = icons.app

    def __init__(self):
        self.msg = "Hello MatsuNet"
        self._lock_btn = Button(75, 108, 90, 45, 'lock')

    def background(self):
        pass

    def foreground(self):
        self._draw()
        wasp.system.request_event(wasp.EventMask.TOUCH)

    def draw(self):
        self._draw()

    def _draw(self):
        draw = wasp.watch.drawable
        draw.fill()
        draw.string(self.msg, 0, 60, width=240)
        self._lock_btn.draw()

    def touch(self, event):
        if self._lock_btn.touch(event):
            self._send_cmd('{"t":"lock_screen"}')

    def tick(self, ticks):
        pass

    def press(self, button, state):
        pass

    def swipe(self, event):
        pass

    # this is duplicated code from musicplayer.py
    def _send_cmd(self, cmd):
        print('\r')
        for i in range(1):
            for i in range(0, len(cmd), 20):
                print(cmd[i: i + 20], end='')
                time.sleep(0.2)
            print(' ')
        print(' ')

