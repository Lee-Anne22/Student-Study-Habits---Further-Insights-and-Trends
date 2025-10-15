
#Importing all necessary programs
def import_study_libs():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import sklearn as sk
    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import StratifiedKFold
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import classification_report
    from sklearn.metrics import make_scorer
   # import lime as lime
    #import shap as shap
    return {"np":np, "pd":pd, "plt":plt, "GridSearchCV":GridSearchCV, "StratifiedKFold":StratifiedKFold,
            "RandomForestClassifier":RandomForestClassifier, "accuracy_score": accuracy_score, "confusion_matrix": confusion_matrix,
            "classification_report":classification_report, "make_scorer": make_scorer}

# Loading the data set
file= "student_habits_performance.csv"

def load_study_data(file="student_habits_performance.csv", **kwargs):
    try:
        libs= import_study_libs()
        pd=libs["pd"]
        df= pd.read_csv(file, sep=';', **kwargs)
        dfc=df.columns.str.strip() #To clean up data
        print ("Data Loaded Succesfully!")
        return dfc
    except FileNotFoundError:
        print (f"File not found!: {file_path}")
        return None

def study_clean(dfc):
    df= load_study_data()
    dfc= df["dfc"]
    libs= import_study_libs()
    pd=libs["pd"]
    df_missing= dfc.fillna(df.mean(numeric_only= True))
    df_duplicates= df_missing.drop_duplicates()
    df_clean= df_duplicates.head()

    print ("Data preprocessed and cleaned!")
    return df_clean
    
if __name__ == "__main__":
    libs = import_study_libs()
    df = load_study_data()
    if df is not None:
        df_clean = study_clean(df)
        print(df_clean)