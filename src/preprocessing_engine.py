import os
import pandas as pd

from audit_logger import log_preprocessing


PREPROCESSED_FOLDER = "data/preprocessed"


def preprocess_data(valid_dataframes):
    """
    Preprocess validated dataframes
    """

    os.makedirs(PREPROCESSED_FOLDER, exist_ok=True)

    preprocessed_dataframes = {}

    for file_name, dataframe in valid_dataframes.items():

        try:

            print(f"Preprocessing started → {file_name}")

            # Remove duplicate rows
            dataframe = dataframe.drop_duplicates()

            # Standardize column names
            dataframe.columns = [
                column.strip().lower()
                for column in dataframe.columns
            ]

            # Remove spaces from string columns
            for column in dataframe.select_dtypes(include="object"):

                dataframe[column] = dataframe[column].str.strip()

            # Generate parquet file name
            parquet_file_name = file_name.replace(
                ".csv",
                ".parquet"
            )

            parquet_file_path = os.path.join(
                PREPROCESSED_FOLDER,
                parquet_file_name
            )

            # Save parquet
            dataframe.to_parquet(
                parquet_file_path,
                index=False
            )

            log_preprocessing(
                file_name=file_name,
                status="SUCCESS",
                row_count=len(dataframe),
                message="Preprocessing successful"
            )

            print(f"Preprocessing successful → {file_name}")

            preprocessed_dataframes[file_name] = dataframe

        except Exception as e:

            log_preprocessing(
                file_name=file_name,
                status="FAILED",
                row_count=0,
                message=str(e)
            )

            print(f"Error preprocessing {file_name}: {e}")

    return preprocessed_dataframes