import re

def extract_sentences(text):

    sentences = re.split(r"[.\n]", text)

    return [s.strip() for s in sentences if s.strip()]


def organize_text(text):

    goals=[]
    tasks=[]
    habits=[]

    lines = extract_sentences(text)

    for line in lines:

        l=line.lower()

        if "learn" in l or "build" in l:
            goals.append(line)

        elif "daily" in l or "gym" in l:
            habits.append(line)

        else:
            tasks.append(line)

    return goals,tasks,habits
