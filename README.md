Below is the content for your `README.md` file, formatted according to the requirements for your **8:00 PM UTC Interim Submission**. You can copy and paste this directly into your file.

***

```markdown
# African Climate Trend Analysis (Week 0)

## Overview
[cite_start]This project focuses on the exploratory data analysis (EDA) of historical climate data for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria[cite: 1, 14]. [cite_start]The analysis covers satellite-derived climate measurements from the NASA Prediction of Worldwide Energy Resources (NASA POWER) database spanning January 2015 to March 2026[cite: 23, 24].

[cite_start]The goal is to surface key climate trends, seasonal patterns, and anomalies to support Ethiopia’s data-driven position as the host of COP32 in 2027[cite: 13, 15].

## Environment Setup
Follow these steps to reproduce the development environment on Linux (Ubuntu/Mint):

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/climate-challenge-week0.git
   cd climate-challenge-week0
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Environment:**
   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure
[cite_start]The repository is organized as follows[cite: 34]:
* [cite_start]`notebooks/`: Jupyter notebooks for data cleaning and EDA (e.g., `ethiopia_eda.ipynb`)[cite: 37].
* `src/`: Source code for data processing and utility functions.
* `scripts/`: Python scripts for automated tasks.
* `tests/`: Unit tests to ensure code reliability.
* [cite_start]`.github/workflows/`: CI/CD pipeline configuration (`ci.yml`)[cite: 32].

## Data Handling
* [cite_start]**Source:** NASA POWER[cite: 23].
* **Usage:** Data files are stored locally in a `data/` directory.
* [cite_start]**Privacy:** Per project requirements, raw and cleaned `.csv` files are ignored by Git and are not committed to the repository[cite: 25, 49].

## Continuous Integration
[cite_start]This repository uses GitHub Actions to automatically run environment checks on every push to the `main` branch, ensuring that all dependencies in `requirements.txt` install correctly[cite: 32].

## Author
* **Name:** Mahlet Belay
* [cite_start]**Project:** 10 Academy: Artificial Intelligence Mastery - Week 0 Challenge [cite: 1]
```

***

### Dependencies (`requirements.txt`)
If you haven't created your `requirements.txt` yet, copy and paste this into it as well:

```text
# Data Analysis
pandas
numpy
scipy

# Visualization
matplotlib
seaborn
plotly

# Dashboard & Interactive Tools
streamlit
notebook
ipykernel
```