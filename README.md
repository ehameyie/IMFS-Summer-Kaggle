# IMFS-Summer-Kaggle

## What
The Office of Investment Management Fintech Strategies (IMFS) is excited to announce the kick-off of our second annual data science collaborative and friendly competition. This collaborative effort brings together crew from across IMG and IMS that have an interest in learning about data science and getting some hands on experience. Beginning in late June, all interested crew members will be split up into teams to participate in a Kaggle competition. Kaggle is a platform that brings together data scientists from across the world to work on data problems. The IMFS data science team has lined up an interesting problem to tackle and we hope that as many people that are interested in can join us.


## Timeline
Kickoff - June 28th 2018
Weekly meeting 1 -
Weekly meeting 2 -
Weekly meeting 3 -
Weekly meeting 4 -
Demo day and celebratory lunch -


## How
Here’s a brief rundown of what you need to do:

1. Join the competition on [Slack](https://join.slack.com/t/imfsdatacomp/signup). Once in Slack, make sure to join your team's channel.
2. Review git commands. Here is a good [refresher](http://rogerdudler.github.io/git-guide/)
3. Clone this repository locally
4. Create a git branch where you will work on your own
5. Start with "Phase 1 - similarityCompetition"
6. Train your model using "train.csv"
7. Run your model using 'test.csv' as your input
8. Submit your work using the "submission_phase1_yourteamname.csv" template
9. Save your output results in the "submission" folder under "Phase 1 - submission". Make sure to name your output CSV as "submission_phase1_yourteamname.csv".
10. If you still have time, move on to "Phase 2 - buySellCompetition"
11. Train your model using "train.csv"
12. Run your model using 'test.csv' as your input
13. Submit your work using the "submission_phase2_yourteamname.csv" template
14. Save your output results in the "submission" folder under "Phase 2 - submission". Make sure to name your output CSV as "submission_phase2_yourteamname.csv".
15. Merge your branch to the main (origin) repo
16. Confirm your submissions are present in the "submission" folder in the main repository
17. Post "completed with project - yourteamname" in the "general" Slack channel

## Data and Rules

### Data

#### Phase 1 - similarityCompetition
##### Refer to the "dataset" folder.
The "train.csv" = your training dataset
* description_x = description on a security x
* description_y = description on a security y
* ticker_x = ticker for security x
* ticker_y = ticker for security y
* same_security = binary (true/False). Whether x and y refer to the same security (true) or not (false)

The "test.csv" = your test dataset used to grade your results
* description_x = description on a security x
* description_y = description on a security y
* same_security = binary (true/False). The output you need to predict.

##### Refer to the "submission" folder.
The "submission_phase1_yourteamname.csv" = what your output file must look like
* description_x = description on a security x
* description_y = description on a security y
* same_security = your predictions (binary true/false)

#### Phase 2 - buySellCompetition
##### Refer to the "dataset" folder.
The "train.csv" = your training dataset
* buysell = binary (1=buy/0=sell).

The "test.csv" = your test dataset used to grade your results
* buysell = binary (1=buy/0=sell).

##### Refer to the "submission" folder.
The "submission_phase2_yourteamname.csv" = what your output file must look like
* buysell = binary (1=buy/0=sell).

### Rules
1. We evaluate the accuracy of your predictions using [RMSE](https://www.analyticsvidhya.com/blog/2016/02/7-important-model-evaluation-error-metrics/) or [AUC](https://medium.com/@andygon/eli5-roc-curve-auc-metrics-ac4fe482f018)

2. Your submission must follow the template "submission_phasenumber_yourteamname.csv"

## Participants
### Team 1
Sharon Tsao

### Team 2
Chuqi Yang

### Team 3
Karly Jerman

### Team 4



## Scoring Board Leaders
### Leader 1 - Team x
