import time

import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", 'all']
cities = ['chicago', 'new york city', 'washington']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs

    while True:
        city = input(
            "Please enter one of the following cities you want to see data for:\n Chicago, New York City,"
            "or Washington\n")
        if city.lower() in cities:
            break
        else:
            print('The city not correct, Please enter a valid city')

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input(
            "\nPlease select the month you want to check or enter 'all' if you don't want to filter\n January, "
            "February, March, April, May, June\n")
        if month.lower() in months:
            break
        else:
            print('The month not correct, Please enter a valid month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input(
            "\nPlease select the day you want to check or enter 'all' if you don't want to filter\n Monday, Tuesday, "
            "Wednesday, Thursday, Friday, Saturday and Sunday\n")
        if day.lower() in week_days:
            break
        else:
            print('The day not correct, Please enter valid day')

    print('-' * 40)
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

    df['day'] = df['Start Time'].dt.day_name()

    df['month'] = df['Start Time'].dt.month

    if month != 'all':
        month = months.index(month)
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month from the given filtered data is: ", df['month'].max())

    # display the most common day of week
    print("The most common day from the given filtered data is: ", df['day'].mode().max())

    # display the most common start hour
    print("The most common day from the given filtered data is: ", df['Start Time'].dt.hour.mode().max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station used is: ", df['Start Station'].mode().max())

    # display most commonly used end station
    print("The most common end station used is: ", df['End Station'].mode().max())

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' - ' + df['End Station']
    print("The most common end station used is: ", df['trip'].mode().max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time = ', df['Trip Duration'].sum())
    # display mean travel time
    print('The mean travel time = ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The type of users counted as: ', df['User Type'].value_counts())

    # Display counts of gender
    try:
        print('The gender of users counted as: ', df['Gender'].value_count())
    except:
        print('Gender count not available')

    # Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth as: ', (df['Birth Year'].min()))
        print('The most recent year of birth as: ', (df['Birth Year'].max()))
        print('The most common year of birth as: ', (df['Birth Year'].mode().max()))
    except:
        print('Birth Year count not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    while True:
        count = 0
        print_data = input('\nDo you want to see the first 5 row of data ? Enter yes or no.\n ').lower()

        while print_data == 'yes':
            count = count + 5
            print(df[count:count + 5])
            while True:
                print('\nDo you want to see more data?\n')
                print_data = input()
                if print_data == 'yes':
                    count = count + 5
                    print(df[count: count + 5])
                elif print_data != "yes":
                    break
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
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
