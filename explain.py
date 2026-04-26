def generate_explanation(features):

    reasons = []

    if features["attendance"] < 75:
        reasons.append("Low attendance is affecting performance")

    if features["study_hours"] < 2:
        reasons.append("Study hours are too low")

    if features["screen_time"] > 5:
        reasons.append("High screen time reduces focus")

    if features["min_percentage"] < 40:
        reasons.append("Some subjects have very low marks")

    if features["sleep_hours"] < 6:
        reasons.append("Lack of sleep affects learning")

    if not reasons:
        reasons.append("Overall performance is stable")

    return reasons


def generate_recommendations(features):

    tips = []

    if features["study_hours"] < 3:
        tips.append("Increase study time to 3–4 hours daily")

    if features["attendance"] < 80:
        tips.append("Maintain attendance above 80%")

    if features["screen_time"] > 4:
        tips.append("Reduce screen time")

    if features["min_percentage"] < 50:
        tips.append("Focus on weak subjects")

    if features["sleep_hours"] < 7:
        tips.append("Maintain proper sleep schedule")

    if not tips:
        tips.append("Keep maintaining your performance")

    return tips