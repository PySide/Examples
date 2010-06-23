'''
Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
All rights reserved.
Contact: Nokia Corporation (qt-info@nokia.com)
Ported by PySide team (pyside@openbossa.org)

This file is part of the Qt Mobility Components.

$QT_BEGIN_LICENSE:BSD$
You may use this file under the terms of the BSD license as follows:

"Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.
  * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
    the names of its contributors may be used to endorse or promote
    products derived from this software without specific prior written
    permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
$QT_END_LICENSE$
'''

import sys

from PySide.QtCore import *
from QtMobility.Sensors import *

class RotationFilter(QRotationFilter):
    stamp = qtimestamp()

    def filter(self, reading):
        diff = ( reading.timestamp() - stamp )
        stamp = reading.timestamp()
        print "Rotation: %.2f x" % reading.x(),
              " %.2f y" % reading.y(),
              " %.2f z" % reading.z(),
              " (%.2f ms since last, " % diff / 1000,
              "%.2f Hz)" % 1000000.0 / diff

        return true

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    args = app.arguments()
    rate_place = args.indexOf("-r")
    rate_val = 0;

    if (rate_place != -1):
        rate_val = args.at(rate_place + 1).toInt()

    sensor = QRotationSensor()

    if (rate_val > 0)
        sensor.setDataRate(rate_val)

    filter = RotationFilter()
    sensor.addFilter(filter)
    sensor.start()

    if (!sensor.isActive())
        qWarning("Rotationsensor didn't start!")
        return 1

    if (sensor.property("hasZ").isValid()):
        if (sensor.property("hasZ").toBool()):
            qDebug("Sensor hasZ is set")
        else:
            qDebug("Sensor hasZ is NOT set")
    else:
        qDebug("Sensor hasZ error: no value")

    return app.exec_()
