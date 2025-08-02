def change_hrs(timestr, change):
    hours, minutes = timestr.split(":")
    hours = int(hours)
    minutes = int(minutes)
    new_hours = (hours + change) % 24
    return f"{new_hours}:{minutes:02d}"
print(change_hrs("9:04", 5));
