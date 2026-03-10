import re
import datetime

def extract_time(task):

    match = re.search(r"\b\d{1,2}(:\d{2})?\s?(am|pm)?\b", task.lower())

    if match:
        return match.group()

    return None


def current_time_block():

    hour = datetime.datetime.now().hour

    if hour < 12:
        return "morning"

    if hour < 17:
        return "afternoon"

    return "evening"
