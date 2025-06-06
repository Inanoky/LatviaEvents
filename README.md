# Latvia Music Events Fetcher

This repository contains a simple Python script for retrieving upcoming music events in Latvia for the next weekend using the Ticketmaster Discovery API.

## Requirements
- Python 3.10+
- `requests` package
- A Ticketmaster API key

## Setup
1. Install dependencies:
   ```bash
   pip install requests
   ```
2. Export your Ticketmaster API key as an environment variable:
   ```bash
   export TICKETMASTER_API_KEY=YOUR_KEY_HERE
   ```

## Usage
Run the script:
```bash
python fetch_latvia_music_events.py
```
The script prints event names, start dates, and URLs for the upcoming weekend.
