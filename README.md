# IMFS-Summer-Kaggle

## What
The Office of Investment Management Fintech Strategies (IMFS) is excited to announce the kick-off of our second annual data science collaborative and friendly competition. This collaborative effort brings together crew from across IMG and IMS that have an interest in learning about data science and getting some hands on experience. Beginning in late June, all interested crew members will be split up into teams to participate in a Kaggle competition. Kaggle is a platform that brings together data scientists from across the world to work on data problems. The IMFS data science team has lined up an interesting problem to tackle and we hope that as many people that are interested in can join us.


## Timeline
* Kickoff - June 28th 2018
* Weekly meeting 1 - July 6th 2018
* Weekly meeting 2 - July 13th 2018
* Weekly meeting 3 - July 20th 2018
* Weekly meeting 4 - July 27th 2018
* Demo day and celebratory lunch - August 3rd 2018


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
Analysts tend to use different descriptions to refer to the same security. In this challenge, you are asked to make use of these descriptions to predict whether a pair of descriptions refers to the same security or not.

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

#### Phase 2 - stockDirection
Can you use eight years of daily news headlines to predict stock market movement?
You have historical news headlines from Reddit WorldNews Channel ranked by reddit users' votes, and only the top 25 headlines are considered for a single date. (Range: 2008-06-08 to 2016-07-01). You are also provided with Dow Jones Industrial Average (DJIA) stock data (Range: 2008-08-08 to 2016-07-01). The challenge is to use news headlines data to predict stock directionality, i.e. whether the DJIA Adj. Close value decreases, or stays the same/increases.

Some algorithms you may consider: Naives Bayes, Logistic Regression, SVM and Random Forest.

##### Refer to the "dataset" folder.
The "train.csv" = your training dataset
* Date = date stock/news were pulled
* Open = stock price at market open on the day
* High = highest stock price on the day
* Low = lowest stock price on the day
* Close = stock price at market close on the day
* Volume = volume
* Adj Close = stock price at market close, adjusted for fair value
* Top1 thru Top25 = top 25 news headlines from reddit

The "test.csv" = your test dataset used to grade your results
* Date = date stock/news were pulled
* Top1 thru Top25 = top 25 news headlines from reddit

##### Refer to the "submission" folder.
The "submission_phase2_yourteamname.csv" = what your output file must look like
* Date = date stock/news were pulled
* stock_directionality = your prediction of stock movement. Must be binary (1 if (DJIA Adj. Close - Open)>= 0 | 0 otherwise).


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
