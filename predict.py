def predict_performance(features):

    score = (
        features["avg_percentage"] * 0.5 +
        features["study_hours"] * 5 +
        features["attendance"] * 0.2 -
        features["screen_time"] * 2 +
        features["sleep_hours"] * 1
    )

    score = max(0, min(100, score))

    if score < 40:
        risk = "High Risk"
    elif score < 70:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return score, risk