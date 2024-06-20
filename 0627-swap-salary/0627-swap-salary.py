import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    d=[]
    for i in salary["sex"]:
        if(i=="f"):
            d.append("m")
        elif(i=="m"):
            d.append("f")
    salary["sex"]=(d)
    return salary
