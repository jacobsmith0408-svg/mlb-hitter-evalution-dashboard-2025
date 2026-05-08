# 2025 MLB Hitter Evalutaion Dashboard
Interactive Tableau dashboard analyzing MLB hitter performance using Statcast data.
# Dashboard Link: 
https://public.tableau.com/app/profile/jacob.smith5068/viz/mlb_hitter_eval_2025__twbx/MainDashboard#1

View Dashboard Here:
<img width="1354" height="580" alt="Screenshot 2026-05-08 at 1 32 28 PM" src="https://github.com/user-attachments/assets/e3a0afce-efe6-4a2d-aa7d-0fa1a479a47a" />


# Tools Used: 
- Tableau
- Statcast Data
- Python (pandas, pybaseball)
- Data Visualization
- Baseball Analytics Metrics

# Metrics Used: 
- wOBA (Weighted On-Base Average)
- xwOBA (Expected Weighted On-Base Average)
- Strikeout Rate (K%)
- Exit Velocity
- Launch Angle
- Custom Player Value Score

# Data Pipeline

The full data pipeline was built using Python:

1. Pull Statcast data using PyBaseball
2. Clean and filter relevant events
3. Aggregate pitch-level data to plate appearance level
4. Aggregate plate appearance data to player-level metrics
5. Calculate custom player value scores
6. Export processed data for visualization in Tableau

All data processing scripts are included in the `src/` directory.

# Tools Used

- Python
- PyBaseball
- Pandas
- NumPy
- Tableau
- Git / GitHub

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
