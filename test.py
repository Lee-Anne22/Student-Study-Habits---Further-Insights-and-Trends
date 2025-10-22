# %%
#Importing all necessary programs
def import_study_libs():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import sklearn as sk
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import StratifiedKFold
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.tree import plot_tree
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import classification_report
    from sklearn.metrics import make_scorer
    import lime as lime
    import shap as shap
    return {"np": np, "pd": pd, "plt": plt, "train_test_split": train_test_split, "GridSearchCV": GridSearchCV, "StratifiedKFold": StratifiedKFold,
            "DecisionTreeClassifier": DecisionTreeClassifier, "accuracy_score": accuracy_score, "confusion_matrix": confusion_matrix,
            "classification_report":classification_report, "make_scorer": make_scorer}

# Loading the data set
file= "student_habits_performance.csv"
def load_study_data():
    try:
        libs= import_study_libs()
        pd= libs["pd"]
        df= pd.read_csv(file, sep=';')
        dfc=df.columns.str.strip() #To clean up data
        print ("Data Loaded Succesfully!")
    except FileNotFoundError:
        print (f"File not found!: {file}")

# %%
# Handle missing Values and duplicates:
def study_clean():
    data= load_study_data()
    df= data["dfc"]
    libs= import_study_libs()
    pd= libs["pd"]
    np= libs["np"]
    size=df.head()
    shape=df.shape()
    stats=df.describe()
    print (f"Data size: {size}\n Data shape: {shape}\n Data Statistics: {stats}")
    df_missing= df.fillna(df.mean (numeric_only= True))
    df_duplicates= df_missing.drop_duplicates()
    df_clean = df_duplicates[
            (df_duplicates["sleep_hours"] + df_duplicates["social_media_hours"] + df_duplicates["netflix_hours"] + df_duplicates["study_hours_per_day"] <= 24) &
            (df_duplicates["sleep_hours"] >= 0) & 
            (df_duplicates["age"].between(16, 24))]
    print ("Data preprocessed and cleaned!")
    return df_clean