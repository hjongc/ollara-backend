# 예를 들어, 특정한 포맷으로 날짜를 변환하는 유틸리티 함수
from datetime import datetime

def format_date(date: datetime) -> str:
    return date.strftime("%Y-%m-%d %H:%M:%S")
