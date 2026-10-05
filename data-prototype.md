# TrueCareer – Data Prototype (Technical Details)

[← Back to README]([https://github.com/Baaotraan0407/truecareer-career-guidance-system/blob/main/README.md])

This document explains the data side of TrueCareer: how assessment answers are turned into feature scores, how students are grouped with K-Means, and how recommendations and mentor matching work. It supports the "recommended experts" step in the customer journey.

**Live dashboard:** [View TrueCareer Dashboard](https://truecareer-career-guidance-system-j2ayh9kkh4s2pjjeufejfw.streamlit.app/)

## Dataset

File: `data/truecareer_dataset_v1_4_vietnam_context.csv`

- 800 student records
- 43 columns
- Version: v1.4

The dataset includes:

- Student background information
- Vietnamese university admission subject groups
- High-school subject orientation
- Academic skill scores
- Interest orientation scores
- Personality and work-style scores
- Learning and guidance needs
- Recommended majors, courses, mentor types and career paths

**Important:** this dataset is synthetic and used for prototype demonstration only. It does not represent real student records.

## Vietnam education context

Instead of only using traditional exam blocks, the dataset uses the column `admission_subject_group`, with common university admission combinations:

- A00 – Math, Physics, Chemistry
- A01 – Math, Physics, English
- B00 – Math, Chemistry, Biology
- C00 – Literature, History, Geography
- D01 – Math, Literature, English
- Undecided

It also includes `high_school_subject_orientation`, which reflects the student's learning orientation under Vietnam's current career-oriented upper-secondary system. This separates what students study in high school from the subject combination they may use for university admission.

## Workflow

```
Student Profile Input
↓
Career Assessment
↓
Assessment-to-Feature Mapping
↓
Student Profile Scores
↓
Data Preprocessing
↓
K-Means Clustering
↓
Cluster Interpretation
↓
Major, Course, Mentor & Career Path Recommendation
↓
Mentor Matching
↓
Dashboard Visualization
```

## 1. Assessment mapping

Assessment answers are converted into feature scores: academic strength, interests, personality, learning preference and guidance needs.

The clustering model uses 22 numeric assessment-related features. Some are mapped directly from assessment questions; others are derived from related answers using domain-informed synthetic rules.

## 2. Student clustering

K-Means is used as an exploratory method to group students with similar assessment profiles.

- Only numeric assessment features are used. Recommendation output columns are not used as inputs.
- The number of clusters is 6, based on the predefined student orientation groups in the recommendation design.

Outputs:

- `data/truecareer_clustered_output.csv`
- `data/truecareer_cluster_profile_summary.csv` (average feature scores per cluster, used to interpret each group)

| Cluster | Description |
|---|---|
| Tech-Analytical | Strong technology, logic and analytical interests |
| Business-Strategic | Interested in business, management and leadership |
| Finance-Oriented | Interested in finance, banking, data or investment |
| Social-Communicative | Strong communication, teamwork and helping orientation |
| Creative-Design | Interested in design, media, creativity and user experience |
| Balanced Explorer | Still uncertain and needs broader career exploration |

## 3. Recommendation mapping

Cluster results are combined with contextual factors (admission subject group, career priority, study budget, willingness to relocate) to recommend:

- `recommended_major`
- `recommended_courses`
- `recommended_mentor_type`
- `recommended_career_path`

These are generated through rule-based mapping after clustering.

Output: `data/truecareer_recommendation_summary.csv`

## 4. Mentor matching

Sample mentor database: `data/mentor_database.csv`

Each mentor profile has: mentor ID, name, mentor type, expertise, years of experience and price range.

Matching works in two directions, through the `recommended_mentor_type` field:

- **Student → Mentor:** a student is shown mentors whose `mentor_type` matches their `recommended_mentor_type`.
- **Mentor → Students:** a mentor can see all students who match their professional category. One mentor can support many students with similar needs.

```
Student recommended_mentor_type = Technology Mentor
↓
System shows mentors with mentor_type = Technology Mentor
```

## Dataset notes

The original `student_cluster` column is a domain-informed reference label. K-Means is used to show how students can be grouped by assessment features, so the result should be read as exploratory analysis, not a validated prediction model.

If real students take the assessment in the future, their answers can be converted into feature scores and added as real data. Real data should be anonymized before storage or analysis, and kept separate from synthetic data using the `data_type` column.

## Technologies

Python, Pandas, NumPy, Scikit-learn, Plotly, Streamlit, Axure RP, GitHub, VS Code

## How to run

```bash
pip install -r requirements.txt
```

**Validate the dataset:** loads the data, checks expected columns, duplicate student IDs and missing values.

```bash
python src/data_preprocessing.py
```

**Run K-Means:** selects the 22 features, standardizes them, runs K-Means with 6 clusters, calculates the silhouette score and saves the outputs.

```bash
python src/clustering.py
```

**Build recommendations:** shows major, mentor type and cluster distributions with sample outputs, and saves the summary.

```bash
python src/recommendation.py
```

**Open the dashboard locally:**

```bash
streamlit run dashboard/app.py
```

## Possible improvements

- Collect real assessment data
- Add more detailed university admission data
- Improve recommendations with student feedback
- Add a counselor review function
- Build a larger mentor database
- Try more advanced recommendation algorithms
- Add a real-time assessment form
- Evaluate the model with real user outcomes
