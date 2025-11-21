# module import
import sqlalchemy as sa
import pandas as pd

# connection to database
engine = sa.create_engine('sqlite:///hydro.db')
connection = engine.connect()

# read out temperature data of sensor
sql_query = '''
SELECT *
FROM temperature_sensor_{}
'''
df_temp1 = pd.read_sql(sql_query.format(1), con=connection)
df_temp2 = pd.read_sql(sql_query.format(2), con=connection)
df_temp3 = pd.read_sql(sql_query.format(3), con=connection)
df_temp4 = pd.read_sql(sql_query.format(4), con=connection)
df_temp1.head()

df_temp4.iloc[[144], :]

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
df_temp4.iloc[[144], :-1].T.plot(legend=False,
                            ax=ax)
ax.set(xlabel='Time since cycle start [sec]',
       ylabel='Temperature [°C]',
      title='Temperature sensor 4 data of hydraulic pump')
ax.set_xticklabels(range(-10, 71, 10))

# module import
import seaborn as sns

# initialise figure and axes
fig, ax = plt.subplots()

# draw scatter plot with regression line
sns.regplot(x=list(range(60)),
            y=df_temp4.iloc[144, :-1].astype(float),
            ci=False, #optional: no confidence intervall displayed
            ax=ax)

# optimise scatter plot
ax.set(xlabel='Time since cycle start [sec]',
       ylabel='Temperature [°C]',
       title='Temperature sensor 4 data of hydraulic pump\nwith linear fit')

from sklearn.linear_model import RANSACRegressor

model_ransac = RANSACRegressor(residual_threshold=1)

features = pd.DataFrame({'x': range(60)}) #erzeugt einen Dataframe
target = df_temp4.iloc[144, :-1] #erzeugt eine Series! Keinen Dataframe

model_ransac.fit(features, target)

model_ransac.inlier_mask_

# module import (in case it wasn't done before)
import seaborn as sns

# initialise figure and axes
fig, ax = plt.subplots()

# draw scatter plot
sns.scatterplot(x=list(range(60)),
                y=df_temp4.iloc[144, :-1],
                hue=model_ransac.inlier_mask_, #coloring inliers (orange) and outliers (blue)
                ax=ax)

# optimise plot
ax.set(xlabel='Time since cycle start [sec]',
       ylabel='Temperature [°C]',
       title='Temperature sensor 4 data of hydraulic pump')
ax.legend(title='Inlier')

# copy DataFrame for structure
df_temp4_outliers_mask = df_temp4.copy()

# instantiate RANSAC regression model with adjusted outlier threshold
model_ransac = RANSACRegressor(residual_threshold=1)

for cycle in range(len(df_temp4)):  # for each cycle
        
    # target vector for this cycle
    target = df_temp4.iloc[cycle, :-1]
    
    # fit model with data of this cycle
    model_ransac.fit(features, target)
    
    # save outlier mask of this cycle
    df_temp4_outliers_mask.iloc[cycle, :-1] = ~model_ransac.inlier_mask_

df_temp4_outliers_mask.head()


def outlierdetection(df_temp):
    """Detecting outliers for temperature DataFrames. Only rows with outliers will be returned. Inliers will be masked with NaN
    df_temp = placeholder for read temperature sensor DataFrame"""

    # copy DataFrame for structure
    temp_values = df_temp.copy().set_index('cycle_id')
    df_outliers_mask = temp_values.copy()
    
    # instantiate RANSAC regression model with adjusted outlier threshold
    model_ransac = RANSACRegressor(residual_threshold=1)

    for cycle in range(len(df_temp)):  # for each cycle

        # target vector for this cycle
        features = pd.DataFrame({'x': range(60)})
        target = temp_values.iloc[cycle, :]

        # fit model with data of this cycle
        model_ransac.fit(features, target)

        # save outlier mask of this cycle
        df_outliers_mask.iloc[cycle, :] = ~model_ransac.inlier_mask_

    # filter only outlier values
    outlier_values = temp_values[df_outliers_mask]

    # return only rows that contain outliers
    output = outlier_values[~outlier_values.isna().all(axis=1)]
    return output


df_temp1_outliers = outlierdetection(df_temp1)
df_temp2_outliers = outlierdetection(df_temp2)
df_temp3_outliers = outlierdetection(df_temp3)
df_temp4_outliers = outlierdetection(df_temp4)


with pd.ExcelWriter('temp_outliers.xlsx') as writer:  
    df_temp1_outliers.to_excel(writer, sheet_name='df_temp1_outliers')
    df_temp2_outliers.to_excel(writer, sheet_name='df_temp2_outliers')
    df_temp3_outliers.to_excel(writer, sheet_name='df_temp3_outliers')
    df_temp4_outliers.to_excel(writer, sheet_name='df_temp4_outliers')


# close connection to data base
connection.close()