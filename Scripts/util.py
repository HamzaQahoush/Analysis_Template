import re
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def clean_analysis_sheet(sheet):
    """
    Cleans and standardizes the column names in an analysis sheet DataFrame.

    Parameters:
        sheet (pd.DataFrame): The analysis sheet DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned analysis sheet DataFrame.

    """
    str_cols = sheet.select_dtypes(include=['object']).columns
    sheet.columns = sheet.columns.str.strip()
    for col in str_cols:
        sheet[col] = sheet[col].str.strip()
    sheet.columns = sheet.columns.str.replace(' ', '_').str.replace('/', '_').str.replace('-', "_")
    analysis_sheet_filtered = sheet.drop(columns=['Data_collection_level', 'Relevance', 'Constraints_Checks'])
    return analysis_sheet_filtered


def replace_slash(column_name):
    """
        Replaces forward slash ('/') characters with a period ('.') in a given string.

        Parameters:
            column_name (str): The string to be modified.

        Returns:
            str: The modified string with forward slashes replaced by periods.
        """
    return column_name.replace('/', '.')
