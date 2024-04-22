import os
import re
import signal
import sys
import time

# Function to handle Ctrl+C signal
def signal_handler(signal, frame):
    print("\nMonitoring stopped.")
    sys.exit(0)

# Function to monitor log file
def monitor_log(log_file):
    try:
        with open(log_file, "r") as file:
            file.seek(0, 2)  # Move cursor to end of file
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.1)  # Sleep briefly if no new lines
                    continue
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
        sys.exit(1)

# Function to perform log analysis
def analyze_log(log_file):
    keyword_counts = {}
    try:
        for line in monitor_log(log_file):
            # Perform basic analysis
            keywords = re.findall(r'error|warning|exception', line, re.IGNORECASE)
            for keyword in keywords:
                keyword_counts[keyword] = keyword_counts.get(keyword, 0) + 1
            
            # Print the log entry
            print(line)
            
            # Generate summary report
            print("\nSummary Report:")
            for keyword, count in keyword_counts.items():
                print(f"{keyword.capitalize()}: {count}")
            print("-" * 20)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    
    # Specify log file path
    log_file = "example.log"
    
    # Start log analysis
    analyze_log(log_file)
