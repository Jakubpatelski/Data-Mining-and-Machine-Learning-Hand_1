"""Shared survey loading for the weather and motivation notebooks."""

from pathlib import Path

import pandas as pd
import yaml


def load_student_data():
    """Read the four survey files and return one table without passwords."""
    # Find the shared dataset folder one level above this Python file.
    dataset = Path(__file__).resolve().parent.parent / "dataset"

    df_2023 = pd.read_csv(dataset / "Dataminers 2023.tsv", sep="\t")
    # Keep timestamps as text; each notebook extracts the dates it needs.
    df_2024 = pd.read_json(dataset / "Dataminers 2024.json", convert_dates=False)
    df_2025 = pd.read_xml(dataset / "Dataminers_2025.xml", parser="etree")
    with open(dataset / "Dataminers 2026.yaml", encoding="utf-8") as file:
        df_2026 = pd.DataFrame(yaml.safe_load(file))

    clean_tables = []
    for source, table in zip(
        [2023, 2024, 2025, 2026], [df_2023, df_2024, df_2025, df_2026]
    ):
        # Remove passwords and give the remaining columns consistent names.
        cleaned = table.drop(
            columns=["Enter Your Password", "Enter_Your_Password"], errors="ignore"
        ).copy()
        cleaned.columns = [
            "timestamp", "shoe_size", "programme", "height",
            "course_reason", "seattle_letters",
        ]
        # The source identifies the timestamp format, not necessarily its year.
        cleaned["source_file"] = source
        clean_tables.append(cleaned)

    return pd.concat(clean_tables, ignore_index=True)

