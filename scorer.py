

'''Scoring algorithm for the IMFS Summer Data SCience Competition.
Algo goes through each submitted csv and applies AUC and RMSE.
Algo then ranks team based on best AUC/RMSE'''

__author__ = 'eunice hameyie'
__version__ = 'v1.0'

# Import packages
import pandas as pd
import glob, os, re, datetime, time, csv
from unidecode import unidecode

# Track time
startTime = time.time()
today_date = datetime.datetime.now().strftime('%Y/%m/%d')

#Score phase 1
def score_phase1(file):
    '''Scoring the first leg of the IMFS summer competition'''
    file_true = 'dataset/Phase 1 - similarityCompetition/test_realval.csv' #test_original.csv'
    df = pd.read_csv(file)
    df['same_security'] = (df['same_security']).astype(int)
    df_true = pd.read_csv(file_true)
    df_true['same_security'] = (df_true['same_security']).astype(int)

    # print(df.head(2))
    # print(df_true.head(2))

    ## Score
    truepositive_negative = df_true[df_true['same_security'] == df['same_security']]
    falsepositive_negative = df_true[df_true['same_security'] != df['same_security']]
    truepositive = truepositive_negative[truepositive_negative['same_security'] == 1]['same_security'].count()
    truenegative = truepositive_negative[truepositive_negative['same_security'] == 0]['same_security'].count()
    falsepositive = falsepositive_negative[falsepositive_negative['same_security'] == 1]['same_security'].count()
    falsenegative = falsepositive_negative[falsepositive_negative['same_security'] == 0]['same_security'].count()
    allpositives = df_true[df_true['same_security'] == 1]['same_security'].count()
    allnegatives = df_true[df_true['same_security'] == 0]['same_security'].count()

    recall = 100.0 * truepositive/allpositives
    precision = 100.0 * truepositive/(truepositive+falsepositive)
    accuracy = 100.0 * (truepositive+truenegative)/(allpositives+allnegatives)
    f_measure = 2.0/((1/precision) + (1/recall))
    print('recall is %.2f, and precision is %.2f, and accuracy is %.2f, and f_measure is %.2f' %(recall, precision, accuracy, f_measure))
    return recall, precision, accuracy, f_measure

# Path to files
path_phase1 = "submission/Phase 1 - submission/"
all_files_phase1 = glob.glob(os.path.join(path_phase1, "*.csv")) #make list of paths

# Run scoring function
recall_summary = []
precision_summary = []
accuracy_summary = []
f_measure_summary = []
team_name_summary = []

for file in all_files_phase1:
    print(file)
    # Getting the file name without extension
    file_name = os.path.splitext(os.path.basename(file))[0]
    team_name = file_name.split("_",2)[2]
    print(team_name)
    recall, precision, accuracy, f_measure = score_phase1(file)
    recall_summary.append(recall)
    precision_summary.append(precision)
    accuracy_summary.append(accuracy)
    f_measure_summary.append(f_measure)
    team_name_summary.append(team_name)

#Writing to summary csv
hdr = ['team_name'] + ['accuracy'] + ['f_measure'] #+ ['recall'] + ['precision']
phase1_summary_path = 'scores/Phase 1 - scores/' + "Phase1_scores_" + today_date.replace("/", "_") + ".csv"
phase1_summary_path_sorted = 'scores/Phase 1 - scores/' + "Phase1_scores_" + today_date.replace("/", "_") + "_sorted.csv"
with open(phase1_summary_path, "w") as csvfile:
    writer = csv.writer(csvfile, delimiter= ",")
    writer.writerow(hdr)
    for i in range(0, len(team_name_summary)):
        toWrite = []
        toWrite.append(unidecode(team_name_summary[i]))
        toWrite.append(accuracy_summary[i])
        toWrite.append(f_measure_summary[i])
        # toWrite.append(recall_summary[i])
        # toWrite.append(precision_summary[i])
        writer.writerow(toWrite)
print('Summary table complete for phase 1')
#Sort resulting DataFrame
phase1_summary = pd.read_csv(phase1_summary_path)
phase1_summary = phase1_summary.sort_values(by=['accuracy'], ascending=False)
print(phase1_summary)
phase1_summary.to_csv(phase1_summary_path_sorted, index= False)



