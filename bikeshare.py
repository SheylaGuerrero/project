import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data = {'january': 1,'february': 2,'march': 3,'april': 4,'may': 5,'june': 6,'july': 7,'august': 8,'september': 9,'october': 10,'november': 11,'december': 12}
day_data = {'monday': 1,'tuesday': 2,'wednesday': 3,'tuesday': 4,'friday': 5,'saturday': 6,'sunday':7}
op_data = {'month': 1,'day': 2,'both': 3,'none': 4,'all': 5}
cities = list(CITY_DATA.keys())
months = list(month_data.keys())
days = list(day_data.keys())
option = list(op_data.keys())
global city
global filteropt
global day
def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Hello! Let\'s explore some US bikeshare data!')
    city =input("Choose a city chicago,new york city, washington: ").lower()
    while city not in cities:
                city = input("Please, insert a city from the list: ").lower()
    
     
    # TO DO: get user input for month (all, january, february, ... , june)
    filteropt=input("DO you want filter by month,day,both,all,none: ").lower()
    while filteropt not in option:
                filteropt = input("Please, choose one of this options filter by month,day,both,all,none: ").lower()
    
    if filteropt == 'both':
        month =input("write a month: ").lower()
        while month not in months:
                month = input("Please, insert a correct month: ").lower()
        day =input("write a day: ").lower()
        while day not in days:
                day = input("Please, insert a correct day: ").lower()
    elif filteropt == 'month':
         month =input("write a month: ").lower()
         while month not in months:
                month = input("Please, insert a correct month: ").lower()
         day='all'
    elif filteropt == 'day':
         month='all'
         day =input("write a day: ").lower()
         while day not in days:
                day = input("Please, insert a correct day: ").lower()
    elif filteropt == 'none':
         month='all'
         day= 'all'
    elif filteropt == 'all':
         month='all'
         day= 'all'
    else:
        print('unrecognized option')
       
    
        
        
        
    print('-'*40)   
    return city, month, day,filteropt


def load_data(city, month, day,filteropt):
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
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['city']= city
    df['filt']= filteropt
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august', 'september', 'october', 'november','december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
  
    return df


def time_stats(df):
    print('Loading stadistics......')
    print(' ')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    for x in range(len(months)): 
        if common_month == x:
            print("most popular month:",common_month,months[x-1])
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    
    
    print("most popular day:",common_day)
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    counter = df['hour'].value_counts()
    ansnm=counter.max()
    ansid=counter.idxmax()
    
    print("most popular hour:",ansid,"counts:",ansnm)
    common_filt = df['filt'].mode()[0]
    print('filter:',common_filt)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_startst = df['Start Station'].mode()[0]
    counter = df['Start Station'].value_counts()
    sta_nm=counter.max()
    sta_id=counter.idxmax()

    # TO DO: display most commonly used end station
    common_endst = df['End Station'].mode()[0]
    counterend = df['End Station'].value_counts()
    end_nm=counterend.max()
    end_id=counterend.idxmax()

    # TO DO: display most frequent combination of start station and end station trip
    
    com = df.groupby(['Start Station', 'End Station']).size().reset_index(name='counts')

    count_comb=com.max()
    
     
    print ("Most common trip from start to end:",count_comb)
    print("most popular Start Station:",sta_id,"counts:",sta_nm)
    print("most popular End Station:",end_id,"counts:",end_nm)
    common_filt = df['filt'].mode()[0]
    print('filter:',common_filt)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    counts=df['Trip Duration'].count()
    # TO DO: display mean travel time
    travel = df['Trip Duration'].mean()
    
    print("duration:", trip_duration, "counts:", counts," mean:", travel)
    common_filt = df['filt'].mode()[0]
    print('filter:',common_filt)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    common_city = df['city'].mode()[0]
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Users:",user_types)
    
    if common_city == "washington":
        print("none gender nad birth year")
    else:
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest = min(df['Birth Year']) 
        recent = max(df['Birth Year'])
        common_birth = df['Birth Year'].mode()[0]
        print("Gender:",gender)
        print("earliest: ",earliest,"recent:",recent,"common year birth:",common_birth)
   
    common_filt = df['filt'].mode()[0]
    print('filter:',common_filt)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_detail():
    for row_index,row in dfn.head(n=5).iterrows():
                print('\nrow number:',row_index, '\n-------------')
                print(row)	
def main():
    while True:
        # call the method retuning data    
        city, month, day,filteropt= get_filters()

	#variable storage data from get_filters method
        df = load_data(city, month, day,filteropt)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        dfn=df
        user_input = 'yes'
        
        while user_input == 'yes':
            #iterate through each row of dataframe
            print_detail()
            
            user_input = input('\nWould you like print details rows? Enter yes or no.\n')
            if user_input =='yes':
                dfn.drop(dfn.index[0:5])
                         
            
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
