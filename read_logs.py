import os
import json
from azure.loganalytics import LogAnalyticsDataCollector
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Azure Log Analytics configuration
WORKSPACE_ID = 'your_workspace_id'
SHARED_KEY = 'your_shared_key'
LOG_TYPE = 'CustomLogType'  # Define your log type name

# Initialize the Azure Log Analytics client
log_analytics_client = LogAnalyticsDataCollector(WORKSPACE_ID, SHARED_KEY)


class LogFileHandler(FileSystemEventHandler):
    """
    Handles file modifications to process new log lines.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'r')
        self.file.seek(0, os.SEEK_END)  # Move to the end of the file

    def on_modified(self, event):
        if event.src_path == self.file_path:
            self.process_new_lines()

    def process_new_lines(self):
        for line in self.file:
            try:
                # Parse the JSON log line
                log_entry = json.loads(line.strip())

                # Transform the log entry
                transformed_entry = self.transform_log(log_entry)

                # Send to Azure Log Analytics
                self.send_to_azure(transformed_entry)
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON: {e}")

    @staticmethod
    def transform_log(log_entry):
        """
        Modify this method to transform log_entry as needed.
        """
        log_entry['processed_timestamp'] = 'now'  # Example transformation
        return log_entry

    @staticmethod
    def send_to_azure(log_entry):
        """
        Sends the log entry to Azure Log Analytics.
        """
        response = log_analytics_client.send(LOG_TYPE, [log_entry])
        if response.status_code == 200:
            print("Log sent successfully.")
        else:
            print(f"Failed to send log: {response.text}")


def main():
    log_file_path = '/path/to/your/log/file.log'  # Update with your log file path

    # Ensure the file exists
    if not os.path.exists(log_file_path):
        print(f"Log file not found: {log_file_path}")
        return

    # Set up the file observer
    event_handler = LogFileHandler(log_file_path)
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(
        log_file_path), recursive=False)
    observer.start()

    try:
        print("Monitoring log file for changes...")
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        print("Stopping log monitoring...")
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main()