#Score Phase 2
def score_phase2(file):
    '''Scoring the second leg of the IMFS summer competition'''
    file_true = 'dataset/Phase 2 - stockDirection/test_original.csv'
    df = pd.read_csv(file)
    df['stock_directionality'] = (df['stock_directionality']).astype(int)
    df_true = pd.read_csv(file_true)
    df_true['stock_direction'] = (df_true['Adj Close'] - df_true['Open'])#.astype(int)
    df_true['stock_directionality'] = 0.0
    df_true.loc[df_true['stock_direction'] > 0, 'stock_directionality'] = 1.0

    # print(df.head(2))
    # print(df_true.head(2))

    ## Score
    truepositive_negative = df_true[df_true['stock_directionality'] == df['stock_directionality']]
    falsepositive_negative = df_true[df_true['stock_directionality'] != df['stock_directionality']]
    truepositive = truepositive_negative[truepositive_negative['stock_directionality'] == 1]['stock_directionality'].count()
    truenegative = truepositive_negative[truepositive_negative['stock_directionality'] == 0]['stock_directionality'].count()
    falsepositive = falsepositive_negative[falsepositive_negative['stock_directionality'] == 1]['stock_directionality'].count()
    falsenegative = falsepositive_negative[falsepositive_negative['stock_directionality'] == 0]['stock_directionality'].count()
    allpositives = df_true[df_true['stock_directionality'] == 1]['stock_directionality'].count()
    allnegatives = df_true[df_true['stock_directionality'] == 0]['stock_directionality'].count()
    # print(truepositive, truenegative, falsepositive, allpositives, allnegatives)
    recall = 100.0 * truepositive/allpositives
    precision = 100.0 * truepositive/(truepositive+falsepositive)
    accuracy = 100.0 * (truepositive+truenegative)/(allpositives+allnegatives)
    f_measure = 2.0/((1/precision) + (1/recall))
    print('recall is %.2f, and precision is %.2f, and accuracy is %.2f, and f_measure is %.2f' %(recall, precision, accuracy, f_measure))
    return recall, precision, accuracy, f_measure

# Path to files
path_phase2 = "submission/Phase 2 - submission"
all_files_phase2 = glob.glob(os.path.join(path_phase2, "*.csv")) #make list of paths

# Run scoring function
recall_summary_ph2 = []
precision_summary_ph2 = []
accuracy_summary_ph2 = []
f_measure_summary_ph2 = []
team_name_summary_ph2 = []

for file2 in all_files_phase2:
    print(file2)
    # Getting the file name without extension
    file_name_ph2 = os.path.splitext(os.path.basename(file2))[0]
    team_name_ph2 = file_name_ph2.split("_",2)[2]
    print(team_name_ph2)
    recall_ph2, precision_ph2, accuracy_ph2, f_measure_ph2 = score_phase2(file2)
    recall_summary_ph2.append(recall_ph2)
    precision_summary_ph2.append(precision_ph2)
    accuracy_summary_ph2.append(accuracy_ph2)
    f_measure_summary_ph2.append(f_measure_ph2)
    team_name_summary_ph2.append(team_name_ph2)

#Writing to summary csv
hdr2 = ['team_name'] + ['accuracy'] + ['f_measure'] #+ ['recall'] + ['precision']
phase2_summary_path = 'scores/Phase 2 - scores/' + "Phase2_scores_" + today_date.replace("/", "_") + ".csv"
phase2_summary_path_sorted = 'scores/Phase 2 - scores/' + "Phase2_scores_" + today_date.replace("/", "_") + "_sorted.csv"
with open(phase2_summary_path, "w") as csvfile:
    writer = csv.writer(csvfile, delimiter= ",")
    writer.writerow(hdr2)
    for i in range(0, len(team_name_summary_ph2)):
        toWrite2 = []
        toWrite2.append(unidecode(team_name_summary_ph2[i]))
        toWrite2.append(accuracy_summary_ph2[i])
        toWrite2.append(f_measure_summary_ph2[i])
        # toWrite.append(recall_summary_ph2[i])
        # toWrite.append(precision_summary_ph2[i])
        writer.writerow(toWrite2)
print('Summary table complete for phase 2')
#Sort resulting DataFrame
phase2_summary = pd.read_csv(phase2_summary_path)
phase2_summary = phase2_summary.sort_values(by=['accuracy'], ascending=False)
print(phase2_summary)
phase2_summary.to_csv(phase2_summary_path_sorted, index= False)

#### Combining scores for final grade
df_ph1 = pd.read_csv(phase1_summary_path_sorted)
df_ph1.columns = ['team_name','accuracy_ph1','f_measure_ph1']
df_ph2 = pd.read_csv(phase2_summary_path_sorted)
df_ph2.columns = ['team_name','accuracy_ph2','f_measure_ph2']
df_combined = pd.merge(df_ph1, df_ph2, on = 'team_name', how='outer').fillna(0)
df_combined['final_score'] = (2 * df_combined['accuracy_ph1'] + df_combined['accuracy_ph2'])/3.0
df_combined = df_combined.sort_values(by=['final_score'], ascending=False).drop(['accuracy_ph1', 'accuracy_ph2', 'f_measure_ph1', 'f_measure_ph2'], axis = 1)
print(df_combined)
df_combined.to_csv('Final_scores_' + today_date.replace("/", "_") + "_sorted.csv")

# print(df_combined)
### Splitting
# from sklearn.model_selection import train_test_split
# # Original data file
# file = 'dataset/Phase 2 - buySellCompetition/Combined_News_DJIA.csv'
# df = pd.read_csv(file)
# # Define features
# features = df.drop(['Label'], axis = 1)
# # Define predictor
# predictor = df['Label'].copy()
# # Split dataset
# X_train, X_test, y_train, y_test = train_test_split(features, predictor, test_size=0.2)
# # Output to save
# X_train.to_csv('dataset/Phase 2 - buySellCompetition/train.csv', index = False)
# X_test.to_csv('dataset/Phase 2 - buySellCompetition/test.csv', index = False)

#### git issues
# https://stackoverflow.com/questions/14744993/git-strange-branch-merge-error-that-i-am-not-sure-how-to-solve
