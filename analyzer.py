def analyze_feedback(text):
    text = str(text).lower()

    # -------------------------
    # CATEGORY RULES
    # -------------------------
    if any(word in text for word in ["schedule", "appointment", "booking", "book"]):
        category = "scheduling"

    elif any(word in text for word in ["wait", "delay", "long time", "waiting"]):
        category = "wait_times"

    elif any(word in text for word in ["staff", "doctor", "nurse", "technician", "rude"]):
        category = "staff"

    elif any(word in text for word in ["billing", "charge", "payment", "insurance", "cost"]):
        category = "billing"

    elif any(word in text for word in ["result", "report", "delay results"]):
        category = "results_delay"

    elif any(word in text for word in ["facility", "clean", "dirty", "room", "equipment"]):
        category = "facility"

    elif any(word in text for word in ["communication", "call", "email", "response"]):
        category = "communication"

    elif any(word in text for word in ["technical", "error", "system", "app", "bug"]):
        category = "technical_issue"

    elif any(word in text for word in ["great", "excellent", "good", "amazing", "smooth", "easy"]):
        category = "positive_experience"

    else:
        category = "other"

    # -------------------------
    # SENTIMENT RULES
    # -------------------------
    positive_words = ["good", "great", "excellent", "amazing", "smooth", "easy", "fast", "comfortable"]
    negative_words = ["bad", "terrible", "awful", "slow", "rude", "pain", "delay", "wait", "confusing"]

    if any(word in text for word in positive_words):
        sentiment = "positive"
    elif any(word in text for word in negative_words):
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "category": category,
        "sentiment": sentiment
    }