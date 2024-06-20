import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    grouped = courses.groupby(["class"]).student.count().reset_index()
    return grouped.loc[grouped["student"] >= 5, ["class"]]
