import csv

def drop_column(data, target_feature, percent, log=False, csv_report=False ):
    report = [['features name', 'missing percentage']]
    if log == True:
        for col in data.columns:
            if col != target_feature:
                #print(col)
                percent_missing = data[col].isnull().sum() * 100 / len(data[col])
                print(col, percent_missing)
                report.append([col, float("{:.3f}".format(percent_missing))])
                if percent_missing>percent:
                    data = data.drop([col], axis=1)
    else:
        for col in data.columns:
            if col != target_feature:
                #print(col)
                percent_missing = data[col].isnull().sum() * 100 / len(data[col])
                report.append([col, float("{:.3f}".format(percent_missing))])
                if percent_missing>percent:
                    data = data.drop([col], axis=1)        

    if csv_report == True:
        with open('report_missing_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            print('Generating CSV file....')
            writer.writerows(report)
   

     
    return data

data = drop_column(dataset,'RainTomorrow', 7, log=True, csv_report=True)
