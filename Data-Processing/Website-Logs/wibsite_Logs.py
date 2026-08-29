import pandas as pd

#load the file
df = pd.read_csv('website_logs.csv')

#datetime column
df['datetime'] = pd.to_datetime(df['date'] + " " + df['time'])

#remove duplicates
df = df.drop_duplicates()

#convert status to numeric
df['status'] = pd.to_numeric(df['status'])

#print
print(df.head())

#top visited page
top_pages = df["page"].value_counts()
print("Top visited pages:")
print(top_pages)
 
#filyter rows which include 404
error_404 = df[df["status"] == 404]
print(error_404)

#konsy page per erroe zyada hy
error_pages = error_404["page"].value_counts()
print("404 Error pages:")
print(error_pages)

#most active ips
top_ips = df["ip_address"].value_counts()
print("Most active ips:")
print(top_ips)

#new csv clean file
df.to_csv('Website_logs_clean.csv' , index = False)
