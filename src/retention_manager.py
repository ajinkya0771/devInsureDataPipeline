import os
import shutil
from datetime import datetime


INGESTION_FOLDER = "data/ingestion"
RETENTION_FOLDER = "data/retention"


def archive_files():
    """
    Archive processed ingestion files
    """

    print("Retention layer started")

    # Create retention folder if not exists
    os.makedirs(
        RETENTION_FOLDER,
        exist_ok=True
    )

    # Timestamp for archive folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    archive_folder = os.path.join(
        RETENTION_FOLDER,
        f"archive_{timestamp}"
    )

    os.makedirs(
        archive_folder,
        exist_ok=True
    )

    # Move all CSV files
    for file_name in os.listdir(INGESTION_FOLDER):

        if file_name.endswith(".csv"):

            source_path = os.path.join(
                INGESTION_FOLDER,
                file_name
            )

            destination_path = os.path.join(
                archive_folder,
                file_name
            )

            shutil.move(
                source_path,
                destination_path
            )

            print(f"Archived → {file_name}")

    print(f"Retention completed → {archive_folder}")