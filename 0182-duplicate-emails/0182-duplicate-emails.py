import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    grp = person.groupby('email')
    data = grp.agg(Count = ('email', 'count'))
    data = data[data['Count']>1]
    data = data.reset_index()[['email']]
    data = data.rename(columns={'email':'Email'})

    return data