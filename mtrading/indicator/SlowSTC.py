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


class SlowSTC(Indicator):

    # Set the default initialization. The first one is executed.
    def initialize(self):
        self.options = [9, 3, 3]
        self.displays = ["SK", "SD"]

    # It generates indicators that is used internally. The first one is executed.
    def declare_using(self):
        self.ind1 = XAverage(self, self.options[1], "FK")
        self.ind2 = XAverage(self, self.options[2], "SK")

    # The computation is executed each time data is added or changed.
    def calculating(self):
        length = self.options[0]
        highest = self.highest("H", length)
        lowest = self.lowest("L", length)

        self.lines["FK"] = (self.lines["C"] - lowest) / (highest - lowest) * 100.0

        self.ind1.calculate()
        self.lines["SK"] = self.ind1.lines["XAverage"]

        self.ind2.calculate()
        self.lines["SD"] = self.ind2.lines["XAverage"]
