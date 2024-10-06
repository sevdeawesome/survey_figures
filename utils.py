import pandas as pd

groups = {
    '4': 'Other',
    'AI safety researcher or professional': 'AI Safety Researcher',
    'Academic researcher in AI/ML/related field (e.g. PhD student, postdoc, professor)': 'Academic',
    'Industry engineer or researcher in AI/ML/related field': 'Industry',
    'Computer science professional or student not focused on ML/AI (e.g. Software Engineer, CS student)': "Other"
}





#result['Q1'] = result['Q1'].replace(groups)
statements = {
    "1": "AGI is too far away to be worth worrying about",
    "2": "Some AI’s (now or in the future) may be moral patients, with their own welfare that we should care about",
    "3": "Existing ML paradigms can produce AGI",
    "4": "Future AI’s will be tools without their own goals or drives",
    "5": "Catastrophic risks from advanced AI are generally overstated",
    "6": "We can always just turn off our AI’s if they behave badly",
    "7": "Self-preservation and control drives will spontaneously emerge in sufficiently advanced ai's",
    "8": "Safety work often slows important progress and wastes time",
    "9": "technical AI researchers should be concerned about catastrophic risks"
}



def fix_data(df):
    df_interventions = pd.read_csv("interventions.csv")
    df_interventions = df_interventions[::-1]
    df["number"] = df_interventions["number"]
    df = df[df["number"] != 0]
    df["Q1"] = df["Q1"].replace(groups)
    return df