# -*- Mode: Python; tab-width: 4 -*-
#       Author: Michaels Kim<michaelskim2016@gmail.com>

# ======================================================================
# Copyright 2016 by Michaels Kim
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Sam
# Rushing not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# MICHAELS KIM RUSHING DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL SAM RUSHING BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# ======================================================================
from mtrading.core import *
from mtrading.indicator.XAverage import *


class WilliamsR(Indicator):

    # Set the default initialization. The first one is executed.
    def initialize(self):
        self.options = [15, 5]
        self.displays = ["WR", "WD"]

    def declare_using(self):
        self.ind1 = XAverage(self, self.options[1], "WR")

    def calculating(self):
        length = self.options[0]
        highest = self.highest("H", length)
        lowest = self.lowest("L", length)

        self.lines["WR"] = (highest - self.lines["C"]) * (-100.0) / (highest - lowest)

        self.ind1.calculate()
        self.lines["WD"] = self.ind1.lines["XAverage"]
