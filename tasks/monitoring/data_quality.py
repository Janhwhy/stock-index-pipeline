def validate_data(df):
    """
    Basic data quality checks
    """

    print("Validating data...")

    # Check if empty
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Check missing values
    missing = df.isnull().sum().sum()
    if missing > 0:
        print(f"Warning: {missing} missing values found")

    # Check duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Warning: {duplicates} duplicate rows found")

    print("Data validation complete")

    return True