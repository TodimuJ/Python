import pandas as pd

df = pd.read_csv(r'/Users/todimu/Downloads/bulkUsers.csv')



def removeColumns(oldDf):
    # Remove specific columns from the CSV file
    columns_to_remove = ['Status [READ ONLY]', 'Last Sign In [READ ONLY]', 'Email Usage [READ ONLY]']

    # Remove the columns from the DataFrame
    df = oldDf.drop(columns=columns_to_remove)

    return df

def generateEmail(domain, df):
    df.loc[1, 'Email Address [Required]'] = df.loc[1, 'First Name [Required]'].lower() + df.loc[1, 'Last Name [Required]'].lower() + f'@{domain}'
    
    for i in range(len(df)):
        # if i in numbers:
            # print(df.loc[i-2, 'First Name [Required]'])
        df.loc[i, 'Email Address [Required]'] = df.loc[i, 'First Name [Required]'].lower() + df.loc[i, 'Last Name [Required]'].lower() + f'@{domain}'

    return df

def addPassword(password, df):
    df['Password [Required]'] = password

    return df

def saveCSV(df):
    df.to_csv("/Users/todimu/Downloads/newBulkUsers.csv", index=False)


df1 = generateEmail(domain, df)
df2 = addPassword(password, df1)
saveCSV(df2)

print(df2)