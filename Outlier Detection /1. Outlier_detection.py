# establish connection, create engine
import sqlalchemy as sa
engine = sa.create_engine('sqlite:///hydro.db')

#create inspector variable
inspector = sa.inspect(engine)
inspector.get_table_names()


# connect to engine
connection = engine.connect()

#select data via sql query
import pandas as pd
sql_query = '''
SELECT *
FROM temperature_sensor_1
'''

#read sql-query
df_temp1 = pd.read_sql(sql_query, con=connection)

print(df_temp1.shape)
df_temp1.head()


# module import
import matplotlib.pyplot as plt

# initialise figure and axes
fig, ax = plt.subplots()

# plot line chart
df_temp1.iloc[:, :-1].T.plot(legend=False,
                             ax=ax)

# optimise line chart
ax.set(xlabel='Time since cycle start [sec]',
       ylabel='Temperature [°C]',
       title='Temperature sensor 1 data of hydraulic pump')
ax.set_xticklabels(range(-10, 71, 10))


# read out data base
sql_query = '''
SELECT *
FROM temperature_sensor_2
'''
df_temp2 = pd.read_sql(sql_query, con=connection)

# initialise figure and axes
fig, ax = plt.subplots()

# plot temperature data as line chart
df_temp2.iloc[:, :-1].T.plot(legend=False,
                             ax=ax)

# optimise axes
ax.set(xlabel='Time since cycle start [sec]',
       ylabel='Temperature [°C]',
       title='Temperature sensor 2 data of hydraulic pump')
ax.set_xticklabels(range(-10, 71, 10))


# initialise figure and axes
fig, axs = plt.subplots(nrows=4,
                        figsize=[6, 12])

for sensor in range(1, 5):  # for each thermometer
    
    # read in data from database
    sql_query = '''
    SELECT *
    FROM temperature_sensor_{}
    '''.format(sensor)
    df = pd.read_sql(sql_query, con=connection)
    
    # create line chart
    df.iloc[:, :-1].T.plot(legend=False,
                           ax=axs[sensor - 1])
    
    # optimise line chart
    axs[sensor - 1].set(xlabel='Time since cycle start [sec]',
                        ylabel='Temperature [°C]',
                        title='Temperature sensor {} data of hydraulic pump'.format(sensor))
    axs[sensor - 1].set_xticklabels(range(-10, 71, 10))

fig.tight_layout()  # avoid overlapping axes text



# read in data from database for temperature sensor 4
sql_query = '''
SELECT *
FROM temperature_sensor_4
'''
df_temp4 = pd.read_sql(sql_query, con=connection)

# create histogram for cycle 145
ax = df_temp4.iloc[144, :-1].plot(kind='hist', xticks=range(30,55))

# optimise histogramm
ax.set(xlabel='Temperature [°C]',
       ylabel='Count',
       title='Temperature sensor 4 data of hydraulic pump at cycle 145')



# initialise figure and axes
fig, axs = plt.subplots(nrows=4,
                        figsize=[6, 12], 
                        sharey=True)

for sensor in range(1, 5):  # for each thermometer
    
    # read in data from database
    sql_query = '''
    SELECT *
    FROM temperature_sensor_{}
    '''.format(sensor)
    df = pd.read_sql(sql_query, con=connection)
    
    # create histogram for cycle 145
    df.iloc[144, :-1].plot(kind='hist',
                           ax=axs[sensor - 1])
    
    # optimise histogramm
    axs[sensor - 1].set(xlabel='Temperature [°C]',
                        ylabel='Count',
                        title='Temperature sensor {} data of hydraulic pump'.format(sensor))

fig.tight_layout()  # avoid overlapping axes text


#Close Database Connection
connection.close()