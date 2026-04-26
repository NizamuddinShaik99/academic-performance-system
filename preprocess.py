def transform_input(data):
    subjects = data.get("subjects", [])

    percentages = []

    for sub in subjects:
        obtained = sub.get("obtained", 0)
        total = sub.get("total", 100)

        if total > 0:
            percent = (obtained / total) * 100
        else:
            percent = 0

        percentages.append(percent)

    if len(percentages) == 0:
        avg_percentage = 0
        min_percentage = 0
        max_percentage = 0
    else:
        avg_percentage = sum(percentages) / len(percentages)
        min_percentage = min(percentages)
        max_percentage = max(percentages)

    features = {
        "study_hours": data.get("study_hours", 0),
        "attendance": data.get("attendance", 0),
        "screen_time": data.get("screen_time", 0),
        "sleep_hours": data.get("sleep_hours", 0),
        "avg_percentage": avg_percentage,
        "min_percentage": min_percentage,
        "max_percentage": max_percentage
    }

    return features