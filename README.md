

# Project Background

Student exam scores are not only determined by sheer willpower or effort
alone! Exam scores can be effected by various daily habits, including
sleep, diet, social media usage,etc. Why would this be important to
consider from a business perspective? Well, in today’s economy, the
education sector has grown substantially over the past five years alone
due to the pandemic. Online education tools and accessibility has made
the market very lucrative and by determining which habits affect exam
scores more, niche markets for entrepreneurs could be in grasp.
Therefore, the effect of student habits on exam scores was the main
focus of this project.

# Project Summary

The project focused on determining the main daily habits which exerted
the most effect on exam scores of students between 16-24 years of age.
The project utilized data obtained from Kaggle and using machine
learning models were able to determine which daily habits had the
biggest effect on exam scores. The machine learning models utilised in
this project include a Linear Regression model and a Decision Tree.

# Project Process

The project started with data cleaning and preparation for the machine
learning models utilised in this project.

#### <u>Data Loading</u>

The data provided was downloaded as student_habits_performance.csv from
Kaggle and load using pandas. After loading of the csv file, the
necessary libraries were imported and placed in a import_study_libs
class. These libraries can be found in the requirements.txt file for
replication of the project.

#### <u>Preparation</u>

The data was first prepared by cleaning which consisted of filling
missing values with averages and removing any spacing between words.
After cleaning, encoding of categorical variables ( ‘part-time job’,
‘diet quality’, ‘internet quality’, and ‘extracurricular activity’)
using the Sci-kit Learn ‘StandardScaler’ was implemented. These new
encoded categories were added to a copy of the csv and saved as
‘student_habits_encoded’.csv which was used for the exploratory data
analysis and training the machine models.

### Data Exploration and Model Building

#### <u>Data Exploration</u>

Data exploration began with statistical analysis consisting of mmmm,
mmm, mmm. After statistical analysis, data exploration began by plotting
the following plots:

- Scatter plot
  - The correlation between exam score and internet quality, sleep hours
    and exercise frequency
- Stacked bar plot
  - The relationship between internet quality and exam scores by gender,
    further explored using a 3D surface plot.
- Violin plot
  - Mental Health rating per age group: 16-18 years, 19-20 years, 21-22
    years and 23-24 years.
- Heatmap
  - To gain multivariate insights between categories
- Radar plot
  - The average amount of time spent on different habits:

    - Amount of study hours - study hours

    - Amount of time spent on social media - social media hours

    - Amount of time spent on Netflix - netflix hours

    - Amount of time spent on sleep - sleep hours

#### <u>Model Building</u>

Two machine learning models- Linear Regression and a Decision Tree- were
built and trained using Sci-Kit learn for this project. The linear
regression model were used to predict the exam scores of students when
considering the following factors:

- Study hours
- Sleep hours
- Social Media hours
- Netflix hours
- Exercise frequency

The categories expected to be most profitable were increased to predict
the impact on exam score. These categories were: sleep hours, study
hours and exercise frequency. Meanwhile, a Decision Tree model was
utilised to predict whether a student would obtain an exam score above
75% or not.

# Project Insights

1.  Books open doors, but rest keeps you standing.

- High correlation between exam scores and both mental health rating and
  study hours were found.

- **Suggested Niche Industries: Health Focused**

1.  Exam success isn’t random — it scales with study time, peaking
    around 3.5 hours.

- Average study time is around 3.5 hours

- **Suggested Niche Industries: Gamifying Studying, Study Timers,
  Endurance Supplements**

3\. Connection quality peaks early — after that, it’s all you.

- Better internet access were correlated to higher exam scores,
  regardless of gender.

- **Suggested Niche Industries: Study Cafes, Habit Reinforcement Apps**
