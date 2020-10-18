# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:16:43 2020

@author: omar.elfarouk
Credits to Get hub
"""

import time
import pandas as pd
import numpy as np

"#%Assigning dictionatreis for the cities , months and days%"
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_dic = {'1':"january", '2':"february", '3':"march", '4':"april", '5':"may", '6':"june", '12':"all"}

days_dic = {'1':"Monday", '2':"Tuesday", '3':"Wednesday", '4':"Thursday", '5':"Friday",
            '6':"Saturday", '7':"Sunday", '8':"all"}
month_intdic = {1:"january", 2:"february", 3:"march", 4:"april", 5:"may", 6:"june", 12:"all"}

days_intdic = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday",
            6:"Saturday", 7:"Sunday", 8:"all"}
letters_dic = {'a':'chicago','b':'new york city','c':'washington'}
                            #Initial code
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Good morning ! let us try to analyse some data form the US bikeshare !')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs  
    city_input = input("\nChoose any of the cities by using either 'a' for Chicago,'b' for New york city or 'c' for washington\n")
    while True:      
        try:
            letter = city_input.lower()
            z = type(city_input)
        
        except(KeyboardInterrupt == True):
            city_input = input("\n Dont try to escape, please choose an appropriate value\n")
            letter = city_input.lower()
        if(isinstance(city_input,int)or isinstance(city_input,float)):
            city_input = input("\it is a number and  not a valid value, please choose an appropriate letter\n")
            letter = city_input.lower()
        elif (isinstance(city_input,str) and (letter not in letters_dic)):
            city_input = input("\n not a valid value, please choose an appropriate letter ,either 'a','b', or 'c'\n")
            letter = city_input.lower()
        else:
            letter = city_input.lower()
            break
       
    city = letters_dic[letter]
    print("the chosen city is  \n",letters_dic[letter])
    # TO DO: get user input for month (all, january, february, ... , june)
    print("Enter the number '12' to apply no month filter to the data")
    print("Please enter 1 for January and 6 for June in that order")
    month_input = input("Enter the month you want to filter\n")
    while (month_input not in month_dic):
        month_input = input("\nInvalid input; Enter the month '12' for all \n or the month number you want to filter again from 1 to 6\n")
    monthy = month_input.lower()
    month = month_dic[monthy].lower()
    print("the chosen month is  \n",month_dic[monthy])

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("Enter number '8' to apply all weekdays filter to the data")
    print("Please enter 1 for monday and 7 for sunday in that order\n")
    day_input = input("\nEnter the day you want to filter\n")
    while (day_input not in days_dic):
        day_input = input("\nInvalid day ,Enter the day you want to filter again or number '8' for all days\n")
    
    day_in = day_input.lower()
    day = days_dic[day_in]
    print("the chosen day  is  \n",days_dic[day_in])
    print('-' * 40)
    return city, month, day
    print(CITY_DATA[city])

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

    # load data file into a dataframe
    
    df = pd.read_csv(CITY_DATA[city])

    # # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
   
        
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stat(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    #Starting the timing values
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most popular hour
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    #common_month = popular_month.lower()
    #day_in = day_input.lower()
    print('Most Popular month:', month_intdic[popular_month])

    df['day'] = df['Start Time'].dt.weekday
    # find the most popular day
    popular_day = df['day'].mode()[0]
    print('Most Popular day:', days_intdic[popular_day+1])
    #calculating the time difference by setting the timer 
    print("\n The time difference is in %s seconds." % (time.time() - start_time))
    print('-'*70)


def station_stats(df):
    """it shows the  statistics for the  most used stations and road trip."""

    print('\nCalculating The most popular stations and trip...\n')
    start_time = time.time()

    #Displaying the  most commonly used start station
    used_start_station = df['Start Station'].mode()[0]
    print("The common use start station is: " , used_start_station)

    # Displaying the  most commonly used end station
    used_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ", used_end_station)


    # Displaying the most frequent combination of start station and end station trip 
    #by adding start and end station strings
    df['start_end_station'] = df['Start Station'] + ' to ' + df['End Station']
    print(df.start_end_station.mode().loc[0])#loc is used to get the exact string values

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def trip_duration(df):
    """Displays statistics on the total travel time and average travel time"""

    print('\nCalculating travel time ...\n')
    #starting the time clock
    start_time = time.time()

    #  Display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total time travel is: ", total_travel)

    mean = df['Trip Duration'].mean()
    print("mean of trip duration is ", mean)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def user_sts(df):
    """Displays statistics on bikeshare users."""

    print('\ntrying to run the user data \n')
    #setting the clock time to start
    start_time = time.time()

    #  Displaying counts of user types
    user_type_count = df['User Type'].value_counts()
    print("User type count is ", user_type_count)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("User type count is ", gender)
    else:
        print("This data has no Gender column")
        

    #  Display statistics related to the  earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent_birth_year = df['Birth Year'].max()
        most_earliest_birth_year = df['Birth Year'].min()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("The newest birth year is {}".format(most_recent_birth_year))
        print("the earliest birth year is {}".format(most_earliest_birth_year))
        print("Most frequent birth year is {}".format(most_common_birth_year))
    else:
        print("This dataset has no birth year")
    #calculating the time taken by the clock    
    calc_time = time.time() - start_time
    print("\nThis took %s seconds." % calc_time)
    print('-'*70)


def view_raw_data(df):

# Displaying 5 values of raw data if needed
    input_argument = ["yes", "no"]
    n =5
    
    while True:
        user_input = input("\Would you like to see more 5 rows of  bike share statistics , enter yes or no  yes or no\n")
        if user_input.lower() not in input_argument:
            print("\nyour input is not valid, please try again\n")
        elif user_input == input_argument[0]:
            #displaying the first n rows and converting them to dictionary index e
            print(df[:n])
            listed = df[:n]
            #            listed = df.head(n).to_dict(orient='records')
            for item in listed:
                print(item,'\n')
            n+=5
        else:
            break

def main():
    input_argument = ["yes", "no"]
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stat(df)
        station_stats(df)
        trip_duration(df)
        user_sts(df)
        view_raw_data(df)
        
        restart_prog = input('\nWould you like to restart the program again ? Enter yes or no.\n')
        while restart_prog.lower() not in  input_argument:
            restart_prog = input('\n invalid input Would you like to restart the program again ? Enter yes or no.\n')
        if restart_prog.lower() == 'no' and restart_prog.lower()!= 'yes'  :        
            break

if __name__ == "__main__":
    main()
