from datetime import datetime, timedelta

events = [
    {"event_id": "trip_001", "event_time": "10:00:12"},
    {"event_id": "trip_002", "event_time": "10:01:04"},
    {"event_id": "trip_003", "event_time": "10:02:10"},
    {"event_id": "trip_004", "event_time": "10:03:25"},
    {"event_id": "trip_005", "event_time": "10:04:40"},
    {"event_id": "trip_006", "event_time": "10:05:15"},
    {"event_id": "trip_007", "event_time": "10:06:30"},
]

for event in events:
    event["event_time"] = datetime.strptime(
        event["event_time"],
        "%H:%M:%S"
    )

WINDOW_SIZE = timedelta(minutes=5)

for current_event in events:

    current_time = current_event["event_time"]

    window_start = current_time - WINDOW_SIZE

    count = 0

    for event in events:
        if window_start <= event["event_time"] <= current_time:
            count += 1

    print(
        current_time.strftime("%H:%M:%S"),
        "→ last 5 minutes:",
        count,
        "trips"
    )