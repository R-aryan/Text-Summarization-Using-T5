import datetime
from enum import Enum

from pytz import timezone


class TimeReferenceType(Enum):
    PAST = -1
    FUTURE = 1


class Datetime:

    @staticmethod
    def now() -> datetime:
        return Datetime.utc_now()

    @staticmethod
    def utc_now() -> datetime:
        return datetime.datetime.utcnow()

    @staticmethod
    def hk_now():
        return datetime.datetime.now(timezone('Asia/Hong_Kong'))

    @staticmethod
    def total_seconds_now():
        epoch = Datetime.now() - datetime.datetime.utcfromtimestamp(0)
        return epoch.total_seconds()

    @staticmethod
    def date_today() -> datetime:
        return datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def time_from(base_time: datetime, delta: int, reference: TimeReferenceType = TimeReferenceType.FUTURE.value):
        return base_time + reference * datetime.timedelta(delta)

    @staticmethod
    def str_to_datetime(ttl_time) -> datetime.datetime:
        return datetime.datetime.strptime(str(ttl_time).replace(" ", 'T'), "%Y-%m-%dT%H:%M:%S.%f")

    @staticmethod
    def str_to_ftx_time(time_string):
        return datetime.datetime.strptime(''.join(time_string.rsplit(':', 1)), '%Y-%m-%dT%H:%M:%S.%f%z')
