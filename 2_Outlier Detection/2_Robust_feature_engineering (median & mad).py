# module import
import sqlalchemy as sa
import pandas as pd

# connection to database
engine = sa.create_engine('sqlite:///hydro.db')
connection = engine.connect()

# read out temperature data from sensors
sql_query = '''
SELECT *
FROM temperature_sensor_{}
'''
df_temp1 = pd.read_sql(sql_query.format(1), con=connection)
df_temp2 = pd.read_sql(sql_query.format(2), con=connection)
df_temp3 = pd.read_sql(sql_query.format(3), con=connection)
df_temp4 = pd.read_sql(sql_query.format(4), con=connection)

df_temp1.head()

# Creating column 'cycle_id'
df = df_temp1.loc[:, ['cycle_id']]
df.head()

# Adding temperature sensor 1 mean, Axis 1 -> Mean per Row
df.loc[:, 'temp1_central'] = df_temp1.mean(axis=1)
df.head()

# temperature sensor 1 standard deviation
df.loc[:, 'temp1_dispersion'] = df_temp1.std(axis=1)
df.head()

# temperature sensor 2 (mean and standard deviation)
df.loc[:, 'temp2_central'] = df_temp2.mean(axis=1)
df.loc[:, 'temp2_dispersion'] = df_temp2.std(axis=1)

# temperature sensor 3 (mean and standard deviation)
df.loc[:, 'temp3_central'] = df_temp3.mean(axis=1)
df.loc[:, 'temp3_dispersion'] = df_temp3.std(axis=1)

# temperature sensor 4 (mean and standard deviation)
df.loc[:, 'temp4_central'] = df_temp4.mean(axis=1)
df.loc[:, 'temp4_dispersion'] = df_temp4.std(axis=1)

df.head()

df_temp4.iloc[[149, 150], :]

# import matplotlib
import matplotlib.pyplot as plt

#drawing figure
fig, ax = plt.subplots()

# plot line chart
df_temp4.iloc[[149, 150], :-1].T.plot(legend=True,
                                      ax=ax)

# optimise line chart
ax.set(xlabel='Time since cycle start [sec]',
       ylabel='Temperature [°C]',
       title='Temperature sensor 4 data of hydraulic pump')
ax.set_xticklabels(range(-10, 71, 10))

df_temp4.iloc[[149, 150], :].mean(axis=1)
df_temp4.iloc[[149, 150], :].std(axis=1)
df_temp4.iloc[[149, 150], :].median(axis=1)


from statsmodels.robust import mad
mad(df_temp4.iloc[[149, 150], :-1],axis=1)
df_robust = df_temp1.loc[:, ['cycle_id']]


for sensor in range(1, 5):  # for each thermometer
    
    # read in data from database
    sql_query = '''
    SELECT *
    FROM temperature_sensor_{}
    '''.format(sensor)
    df_tmp = pd.read_sql(sql_query, con=connection)
    
    df_robust.loc[:, 'temp{}_central'.format(sensor)] = df_tmp.median(axis=1)
    df_robust.loc[:, 'temp{}_dispersion'.format(sensor)] = mad(df_tmp.iloc[:, :-1], axis=1)

df_robust.head()


import seaborn as sns
sns.scatterplot(x=df.loc[:, 'temp4_central'],
                y=df_robust.loc[:, 'temp4_central'])


sns.scatterplot(x=df.loc[:, 'temp4_dispersion'],
                y=df_robust.loc[:, 'temp4_dispersion'])


# table names in database
tables = ['cooling_efficiency',
          'cooling_power',
          'machine_efficiency',
          'temperature_sensor_1',
          'temperature_sensor_2',
          'temperature_sensor_3',
          'temperature_sensor_4',
          'volume_flow_sensor_1',
          'volume_flow_sensor_2']

# columns names in DataFrames
col_names = ['cool_eff',
             'cool_power',
             'mach_eff',
             'temp_1',
             'temp_2',
             'temp_3',
             'temp_4',
             'flow_1',
             'flow_2']

# initialise DataFrames
df = df_temp1.loc[:, ['cycle_id']]
df_robust = df_temp1.loc[:, ['cycle_id']]

for s in range(len(tables)):  # for each sensor
    
    # read in data from database
    sql_query = '''
    SELECT *
    FROM {}
    '''.format(tables[s])
    df_tmp = pd.read_sql(sql_query, con=connection)
    
    # non-robust summary values
    df.loc[:, '{}_central'.format(col_names[s])] = df_tmp.mean(axis=1)
    df.loc[:, '{}_dispersion'.format(col_names[s])] = df_tmp.std(axis=1)
    
    # robust summary values
    df_robust.loc[:, '{}_central'.format(col_names[s])] = df_tmp.median(axis=1)
    df_robust.loc[:, '{}_dispersion'.format(col_names[s])] = mad(df_tmp.iloc[:, :-1], axis=1)

# pickle data
df.to_pickle('hydro_data.p')
df_robust.to_pickle('robust_hydro_data.p')

# close connection to data base
connection.close()