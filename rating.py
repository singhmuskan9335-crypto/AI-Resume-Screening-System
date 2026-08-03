def get_resume_rating(score):

    if score >= 90:
        return "⭐⭐⭐⭐⭐ Excellent Candidate"

    elif score >= 75:
        return "⭐⭐⭐⭐ Very Good Candidate"

    elif score >= 60:
        return "⭐⭐⭐ Good Candidate"

    elif score >= 40:
        return "⭐⭐ Average Candidate"

    else:
        return "⭐ Poor Candidate"