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

# Repository Structure

mlb-hitter-evalution-dashboard-2025/
│
├── src/
│ ├── pull_statcast_2025.py
│ ├── build_pa_level_2025.py
│ ├── build_season_metrics_2025.py
│ ├── build_player_value_score_2025.py
│ ├── build_final_player_table_2025.py
│
├── requirements.txt
├── README.md
└── .gitignore

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
