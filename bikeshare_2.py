import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTH_MAPPING = {
    'jan': "january",
    'feb': "february",
    'mar': "march",
    'apr': "april",
    'may': "may",
    'jun': "june",
}

DAY_MAPPING = {
    'mon': "Monday",
    'tue': "Tuesday",
    'wed': "Wednesday",
    'thu': "Thursday",
    'fri': "Friday",
    'sat': "Saturday",
    'sun': "Sunday",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ""
    month = ""
    day = ""

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    isValid = False
    while not isValid:
        cityInput = input(
            "Please Enter A City Name (chicago, new york city, washington): ").strip().lower()
        if cityInput == "chicago" or cityInput == "new york city" or cityInput == "washington":
            isValid = True
            city = cityInput
        else:
            print("Invalid Input!")
    print(f"You chose {city}")

    # TO DO: get user input for month (all, january, february, ... , june)

    isValid = False
    while not isValid:
        monthInput = input(
            "Please Enter A Month (jan, feb, mar, apr, ..., dec) or press enter to analyze all months: ").strip().lower()
        if monthInput == "":
            month = "all"
            isValid = True
        elif monthInput in MONTH_MAPPING:
            month = MONTH_MAPPING[monthInput]
            isValid = True
        else:
            print("Invalid Input")
    print(f"You chose {month}")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    isValid = False
    while not isValid:
        dayInput = input(
            "Please Enter A Day Of The Week (mon, tue, wed, ..., sun) or press enter to analyze all days of the week: ").strip().lower()
        if dayInput == "":
            day = "all"
            isValid = True
        elif dayInput in DAY_MAPPING:
            day = MONTH_MAPPING[monthInput]
            isValid = True
        else:
            print("Invalid Input")
    print(f"You chose {day}")

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
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by month
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mostCommonMonth = df['month'].mode()[0]
    print(f"The most common month is {mostCommonMonth}")

    # TO DO: display the most common day of week
    mostCommonDay = df['day_of_week'].mode()[0]
    print(f"The most common day of week is {mostCommonDay}")

    # TO DO: display the most common start hour
    mostCommonHour = df['hour'].mode()[0]
    print(f"The most common hour is {mostCommonHour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostUsedStart = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is {mostUsedStart}")

    # TO DO: display most commonly used end station
    mostUsedEnd = df['End Station'].mode()[0]
    print(f"The most commonly used end station is {mostUsedEnd}")

    # TO DO: display most frequent combination of start station and end station trip
    mostUsedComb = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(
        f"The most commonly used start and end station combination is {mostUsedComb}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTripDuration = df['Trip Duration'].sum()
    print(f"The total trip duration is {totalTripDuration}")

    # TO DO: display mean travel time
    meanTripDuration = df['Trip Duration'].mean()
    print(f"The average travel time is {meanTripDuration}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nCounts Of User Types:")
    userTypesCount = df.groupby(['User Type']).size()
    print(userTypesCount)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print("\nCounts Of Gender:")
        genderCount = df.groupby(['Gender']).size()
        print(genderCount)

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        birthYear = df['Birth Year']
        earliestYear = birthYear.min()
        latestYear = birthYear.max()
        mostCommonYear = birthYear.mode()[0]
        print("\nBirth Year:")
        print(f"The earliest year of birth is {int(earliestYear)}")
        print(f"The most recent year of birth is {int(latestYear)}")
        print(f"The most common year of birth is {int(mostCommonYear)}")

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' and restart.lower() != 'y':
            break


if __name__ == "__main__":
    main()
