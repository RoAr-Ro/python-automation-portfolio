# Automated Email Report Bot

## Description
Script that fetches user data from a REST API, generates a formatted
Excel report and sends it automatically via email with the file attached.

## Technologies
- Python 3
- requests
- openpyxl (with styled headers)
- smtplib

## Setup
Set these environment variables before running:
- `EMAIL` → your Gmail address
- `PASSWORD` → your Gmail app password
- `RECIPIENT` → recipient email address

## How to run
1. Install dependencies: `pip install requests openpyxl`
2. Set environment variables
3. Run: `python email_bot.py`

## Output
- `users_report.xlsx` generated and sent via email automatically