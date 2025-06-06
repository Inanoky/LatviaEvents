import os
import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

API_KEY = os.getenv('TICKETMASTER_API_KEY')
if not API_KEY:
    raise SystemExit("Please set the TICKETMASTER_API_KEY environment variable")

def upcoming_weekend_range(tz=ZoneInfo('Europe/Riga')):
    today = datetime.now(tz).date()
    days_until_friday = (4 - today.weekday()) % 7
    friday = datetime.combine(today + timedelta(days=days_until_friday), datetime.min.time(), tz)
    sunday = friday + timedelta(days=2, hours=23, minutes=59, seconds=59)
    return friday.astimezone(ZoneInfo('UTC')), sunday.astimezone(ZoneInfo('UTC'))

def fetch_events():
    start, end = upcoming_weekend_range()
    url = 'https://app.ticketmaster.com/discovery/v2/events.json'
    params = {
        'apikey': API_KEY,
        'countryCode': 'LV',
        'classificationName': 'music',
        'startDateTime': start.isoformat().replace('+00:00', 'Z'),
        'endDateTime': end.isoformat().replace('+00:00', 'Z'),
        'size': 20
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    events = data.get('_embedded', {}).get('events', [])
    for e in events:
        name = e.get('name')
        date = e.get('dates', {}).get('start', {}).get('dateTime')
        link = e.get('url')
        print(f"{name} | {date} | {link}")

if __name__ == '__main__':
    fetch_events()
