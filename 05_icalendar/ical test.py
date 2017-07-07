#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
read & write VCAL files (.05_icalendar).

shenbo@hotmail.com
@ 2017.06.02
"""

from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC  # timezone

import os

directory = os.path.dirname(__file__)


def readics(filename):
    with open(os.path.join(directory, filename), 'rb') as fp:
        data = fp.read().decode(encoding='utf-8')
    cal = Calendar.from_ical(data)
    return cal


def test(cal):
    for ve in cal.walk('vevent'):
        summ = ve.decoded('summary').decode(encoding='utf-8')

        summ = summ.replace('\n', ' ')
        summ = summ.replace('*', ' ')
        summ = summ.replace('>', ' ')
        summ = summ.replace('/', ' ')
        summ = summ.replace(':', ' ')
        summ = summ.replace('@', ' ')

        date = ve.decoded('dtstart')
        ymd = date.strftime('%Y%m%d')
        filename = '{1} {0}.md'.format(summ, ymd)

        print(filename)

        filedata = '---\ntitle: {} \ndate: {} \ntags: {} \n---'.format(summ, date, '')

        folderpath = os.path.join(directory + '\\md\\')
        isfolderexists = os.path.exists(folderpath)
        if not isfolderexists:
            os.makedirs(folderpath)
        with open(os.path.join(folderpath, filename), 'wb') as fd:
            fd.write(bytes(filedata, 'UTF-8'))


def addevent():
    cal = Calendar()
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('version', '2.0')

    event = Event()
    event.add('summary', 'Python meeting about calendaring')
    event.add('dtstart', datetime(2005, 4, 4, 8, 0, 0, tzinfo=UTC))
    event.add('dtend', datetime(2005, 4, 4, 10, 0, 0, tzinfo=UTC))
    event.add('dtstamp', datetime(2005, 4, 4, 0, 10, 0, tzinfo=UTC))
    event['uid'] = '20050115T101010/27346262376@mxm.dk'
    event.add('priority', 5)

    cal.add_component(event)

    with open(os.path.join(directory, 'example.05_icalendar'), 'wb') as fd:
        fd.write(bytes(cal.to_ical(), 'UTF-8'))


if __name__ == '__main__':
    ical = readics('shenbo.05_icalendar')
    test(ical)
