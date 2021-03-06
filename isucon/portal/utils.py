import datetime

from django.conf import settings
from django.utils import timezone

jst = datetime.timezone(datetime.timedelta(hours=9))

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def get_jst_time(hour, minute, second):
    """指定時刻をJSTとして取得"""
    return datetime.time(hour=hour, minute=minute, second=second)

def get_jst_datetime(year, month, day, hour, minute, second):
    """指定日時をJSTとして取得"""
    return datetime.datetime(year, month, day, hour, minute, second).replace(tzinfo=jst)

def is_last_spurt(t, participate_at):
    t = t.astimezone(jst) # 必ずJSTで比較する
    lookahead = t + datetime.timedelta(hours=1)

    contest_end = datetime.datetime.combine(participate_at, settings.CONTEST_END_TIME).replace(tzinfo=jst)

    if lookahead >= contest_end:
        return True

    return False

def normalize_for_graph_label(t):
    return t.astimezone(jst).strftime(TIME_FORMAT)
