import os
import shutil
from datetime import datetime
from zipfile import ZipFile


INGESTION_FOLDER = "data/ingestion"
RETENTION_FOLDER = "data/retention/archive"


def archive_files():

    print("Retention layer started")

    os.makedirs(RETENTION_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    zip_file_path = os.path.join(
        RETENTION_FOLDER,
        f"archive_{timestamp}.zip"
    )

    csv_files = [
        file_name
        for file_name in os.listdir(INGESTION_FOLDER)
        if file_name.endswith(".csv")
    ]

    with ZipFile(zip_file_path, "w") as zip_file:

        for file_name in csv_files:

            source_path = os.path.join(
                INGESTION_FOLDER,
                file_name
            )

            zip_file.write(
                source_path,
                arcname=file_name
            )

            os.remove(source_path)

            print(f"Archived → {file_name}")

    print(f"Retention completed → {zip_file_path}")