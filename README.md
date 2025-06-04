# COVID-19 Clinical Trials: EDA & Power BI Dashboard

---

## **Project Overview**

This project provides an in-depth **Exploratory Data Analysis (EDA)** of global **COVID-19 clinical trials** data, complemented by an **interactive Power BI dashboard**. The primary goal is to uncover key trends, patterns, and insights related to trial statuses, phases, start dates, age demographics, and intervention types.

---

## **Key Features & Analysis**

* **Comprehensive Data Cleaning & Preprocessing:** Handled missing values, converted data types, and addressed duplicates to ensure data quality.
* **Temporal Analysis of Trial Starts:** Visualized the evolution of trial initiations over time, highlighting periods of high research activity during the pandemic.
* **Trial Status Distribution:** Explored the breakdown of trials by their current status (e.g., completed, recruiting, terminated), providing an overview of the research landscape.
* **Clinical Phase Breakdown:** Analyzed the distribution of trials across different clinical phases (e.g., Phase 1, Phase 2, Phase 3), showing the progression of research.
* **Age Group Demographics:** Investigated the most common age groups targeted in these trials.
* **Relationship Analysis:** Examined the interplay between trial statuses and phases, and explored common outcome measures associated with various conditions.
* **Interactive Power BI Dashboard:** A dynamic dashboard built to allow users to interactively explore the cleaned data, filter by various parameters, and drill down into specific insights.

---

## **Tools & Technologies**

* **Python:**
    * `pandas`: For robust data manipulation and analysis.
    * `matplotlib.pyplot`: For static data visualizations.
    * `seaborn`: For enhanced statistical data visualizations.
* **Power BI:** For creating a comprehensive, interactive, and shareable data dashboard.

---
## Data Source

The dataset used for this analysis is `COVID clinical trials.csv`, containing information on clinical trials related to COVID-19.
* **Local Copy:** [View Dataset File in this Repository](https://github.com/BIKRAMADITTYA/COVID-Clinical-Trials-EDA-Dashboard/blob/main/COVID%20clinical%20trials.csv) 
## **Project Structure**

---

<pre>
COVID-19 Clinical Trials: EDA & Power BI Dashboard/
├── data/
│   └── COVID clinical trials.csv
├── notebooks/
│   └── covid 19 eda.py
├── power_bi_dashboard/
│   └── Clinical Trials Overview Dashboard.pbix
├── output/
│   ├── final_cleaned_trials.csv
│   ├── conditions_outcomes_summary.csv
│   ├── status_vs_phases.csv
│   └── trial_counts_over_time.csv
├── images/
│   └── [screenshots key plots]
├── .gitignore
├── README.md
└── requirements.txt
</pre>

---

## Power BI Dashboard

Explore the data interactively through the Power BI dashboard:

 * **Dashboard File:** [Clinical Trials Overview Dashboard.pbix](https://github.com/BIKRAMADITTYA/COVID-Clinical-Trials-EDA-Dashboard/blob/main/Clinical%20Trial%20Overview%20Dashboard.pbix)

 * * 📊An overview screenshot of the interactive Power BI dashboard, showing key metrics and visualizations.*

   ![Clinical Trial Overview Dashboard](https://github.com/user-attachments/assets/e6666044-6bec-4809-8c29-c16c335ba95d)

 * 
---

## Visualizations/Screenshots

Here are some key visuals from the project:
![Distribution of Phases](https://github.com/user-attachments/assets/e0f4208e-688a-4148-be67-a30171c4d81f)

*Bar chart showing the distribution of clinical trials across different phases, highlighting the prevalence of Phase 3 trials.*

![Trials Started Over Time](images/trials_over_time.png)
*Line chart showing the number of trials started each month, revealing trends in research activity.*

---
