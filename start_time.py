from datetime import datetime, timedelta
def gen_slot(interval_minutes=15):
    now = datetime.now()

    minutes = (now.minute // interval_minutes + 1) * interval_minutes
    start = now.replace(minute=0, second=0, microsecond=0) + timedelta(minutes=minutes)

    end = now.replace(hour=15, minute=0, second=0, microsecond=0)    
    slots = []
    if start > end:
        # If after 17:00, generate for next day from 9:00 to 17:00
        tomorrow = now + timedelta(days=1)
        start = tomorrow.replace(hour=9, minute=0, second=0, microsecond=0)
        end = tomorrow.replace(hour=15, minute=0, second=0, microsecond=0)
    while start <= end:
        slots.append(start.strftime("%H:%M"))
        start += timedelta(minutes=interval_minutes)
    return slots
