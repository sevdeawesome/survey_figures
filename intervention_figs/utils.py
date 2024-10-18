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


'''
We should develop more powerful and more general systems as fast as possible    18.867925
We should never build AGI                                                        5.660377


'''

timelines_positions = {
    "Eventually, but not soon.": "Eventually",
    "Soon, but not as fast as possible": "Soon",
    "We should develop more powerful and more general systems as fast as possible": "ASAP",
    "We should never build AGI": "Never"
}



def fix_data(df, drop_zeros=True):
    if drop_zeros:
        df = df[df["number"] != 0]
    df["Q1"] = df["Q1"].replace(groups)
    
    return df