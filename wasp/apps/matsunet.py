# SPDX-License-Identifier: MY-LICENSE
# Copyright (C) YEAR(S), AUTHOR

import wasp

class MatsuNetApp():
    """App to control devices"""
    NAME = "MatsuNet"

    def __init__(self, msg="Hello MatsuNet"):
        self.msg = msg

    def foreground(self):
        self._draw()

    def _draw(self):
        draw = wasp.watch.drawable
        draw.fill()
        draw.string(self.msg, 0, 108, width=240)
