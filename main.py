from wait import wait_no_assertion_failure, wait_until


def is_file_ready(filename):
    """Checks if a file exists and is readable."""
    import os
    return os.path.exists(filename) and os.access(filename, os.R_OK)


def download_file(url):
    """Simulates downloading a file (replace with your actual implementation)."""
    # Simulate download logic (not shown)
    pass


# Wait for a file to be downloaded and become readable
wait_until(lambda: is_file_ready("downloaded_file.txt"),
           "Downloaded file is not ready after retries.")

# Download a file and retry if there's an assertion error during download
wait_no_assertion_failure(lambda: download_file("https://example.com/file.zip"),
                          "File download failed after retries.")
