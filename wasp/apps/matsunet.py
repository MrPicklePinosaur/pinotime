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

class MatsuNetApp():
    """App to control devices"""
    NAME = "MatsuNet"
    ICON = icons.app

    def __init__(self):
        self.msg = "Hello MatsuNet"

    def background(self):
        pass

    def foreground(self):
        self._draw()

    def _draw(self):
        draw = wasp.watch.drawable
        draw.fill()
        draw.string(self.msg, 0, 108, width=240)

    def touch(self, event):
        pass

    def tick(self, ticks):
        pass

    def press(self, button, state):
        pass

    def swipe(self, event):
        pass
