import time
import calendar
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyse.

    Returns:
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington).

    while True:
        city = input('We have collected data in three major US cities:\nChicago, New York City, Washington.\n'\
        'Which city would you like to know more about? ')
        if city.title() == 'New York':
            city = 'New York City'
            break
        elif city.title() not in ('Washington','New York City','Chicago'):
           print('\nSorry, we don\'t have any data on that city.')
           continue
        else: 
            break
    print('\nAlright! Let\'s learn about bikesharing in {}.\n'.format(city.title()))
    
    # TO DO: Would you like to filter the data? -> if yes, month or day -> which

    while True: 
        print('Would you like to filter the data?')
        f_yes_no = input('Please enter y/n: ')
        if f_yes_no.lower() not in ('y','n','yes','no'):
            print('Sorry, I didn\'t understand. Can you repeat that?')
            continue
        else: 
            break
    if f_yes_no == 'n' or f_yes_no == 'no':
        print('\nOkay, bird\'s-eye view it is!')
        month = 'all'
        day = 'all'
    else:
        print('\nCool, do you want to filter by month or day of the week?')
        while True: 
            m_d = input('Please enter month/day: ')
            if m_d.lower() not in ('month','day'):
                print('\nSorry, I didn\'t understand. Can you repeat that?')
                continue
            else:
                break
        if m_d.lower() == 'month':
            day = 'all'
            print('\nMonth it is! Which month would you like to filter by?')
            while True:
                month = input('\nPlease choose from January, February, March, April, May, June: ')
                if month.title() not in ('January', 'February', 'March', 'April', 'May', 'June'):
                    print('Sorry, did you spell that correctly? We only have data from January till June')
                    continue
                else:
                    break
            print('\nAlright, let\'s see the info on {}'.format(month.title()))
        else:
            month = 'all'
            print('\nDay it is! Which day of the week would you like to filter by?')
            while True:
                day = input('\nPlease choose from Monday, Tuesday, Wednesday, Friday, Saturday, Sunday: ')
                if day.title() not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
                    print('Sorry, did you spell that correctly?')
                else:
                    break
            print('\nAlright, let\'s see the info on {}\'s'.format(day.title()))

                

    print('-'*40)
    return city.lower(), month.lower(), day.lower()

#TO DO: load the appropriate data in a dataframem

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    popular_month = df['month'].mode()[0]
    print('The most popular month was {}.'.format(calendar.month_name[popular_month]))

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day of the week was {}.'.format(popular_day))

    # TO DO: display the most common start hour

    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular hour to start cycling was {}.00h.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start_st = df['Start Station'].mode()[0]
    print('The most popular station to start from was {}.'.format(popular_start_st))

    # TO DO: display most commonly used end station

    popular_end_st = df['End Station'].mode()[0]
    print('\nThe most popular station to end at was {}.'.format(popular_end_st))

    # TO DO: display most frequent combination of start station and end station trip
    
    popular_combi = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('\nThe most popular combination of start and and station was: \n{}.'.format(popular_combi))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time_h = int(sum(df['Trip Duration']) / 60)
    print('The total travel time in hours was %s hours.' % total_travel_time_h)
    

    # TO DO: display mean travel time
    mean_travel_time = int((df['Trip Duration'].mean()))
    print('\nThe average travel time in minutes was %s minutes.' % mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print('These were the user types & counts:\n{}\n'.format(user_types))


    # TO DO: Display counts of gender

    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print('This was the division in gender:\n{}\n'.format(user_gender))
    else:
        print('There is no data available on gender for this city')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        youngest_user = int(max(df['Birth Year']))
        oldest_user = int(min(df['Birth Year']))
        popular_birth_year = int(df['Birth Year'].mode()[0])
        print('The youngest user was born in {}.'.format(youngest_user))
        print('The oldest user was born in {}.'.format(oldest_user))
        print('The most popular birth year was {}.'.format(popular_birth_year))
    else: 
        print('\nThere is no data available on birth years for this city')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Asks user to see raw data."""
    while True:
        raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if raw_data not in ('yes','no'):
            print('Sorry, I didn\'t understand. Could you repeat that?')
            continue
        else: 
            break
    i = 0
    while raw_data.lower() == 'yes' and i + 5 <df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5
            raw_data = input('Would you like to see 5 lines of raw data? Enter yes or no.\n')
        
    print('-'*40)
                     

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
