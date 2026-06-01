import os
import pandas as pd

from utils import (
    get_csv_files,
    get_json_files,
    read_json_file
)

from audit_logger import log_ingestion


INGESTION_FOLDER = "data/ingestion"
CONTROL_FOLDER = "config/control_files"


def get_control_file_name(csv_file_name):
    """
    Generate matching control file name

    Example:
    claims_20251017.csv → claims_yyyymmdd.json
    """

    table_name = csv_file_name.split("_")[0]

    return f"{table_name}_yyyymmdd.json"


def validate_columns(dataframe, expected_columns):
    """
    Validate schema columns
    """

    actual_columns = list(dataframe.columns)

    missing_columns = []

    for column in expected_columns:

        if column not in actual_columns:

            missing_columns.append(column)

    return missing_columns


def process_ingestion():
    """
    Main ingestion process
    """

    valid_dataframes = {}

    csv_files = get_csv_files(INGESTION_FOLDER)

    json_files = get_json_files(CONTROL_FOLDER)

    print(f"CSV Files Found: {csv_files}")

    print(f"JSON Files Found: {json_files}")

    for csv_file in csv_files:

        try:

            csv_file_path = os.path.join(
                INGESTION_FOLDER,
                csv_file
            )

            control_file_name = get_control_file_name(csv_file)

            control_file_path = os.path.join(
                CONTROL_FOLDER,
                control_file_name
            )

            # Check control file existence
            if not os.path.exists(control_file_path):

                log_ingestion(
                    file_name=csv_file,
                    status="FAILED",
                    row_count=0,
                    message="Control file missing"
                )

                print(f"Control file missing → {control_file_name}")

                continue

            # Read control JSON
            control_data = read_json_file(control_file_path)

            expected_columns = control_data["expected_columns"]

            mandatory_columns = control_data["expected_columns"]

            # Read CSV file
            dataframe = pd.read_csv(csv_file_path)

            # Empty file validation
            if dataframe.empty:

                log_ingestion(
                    file_name=csv_file,
                    status="FAILED",
                    row_count=0,
                    message="Empty file"
                )

                print(f"Empty file → {csv_file}")

                continue

            # Schema validation
            missing_columns = validate_columns(
                dataframe,
                expected_columns
            )

            if len(missing_columns) > 0:

                log_ingestion(
                    file_name=csv_file,
                    status="FAILED",
                    row_count=0,
                    message=f"Missing columns: {missing_columns}"
                )

                print(f"Schema validation failed → {csv_file}")

                continue

            # Mandatory column null validation
            null_validation_failed = False

            for column in mandatory_columns:

                if dataframe[column].isnull().sum() > 0:

                    null_validation_failed = True

                    log_ingestion(
                        file_name=csv_file,
                        status="FAILED",
                        row_count=len(dataframe),
                        message=f"Mandatory column contains NULLs → {column}"
                    )

                    print(f"NULL validation failed → {csv_file}")

                    break

            if null_validation_failed:

                continue

            # Success
            log_ingestion(
                file_name=csv_file,
                status="SUCCESS",
                row_count=len(dataframe),
                message="Validation successful"
            )

            valid_dataframes[csv_file] = dataframe

            print(f"Validation successful → {csv_file}")

        except Exception as e:

            log_ingestion(
                file_name=csv_file,
                status="FAILED",
                row_count=0,
                message=str(e)
            )

            print(f"Error processing {csv_file}: {e}")

    return valid_dataframes