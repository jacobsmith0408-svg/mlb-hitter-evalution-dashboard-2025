# 2025 MLB Hitter Evalutaion Dashboard
Interactive Tableau dashboard analyzing MLB hitter performance using Statcast data.
# Dashboard Link: 
https://public.tableau.com/app/profile/jacob.smith5068/viz/mlb_hitter_eval_2025__twbx/MainDashboard

View Dashboard Here:
<img width="1360" height="613" alt="Screenshot 2026-02-15 at 5 56 39 PM" src="https://github.com/user-attachments/assets/8ee36b5a-bb93-4fd6-acce-672a19c37fce" />

# Tools Used: 
- Tableau
- Statcast Data
- Python (pandas, pybaseball)
- Data Visualization
- Baseball Analytics Metrics

# Metrics Used: 
- wOBA - actual offensive performance
- xwOBA - expected offense performance based on contact quality
- Plate Appearances (PA) - sample size indicator
- LuckGap (wOBA-xwOBA) - difference between actual and expected performance
- Player Value Score - ranking metric used to evaluate hitters
- Strikeout Rate (K%) — plate discipline metric

# Data Collection
- Statcast data was collected using Python and the pybaseball library. Python was used to retrieve player performance metrics including wOBA, xwOBA, strikeout rate, and plate appearances. The processed dataset was then used to build the interactive Tableau dashboard.

# Key Features 
- Scatter plot comparing expected vs actual performance
- League average reference lines for context
- Interactive filtering by player
- Sample size visualization using point size
- Leaderboard ranking hitters by player value score

# Analytical Purpose 
This dashboard helps to identify: 
- Hitters outperforming their expected performance (potential regression candidates)
- Hitters underperforming their expected performance (potential breakout candidates)
- Elite hitters with both high expected and actual performance
- Reliable performers based on sample size

# Project Motivation 

The goal of this project was to apply baseball analytics concepts using Statcast data and build an interactive dashboard capable of supporting player evaluation and decision-making.

# Repository Contents
- dashboard.twbx — Tableau packaged workbook
- images/dashboard.png — dashboard screenshot
- README.md — project documentation
