from ingestion_manager import process_ingestion
from preprocessing_engine import preprocess_data
from transformation_engine import build_curated_and_semantic
from retention_manager import archive_files


def run_pipeline():

    print("Pipeline execution started")

    # Ingestion layer
    valid_dataframes = process_ingestion()

    # Stop pipeline if no valid files
    if len(valid_dataframes) == 0:

        print("No valid files found")

        return

    # Preprocessing layer
    preprocessed_data = preprocess_data(
        valid_dataframes
    )

    # Transformation layer
    build_curated_and_semantic(
        preprocessed_data
    )

    # Retention layer
    archive_files()

    print("Pipeline execution completed")


if __name__ == "__main__":

    run_pipeline()