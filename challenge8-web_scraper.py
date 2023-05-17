from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

url = 'https://www.lusakatimes.com/'
re = requests.get(url)
print(re)

soup = BeautifulSoup(re.content)

title = soup.find_all('h3', {'class': 'entry-title td-module-title'})

# Extract the text content of the topics and store them in a list
title = [element.text for element in title]


topic_counts = {}
# Count the occurrences of each topic
def count_results():
    count = 0
    for t in title:
        print(count, t.getText())
        count += 1
        topic_counts[t] = topic_counts.get(t, 0) + 1
count_results()

# Prepare the data for visualization
labels = list(topic_counts.keys())
sizes = list(topic_counts.values())

# Create a pie chart to visualize the distribution of topics
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Distribution of Topics')

# Display the pie chart
plt.show()
