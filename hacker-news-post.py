#Guided Project on Exploring Hacker News Posts
#Overview of Concepts Executed 
#   Removing Headers from a List of Lists 
#   Extracting Ask HN and Show HN Posts 
#   Calculating the Average Number of Comments for Ask HN and Show HN Posts 
#   Finding the Amount of Ask HN Posts and Comments by Hour Created 
#   Calculating the Average Number of Comments for Ask HN Posts by Hour 
#   Sorting and Printing Values from a List of Lists 

#Intro
#Read in the data.
import csv
f = open('hacker_news.csv')
hn = list(csv.reader(f))   #reads the file into a list of lists 
hn[:5]  #zero not needed to indicate display of first five rows of hn

# Remove the headers.
headers = hn[0]
hn = hn[1:]
print(headers)
print(hn[:5])

# Identify posts that begin with either `Ask HN` or `Show HN` and separate the data into different lists.
#Note: we can find strings that begin with a certain word(s) by using the beginning anchor, ^, at the start of our regular expression. 
import re
ask_posts = []
show_posts =[]
other_posts = []

for post in hn:
    title = post[1]
    matchone = re.search(r"^Ask HN", title, re.I)
    matchtwo = re.search(r"^Show HN", title, re.I)
    if matchone:
        ask_posts.append(post)
    elif matchtwo:
        show_posts.append(post)
    else:
        other_posts.append(post)
        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))

# Calculate the average number of comments `Ask HN` posts receive.
ask_comments = [int(post[4]) for post in ask_posts]
avg_ask_comments = sum(ask_comments) / len(ask_posts)
print(avg_ask_comments)

# Calculate the average number of comments `Show HN` posts receive.
show_comments = [int(post[4]) for post in show_posts]
avg_show_comments = sum(show_comments) / len(show_posts)
print(avg_show_comments)

# Calculate the amount of `Ask HN` posts created during each hour of day and the number of comments received.
import datetime as dt

ask_comments = [int(post[4]) for post in ask_posts]
created_date = [post[6] for post in ask_posts] #corresponds to created_at column in ask_posts

result_list = zip(created_date, ask_comments)

comments_by_hour = {}
counts_by_hour = {}   #two empty dictionaries 
date_format = "%m/%d/%Y %H:%M" # see strptime examples at https://www.journaldev.com/23365/python-string-to-datetime-strptime

for date, comment in result_list:
    time = dt.datetime.strptime(date, date_format).strftime("%H")  #converting a string to datatime
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1  # x+=1 => x = x + 1, think of frequency_table[data_point] incrementing by 1 count
    else:
        comments_by_hour[time] = comment #refer to line 'for date, comment in result_list:' so comments are relogged into new dictionary
        counts_by_hour[time] = 1 #if is not satisfied so comment and date isn't logged, requires count to be logged in for first time as one
print(comments_by_hour)


# Calculate the average amount of comments `Ask HN` posts created at each hour of the day receive.
avg_by_hour = [[hr, comments_by_hour[hr] / counts_by_hour[hr]] for hr in comments_by_hour]
print(avg_by_hour)

# Sort the values and print the the 5 hours with the highest average comments.
avg_by_hour = sorted(avg_by_hour, key=lambda result: result[1], reverse=True)
    #the sorted run-on is a special function recommended by DQ, follows sorted(iterable, key, reverse) see: 
    #https://www.geeksforgeeks.org/sorted-function-python/ for more
print("Top 5 Hours for 'Ask HN' Comments")
for hr, avg in avg_by_hour[:5]:
    print("{}: {:.2f} average comments per post".format(dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg))
    #this {:2f}, the f refers to a floating point type
    # the .2 tells to run the first two digits after the decimal point
    #for further clarification, the first set of {} refers back to the hr introduced in for loop line
    #the second {} encasing .2f refers to the average comments represented by avg in for loop extracted from avg_by_hour data





