Log Analysis and Monitoring Script

This script provides an automated solution for monitoring and analyzing log files, enabling real-time tracking of log entries and basic analysis functionalities.

Prerequisites:

- Python 3.x installed on your system.

Usage:

1. Download the Script

   - Save the provided Python script as 'log_monitor.py' in your desired directory.

2. Create a Log File:

   - Create a text file named 'example.log' in the same directory where you saved `log_monitor.py`. This file will serve as the log file to be monitored.

3. Populate the Log File:

   - Open 'example.log' with a text editor and add sample log entries. Include lines with keywords like "error", "warning", or "exception" to test the log analysis functionality.

4. Run the Script:

   - Open a terminal or command prompt.
   - Navigate to the directory where you saved 'log_monitor.py'.
   - Run the script by typing 'python log_monitor.py' and pressing Enter.

5. Stop Monitoring:

   - While the script is running, press Ctrl+C in the terminal to stop the monitoring process. This will gracefully terminate the script.

Testing:

- Once the script is running, it will continuously monitor the `example.log` file for new entries.
- It will display new log entries in real-time and perform basic analysis, counting occurrences of keywords like "error", "warning", and "exception".
- Verify the functionality by observing the output in the terminal and checking if the script correctly identifies and counts the specified keywords in the log entries.

Dependencies:

- The script has no external dependencies other than Python's built-in libraries.

Author:

- C R Thoran Kumar.

Repository:

- https://github.com/thoran123/marketfeed-



