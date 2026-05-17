#  PreventativeScan Feedback Tool

A lightweight analytics tool that transforms unstructured patient feedback into structured operational insights for PreventativeScan’s MRI screening service.

Built to help teams identify experience issues, monitor sentiment trends, and detect operational risks during rapid scaling.

---

##  Overview

This tool analyzes member feedback from PreventativeScan’s MRI screening service to surface key drivers of patient experience, including operational friction points, sentiment shifts, and high-severity cases.

It enables faster, data-driven decision-making for Member Experience and Operations teams.

---

##  Features

- Automatic categorization of feedback (e.g., scheduling, staff, billing, wait times)
- Sentiment analysis (positive / neutral / negative)
- Severity scoring based on NPS
- Issue frequency breakdown
- Location-based segmentation of feedback
- Alerts for spikes in negative or high-severity responses

---

##  How It Works

A lightweight rule-based classification engine processes feedback text and converts it into structured operational signals.

Designed for:
- Speed
- Reliability
- Interpretability
- No external API dependency

---

##  How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/preventativescan-feedback-tool.git
cd preventativescan-feedback-tool
