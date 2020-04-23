import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello Friend! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for New York, Chicago or Washington?\n").lower()
    while city.lower() not in ('new york', 'chicago', 'washington'):
        city = input("Invalid selection!!!\nWould you like to see data for New York, Chicago or Washington?\n")
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month\'s data you would like to see?\nNote: only data from Jan-June is available \n").lower()
    while month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june'):
        month = input("Invalid selection!!!\nPlease select from the first six months of the year\n").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day\'s data you would like to see?\n").lower()
    while day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
        day = input("Invalid selection!!!\nPlease enter a valid day\n").lower()
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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Most Popular Month: ', months[popular_month-1])


    # TO DO: display the most common day of week
    popular_day_of_week=df['day_of_week'].mode()[0]
    print('Most Popular Day of The Week: ', popular_day_of_week)


    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Popular Start Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_Start_Station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', popular_Start_Station)


    # TO DO: display most commonly used end station
    popular_End_Station = df['End Station'].mode()[0]
    print('Most Popular End Station: ', popular_End_Station)



    # TO DO: display most frequent combination of start station and end station trip
    popular_Start_End_Station = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print('Most Popular Start-End Combination Stations: ', popular_Start_End_Station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Trip_Duration = df['Trip Duration'].sum()
    print('The Total Trips Duration: ', Total_Trip_Duration)


    # TO DO: display mean travel time
    Total_Mean_Time = df['Trip Duration'].mean()
    print('The Average Trips Time: ', Total_Mean_Time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types Are:\n', user_types)

    # TO DO: Display counts of gender
    try:
        user_genders = df['Gender'].value_counts()
        print('Counts of User Genders Are: \n', user_genders)
    except:
        print('The Gender Data For This City Is Unavailable')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_DOB = df['Birth Year'].min()
        Most_Recent_DOB = df['Birth Year'].max()
        Most_Common_DOB = df['Birth Year'].mode()[0]
        print('The Earliest Birth Year: ', Earliest_DOB)
        print('The Most Recent Birth Year: ', Most_Recent_DOB)
        print('The Most Common Birth Year: ', Most_Common_DOB)
    except:
        print('The Birth Dates Data For This City Is Unavailable')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    while True:
        raw_data_display= input('Would you like to see 5 lines of the raw data? yes/no.\n').lower()
        while raw_data_display.lower() not in ('yes', 'no'):
            raw_data_display= input('Invalid selection!!!\nPlease Type yes or no\n').lower()
        if raw_data_display.lower() == 'yes':
            print(df.head())
        else:
            break
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart.lower() not in ('yes', 'no'):
            restart= input('Invalid selection!!!\nPlease Type yes or no\n').lower()
        if restart.lower() != 'yes':
            print("GoodByee")
            break


if __name__ == "__main__":
	main()
