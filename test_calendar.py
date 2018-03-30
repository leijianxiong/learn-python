#!/usr/bin/env python3

import calendar

#cal = calendar.TextCalendar(calendar.SUNDAY)
# format_month = cal.formatmonth(2018, 3)
# print(format_month)

# cal.prmonth(2018, 3)
#cal.pryear(2018)

# cal = calendar.HTMLCalendar(calendar.SUNDAY)
# format_match = cal.formatmonth(2018, 3)
# print(format_match)

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2018, 3)
