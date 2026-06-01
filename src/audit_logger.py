import os
import pandas as pd
from datetime import datetime


LOG_FOLDER = "logs"


def current_time():
    """
    Returns current timestamp
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_log_file(log_file_path):
    """
    Creates log file if not exists
    """

    if not os.path.exists(log_file_path):

        columns = [
            "timestamp",
            "layer",
            "file_name",
            "status",
            "row_count",
            "message"
        ]

        empty_df = pd.DataFrame(columns=columns)

        empty_df.to_csv(log_file_path, index=False)


def write_log(layer,
              file_name,
              status,
              row_count,
              message,
              log_file_name):
    """
    Writes logs into CSV log file
    """

    try:

        os.makedirs(LOG_FOLDER, exist_ok=True)

        log_file_path = os.path.join(LOG_FOLDER, log_file_name)

        create_log_file(log_file_path)

        log_data = {
            "timestamp": current_time(),
            "layer": layer,
            "file_name": file_name,
            "status": status,
            "row_count": row_count,
            "message": message
        }

        log_df = pd.DataFrame([log_data])

        log_df.to_csv(
            log_file_path,
            mode="a",
            header=False,
            index=False
        )

        print(f"Log written successfully → {log_file_name}")

    except Exception as e:

        print(f"Error writing log: {e}")


def log_ingestion(file_name,
                  status,
                  row_count,
                  message):
    """
    Ingestion layer logging
    """

    write_log(
        layer="INGESTION",
        file_name=file_name,
        status=status,
        row_count=row_count,
        message=message,
        log_file_name="ingestion_log.csv"
    )


def log_preprocessing(file_name,
                      status,
                      row_count,
                      message):
    """
    Preprocessing layer logging
    """

    write_log(
        layer="PREPROCESSING",
        file_name=file_name,
        status=status,
        row_count=row_count,
        message=message,
        log_file_name="preprocessing_log.csv"
    )


def log_retention(file_name,
                  status,
                  row_count,
                  message):
    """
    Retention layer logging
    """

    write_log(
        layer="RETENTION",
        file_name=file_name,
        status=status,
        row_count=row_count,
        message=message,
        log_file_name="retention_log.csv"
    )