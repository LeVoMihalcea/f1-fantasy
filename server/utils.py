def convert_to_milliseconds(time):
    [seconds, milliseconds] = time.split(".")
    [minutes, seconds] = seconds.split(":")
    milliseconds = int(milliseconds)
    seconds = int(seconds)
    minutes = int(minutes)
    return (minutes * 60 + seconds) * 1000 + milliseconds

def convert_to_times(time_in_milliseconds):
    milliseconds = time_in_milliseconds % 1000
    time_in_milliseconds = time_in_milliseconds // 1000
    minutes = time_in_milliseconds // 60
    seconds = time_in_milliseconds % 60
    return f"{minutes}:{seconds}.{milliseconds}"
