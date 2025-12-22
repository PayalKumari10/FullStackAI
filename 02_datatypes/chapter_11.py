import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Asia/Kolkata")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["tea_type", "milk_type", "sweetener", "spices"])