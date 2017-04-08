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
from mtrading.indicator.TrueRange import *
from mtrading.indicator.NAverage import *


class ATR(Indicator):

    # Set the default initialization. The first one is executed.
    def initialize(self):
        self.options = [14]
        self.displays = ["ATR"]

    # It generates indicators that is used internally. The first one is executed.
    def declare_using(self):
        self.ind1 = TrueRange(self, None, None,("TrueRange", "__ATR_TR"))
        self.ind2 = NAverage(self, self.options[0], "__ATR_TR", ("NAverage", "ATR"))

    # The computation is executed each time data is added or changed.
    def calculating(self):
        self.ind1.calculate()
        self.ind2.calculate()
