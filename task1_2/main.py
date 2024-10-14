import csv
from pathlib import Path
from typing import Optional


def read_csv(path: str, columns: list[str]) -> list[dict[str, str]]:
    """Reads a CSV file and returns a list of dictionaries.

    param: path: str: path to the CSV file.
    param: columns: list[str]: list of column names.
    """
    file_path = Path(__file__).parent / Path(path)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = csv.DictReader(file, fieldnames=columns)
            return list(data)
    except FileNotFoundError:
        print(f"File by provided path: {file_path} not found.")
        return []
    except csv.Error:
        print(f"Error reading the CSV file: {file_path}")
        return []


def total_salary(path: str) -> Optional[tuple[float, float]]:
    """Calculates the total and average salary of all employees and return them.

    param: path: path to the CSV file.
    """
    data = read_csv(path, ["name", "salary"])
    if not data:
        print(f"Failed to process given file: {path}")
        return None
    total = sum(float(row["salary"]) for row in data)
    average = total / len(data)
    return total, average


def get_cats_info(path: str) -> list[dict[str, str]]:
    """Reads a CSV file id, name, age and returns a list of dictionaries.

    param: path: str: path to the CSV file.
    """
    return read_csv(path, ["id", "name", "age"])


if __name__ == "__main__":
    print(total_salary("data/salaries.csv"))
    print(get_cats_info("data/cats.csv"))
