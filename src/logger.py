import logging
import os
from datetime import datetime

# Generate log file name with timestamp
LOG_dir = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Define the directory where logs will be stored
logs_dir = os.path.join(os.getcwd(), f"logs/{LOG_dir}")
os.makedirs(logs_dir, exist_ok=True)  # Create the 'logs' directory if it doesn't exist

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Ensure the script is being run directly
if __name__ == "__main__":
    logging.info("Logging has started")