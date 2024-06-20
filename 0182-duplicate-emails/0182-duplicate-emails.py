import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person[person.duplicated(subset=['email'])][['email']]
    return df.drop_duplicates()
