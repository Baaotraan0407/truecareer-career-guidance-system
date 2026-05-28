# TrueCareer: Assessment-Driven Career Guidance and Course Recommendation System

## Project Overview

TrueCareer is an assessment-driven career guidance and course recommendation prototype designed for Vietnamese high school students.

The system helps students explore suitable academic majors, courses, mentor types, and career pathways based on student profile data, assessment responses, academic orientation, and career interests.

This project demonstrates how assessment data can be transformed into structured feature scores, analyzed through clustering, and used to support personalized recommendation logic.

## Problem Background

Many Vietnamese high school students face difficulty choosing suitable university majors and future career paths. Although students may have different academic strengths, interests, family conditions, and career priorities, career guidance is often still based on general advice rather than structured assessment data.

TrueCareer addresses this issue by combining career assessment, student profile data, clustering analysis, and rule-based recommendation mapping to support early-stage career decision-making.

## Dataset

This project uses a synthetic Vietnam-context dataset:

```text
data/truecareer_dataset_v1_4_vietnam_context.csv
```

The dataset contains:

```text
800 student records
43 columns
Version: v1.4
```

The dataset includes:

* Student background information
* Vietnamese university admission subject groups
* High-school subject orientation
* Academic skill scores
* Interest orientation scores
* Personality and work-style scores
* Learning and guidance needs
* Recommended majors
* Recommended courses
* Recommended mentor types
* Recommended career paths

Important note: this dataset is synthetic and is used for prototype demonstration only. It does not represent real student records.

## Vietnam Education Context

This dataset is designed for the Vietnamese high-school and university admission context.

Instead of using only traditional exam blocks, the dataset uses the column `admission_subject_group`, including common university admission combinations such as:

* A00 - Math, Physics, Chemistry
* A01 - Math, Physics, English
* B00 - Math, Chemistry, Biology
* C00 - Literature, History, Geography
* D01 - Math, Literature, English
* Undecided

The dataset also includes `high_school_subject_orientation` to reflect students' high-school learning orientation under Vietnam's current career-oriented upper-secondary education system.

This distinction separates what students study during high school from the subject combinations they may use for university admission.

## System Workflow

```text
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
Dashboard Visualization
```

## Technical Workflow

The technical workflow includes four main steps:

### 1. Assessment Mapping

Student responses from the career assessment are converted into structured feature scores such as academic strength, interests, personality, learning preference, and guidance needs.

### 2. Student Clustering

K-Means clustering is used as an exploratory method to group students with similar assessment profiles. The model uses numeric assessment features and does not use recommendation output columns as clustering inputs.

### 3. Recommendation Mapping

Cluster results are combined with contextual factors such as admission subject group, career priority, study budget, and relocation willingness to recommend suitable majors, courses, mentor types, and career paths.

### 4. Dashboard Visualization

The system visualizes student clusters, recommended academic fields, and guidance needs to support career decision-making.

## Student Clusters

The system uses six student orientation groups:

| Cluster              | Description                                                           |
| -------------------- | --------------------------------------------------------------------- |
| Tech-Analytical      | Students with strong technology, logic, and analytical interests      |
| Business-Strategic   | Students interested in business, management, and leadership           |
| Finance-Oriented     | Students interested in finance, banking, data, or investment          |
| Social-Communicative | Students with strong communication, teamwork, and helping orientation |
| Creative-Design      | Students interested in design, media, creativity, and user experience |
| Balanced Explorer    | Students who are still uncertain and need broader career exploration  |

## Recommendation Outputs

The system provides four types of recommendation outputs:

```text
recommended_major
recommended_courses
recommended_mentor_type
recommended_career_path
```

These recommendations are generated through rule-based mapping after student clustering and profile interpretation.

## Important Dataset Note

This project uses a synthetic dataset for prototype demonstration. The dataset was generated using domain-informed rules and does not represent real student records.

The original `student_cluster` column is treated as a domain-informed reference label. K-Means clustering is used to demonstrate how students can be grouped based on numeric assessment features. Therefore, the clustering result should be understood as exploratory analysis rather than a validated predictive model.

If real students complete the assessment in the future, their responses can be converted into feature scores and added as real assessment data. Real student data should be anonymized before storage or analysis, and synthetic data should be clearly separated from synthetic prototype data using the `data_type` column.

## Project Scope

TrueCareer is a prototype system. It does not replace professional counseling or official university admission guidance. Instead, it demonstrates how assessment data, clustering analysis, and recommendation logic can support early-stage career exploration for Vietnamese high school students.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* GitHub
* VS Code

## Project Structure

```text
truecareer-career-guidance-system/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── truecareer_dataset_v1_4_vietnam_context.csv
│
├── docs/
│
├── src/
│
├── dashboard/
│
├── screenshots/
│
└── prototype/
```

## Future Improvements

Future versions of this project may include:

* Real student assessment data collection
* More detailed university admission data
* Student feedback-based recommendation improvement
* Counselor review function
* Mentor profile database
* More advanced recommendation algorithms
* Model evaluation with real user outcomes
