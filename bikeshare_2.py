import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}


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
    city_list = ('chicago', 'new york city', 'washington')
    month_list = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
    day_list = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all')
    while True:
        try:
            city = input('Name of City: ').lower()
            city_list.index(city)
            break
        except ValueError:
            print('Not an available city... Please type Chicago, New York City, or Washington.')

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Choose Month or type all: ').lower()
            month_list.index(month)
            break
        except ValueError:
            print('Not an available month... Please type a month from January through June.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Choose Day of Week or type all: ').lower()
            day_list.index(day)
            break
        except ValueError:
            print('Not an available Day... Please type a day from Monday through Sunday.')

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
    df['st_month'] = df['Start Time'].dt.month_name()
    df['st_day'] = df['Start Time'].dt.day_name()
    df['st_hour'] = df['Start Time'].dt.hour
    df['StartToEndStation'] = df['Start Station'] + ' to ' + df['End Station']
    if month.title() != 'All':
        df = df[df['st_month'] == month.title()]
    if day.title() != 'All':
        df = df[df['st_day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['st_month'].mode()[0]
    print('Most Common Month: ', popular_month)

    # display the most common day of week
    popular_day = df['st_day'].mode()[0]
    print('Most Common Day: ', popular_day)

    # display the most common start hour
    popular_hour = df['st_hour'].mode()[0]
    print('Most Common Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', popular_startstation)

    # display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('Most Common End Station: ', popular_endstation)

    # display most frequent combination of start station and end station trip
    popular_starttoendstation = df['StartToEndStation'].mode()[0]
    print('Most Common Start to End Station: ', popular_starttoendstation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tripduration_sum = str(df['Trip Duration'].sum())
    print('Sum of Trip Duration (Seconds):'+tripduration_sum)

    # display mean travel time
    tripduration_mean = str(df['Trip Duration'].mean())
    print('Mean of Trip Duration (Seconds):'+tripduration_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# User Stats 
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nUser Counts by Type:')
    print(df['User Type'].value_counts())
    if 'Gender' in df:
        # Display counts of gender
        print('\nUser Counts by Gender:')
        print(df['Gender'].value_counts())
    if 'Birth Year' in df:
        # Display earliest, most recent, and most common year of birth
        birthyear_min = df['Birth Year'].min()
        birthyear_max = df['Birth Year'].max()
        birthyear_mode = df['Birth Year'].mode()[0]
        print('\nUser Birth Year Stats:')
        print('Earliest Birth Year:', birthyear_min)
        print('Most Recent Birth Year:', birthyear_max)
        print('Most Common Birth Year:', birthyear_mode)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data = input('Want to see 5 Lines of Raw Data? Type Yes or No:').lower()
        raw_count = 1
        while raw_data == 'yes':
            r = range(0, len(df), 5)
            print(df[r[raw_count] - 5:r[raw_count]])
            raw_count += 1
            if raw_count >= len(r):
                print('End of Raw Data Reached...')
                break
            raw_data = input('See 5 More Raw Data? Type Yes or No:').lower()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
