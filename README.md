# git-repo
Write a custom script that reads the Nginx logs from the Docker container and sends them to Azure Log Analytics using the HTTP Data Collector API.
Steps:
1. Create a Script: Write a script (e.g., in Python or Bash) that:
- Reads the Nginx logs from the Docker container.
- Formats the logs as required by Azure Log Analytics.
- Sends the logs to Azure Log Analytics using the HTTP Data Collector API.

2. Schedule the Script: Use a cron job or a similar scheduling tool to run the script at regular intervals.