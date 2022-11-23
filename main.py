import pandas as pd
from _datetime import datetime
##
##
##
## This Program has two reqired files:
## 1. The 'Price List Website Products 2022-11.xlsx'
## 2. The 'Analytics Broadpharm Pages 20181001-20221120.csv'
## The second file gets pulled from BP UA under saved reports.
# Note that when you download the file you need to delete the first couple of lines so just the headings remain.
##

#csv_path = r'C:\Users\mschneider\Downloads\Analytics Broadpharm Pages 20181001-20221120.csv'
xl_path = r'C:\Users\mschneider\Downloads\Price List Website Products 2022-11.xlsx'
#DF_CSV = pd.read_csv(csv_path,  sep='delimiter', header=None)
#DF_CSV = pd.read_csv(csv_path)

DF_XL = pd.read_excel(xl_path)

XL = DF_XL.copy()
#Cleaning the excel
URL_xl = XL[XL.columns[0]].astype(str)
name_xl = XL[XL.columns[1]]
#Making the excel dataframe
DF1 = pd.DataFrame()
DF1['URL'] = URL_xl
DF1['name'] = name_xl

def Excel_maker(CSV):
    #Cleaning the CSV
    URL = CSV[CSV.columns[0]].astype(str)
    views = CSV[CSV.columns[1]]
    Unique_Pageviews = CSV[CSV.columns[2]]
    avg_time_on_page = CSV[CSV.columns[3]]
    entrance = CSV[CSV.columns[4]]
    bounce_rate = CSV[CSV.columns[5]]
    exit = CSV[CSV.columns[6]]
    # Additional Function for contact BP
    DF_contact = pd.DataFrame()
    DF_contact['URL'] = URL
    DF_contact['views'] = views
    DF_contact['Unique_Pageviews'] = Unique_Pageviews
    DF_contact['Avg. time on page'] = avg_time_on_page
    DF_contact['entrance'] = entrance
    DF_contact['bounce_rate'] = bounce_rate
    DF_contact['exit'] = exit
    DF_contact = DF_contact[DF_contact['URL'].str.contains('catalog=BP')]
    DF_contact['URL'] = DF_contact['URL'].str[25:]
    return DF_contact



def DF_merge(DF_contact, DF1):
    DF4 = DF_contact.merge(DF1, on='URL', how='inner')
    DF4 = DF4[['name', 'URL', 'views', 'Unique_Pageviews', 'Avg. time on page', 'entrance', 'bounce_rate', 'exit']]
    return DF4

def DF_to_CSV(name, DF4):
    DF4.to_csv(name + '.csv', index=False)

def Import_csv(path):
    data = pd.read_csv(path)
    data1 = data.copy()
    data1 = data1.dropna()
    return data1


if __name__ == '__main__':
    control = int(input(
        "Please enter the number coresponding to selection choice \n 1: Perform calculation on File \n 2: Exit \n"))
    while (control == 1):
        path = input("Please enter file path here.\n")
        name = input("What do you want to name the file. \n")
        CSV = Import_csv(path)
        DF2 = Excel_maker(CSV)
        DF3 = DF_merge(DF2, DF1)
        DF_to_CSV(name, DF3)
        print('Done')
        control = int(input(
            "Please enter the number correspondencing to selection choise \n 1: Perform calulation on File \n 2: Exit \n"))
    if (control == 2):
        print("Thank you")

