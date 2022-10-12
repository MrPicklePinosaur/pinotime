# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2020 Daniel Thompson

"""Terminal Clock
~~~~~~~~~~~~~~~~
Inspired by this post https://www.reddit.com/r/unixporn/comments/9ndo8o/oc_always_keep_some_terminal_with_you/

Displays time among other helpful information

.. figure:: res/TermClockApp.png
    :width: 179

"""

import wasp
import fonts
import icons

MONTH = 'JanFebMarAprMayJunJulAugSepOctNovDec'

class TermClockApp():
    """Simple digital clock application."""
    NAME = 'TermClock'
    ICON = icons.clock

    def foreground(self):
        """Activate the application.

        Configure the status bar, redraw the display and request a periodic
        tick callback every second.
        """
        wasp.system.bar.clock = False
        self._draw(True)
        wasp.system.request_tick(1000)

    def sleep(self):
        """Prepare to enter the low power mode.

        :returns: True, which tells the system manager not to automatically
                  switch to the default application before sleeping.
        """
        return True

    def wake(self):
        """Return from low power mode.

        Time will have changes whilst we have been asleep so we must
        udpate the display (but there is no need for a full redraw because
        the display RAM is preserved during a sleep.
        """
        self._draw()

    def tick(self, ticks):
        """Periodic callback to update the display."""
        self._draw()

    def preview(self):
        """Provide a preview for the watch face selection."""
        wasp.system.bar.clock = False
        self._draw(True)

    def _draw(self, redraw=False):
        """Draw or lazily update the display.

        The updates are as lazy by default and avoid spending time redrawing
        if the time on display has not changed. However if redraw is set to
        True then a full redraw is be performed.
        """

        draw = wasp.watch.drawable
        draw.set_font(fonts.source18) # size 18 font spacing 2

        if redraw:
            now = wasp.watch.rtc.get_localtime()

            # Clear the display and draw that static parts of the watch face
            draw.fill()
            draw.set_color(0xffff)
            draw.string("watch > fetch", 0, 40)
            draw.string('[TIME]', 0, 60)
            draw.string('[DATE]', 0, 80)
            draw.string('[BATT]', 0, 100)
            draw.string('[STEP]', 0, 120)
            draw.string('[HRTR]', 0, 140)
            draw.string("watch >", 0, 160)

            # Redraw the status bar
            wasp.system.bar.draw()
        else:
            # The update is doubly lazy... we update the status bar and if
            # the status bus update reports a change in the time of day 
            # then we compare the minute on display to make sure we 
            # only update the main clock once per minute.
            now = wasp.system.bar.update()
            if not now or self._min == now[4]:
                # Skip the update
                return

        hor_off = fonts.source18.max_width()*7
        # Format the month as text
        month = now[1] - 1
        month = MONTH[month*3:(month+1)*3]

        # Draw the changeable parts of the watch face
        # this is really stupid rn
        draw.set_color(0xff00)
        draw.string('{}{}:{}{}'.format(
            now[3]//10, now[3]%10, now[4]//10, now[4]%10), hor_off, 60)

        draw.set_color(0x0ff0)
        draw.string('{} {} {}'.format(now[2], month, now[0]), hor_off, 80)

        # draw.set_color(0x0f00)
        # draw.string('{}%'.format(wasp.system.bar.battery_level), hor_off, 100)

        draw.set_color(0xf0f0)
        draw.string('1301 steps', hor_off, 120)

        draw.set_color(0xf000)
        draw.string('0 bpm', hor_off, 140)

        # Record the minute that is currently being displayed
        self._min = now[4]

        
