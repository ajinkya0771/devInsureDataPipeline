import os
import json
from datetime import datetime


def current_timestamp():
    """
    Returns current timestamp
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def extract_file_date(file_name):
    """
    Extract date from file name

    Example:
    claims_20251017.csv → 20251017
    """
    try:
        date_part = file_name.split("_")[-1].split(".")[0]
        return date_part
    except Exception as e:
        print(f"Error extracting file date: {e}")
        return None


def read_json_file(json_path):
    """
    Read JSON control file
    """
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
        return data

    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None


def file_exists(file_path):
    """
    Check whether file exists
    """
    return os.path.exists(file_path)


def create_folder(folder_path):
    """
    Create folder if not exists
    """
    os.makedirs(folder_path, exist_ok=True)


def get_csv_files(folder_path):
    """
    Get all CSV files from folder
    """
    csv_files = []

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            csv_files.append(file)

    return csv_files


def get_json_files(folder_path):
    """
    Get all JSON files from folder
    """
    json_files = []

    for file in os.listdir(folder_path):
        if file.endswith(".json"):
            json_files.append(file)

    return json_files