from typing import Dict
import pandas as pd


def partition_by_day(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Reads the pandas dataframe and returns a dictionary that has the day_of_month
    and corresponding dataframe as the key value pairs.
    """

    parts = {}

    for day_of_month in df["DAY_OF_MONTH"].unique():
        # Adding zero padding to the day of month for easy sorting of day
        parts[f"DAY_OF_MONTH == {day_of_month:02}"] = df[df["DAY_OF_MONTH"]
                                                         == day_of_month]

    return parts


def partition_calc(partitions: Dict[str, pd.DataFrame]) -> Dict[str, str]:
    """
    Calculates the length of dataframe for each partition, i.e, the number of
    rows available in dataset for each day.
    """

    parts = {}

    for part_key, df in partitions.items():
        print(f"Calc: {part_key}")
        parts[part_key] = str(len(df))

    return parts
