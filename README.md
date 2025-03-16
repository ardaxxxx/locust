# Locust Performance Testing

## Prerequisites
Ensure you have **Python 3.7+** installed.

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```
2. Install dependencies:
   ```bash
   pip install locust
   ```

## Running Locust
### Web Interface Mode
Run Locust using:
```bash
locust
```
Then, open `http://localhost:8089` in your browser.

### Command-Line (Headless) Mode
```bash
locust -f locustfile.py --headless -u 10 -r 2 --host=http://example.com
```
- `-f locustfile.py`: Locust script
- `--headless`: Run without UI
- `-u 10`: Number of users
- `-r 2`: Spawn rate
- `--host=http://example.com`: Target system

## Test Results
To save results:
```bash
locust -f locustfile.py --headless -u 10 -r 2 --host=http://example.com --csv=results
```

