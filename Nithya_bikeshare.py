#!/usr/bin/env python
# coding: utf-8

# In[9]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("choose a city to analyze? Choose from Chicago, New York, Washington"))
    if city == "Chicago" : 
     print ("We are going to analyze Chichago city")
    elif city == 'New York':
     print ("We are going to analyze New York City")
    elif city == "Washington" : 
     print ("We are going to analyze Washington City")
    else: 
     print ("Please choose from 3 cities Chicago, New York or Washington")


    # get user input for month (all, january, february, ... , june)
    month = str(input("Choose the month to filter: Choose from January through June or choose all"))
    if month == "January" : 
     print ("We are filtering for January")
    elif month == 'February':
     print ("We are filtering for February")
    elif month == "March" : 
     print ("We are filtering for March")
    elif month == "April" :
     print (" We are filtering for April")
    elif month == "May" :
     print ("We are filtering for the month of May")
    elif month == "June" :
     print (" We are filtering for the month of June")
    elif month == "all" :
     print (" We are not filtering any month")
    else: 
     print ("Please choose from January through June or all")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("Choose the day to filter: Choose from Sunday through Saturday or choose all"))
    if day == "Sunday" : 
     print ("We are filtering for Sunday")
    elif day == 'Monday':
     print ("We are filtering for Monday")
    elif day == "Tuesday" : 
     print ("We are filtering for Tuesday")
    elif day == "Wednesday" :
     print (" We are filtering for Wednesday")
    elif day == "Thursday" :
     print ("We are filtering for Thursday")
    elif day == "Friday" :
     print (" We are filtering for Friday")
    elif day == "Saturday" :
     print (" We are filtering for Saturday")  
    elif day == "all" :
     print (" We are not filtering any day")
    else: 
     print ("Please choose from Sunday through Saturday or all")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['End Time'] = pd.to_datetime(df['End Time']) 
    df['month'] = df['Start Time'].dt.month_name() 
    df['day'] = df['Start Time'].dt.day_name()
    if month != "all":
     df =df[df.month == month]
    if day !="all":
     df =df[df.day == day]
    return df




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
   
    start_station = df['Start Station'].mode()[0]
    print ('Most popular start station', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most popular end station',end_station)


    # display most frequent combination of start station and end station trip
    both_station= df[['Start Station','End Station']].mode()
    print('Most popular start and end station',both_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(df['Trip Duration'].sum())
          
    # display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    if city != 'Washington':
     print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    
     print('earliest year : ',df['Birth Year'].min())
     print('latest year : ',df['Birth Year'].max())
     print('common year: ',df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


# In[10]:


if __name__ == "__main__":
	main()


# In[ ]:




