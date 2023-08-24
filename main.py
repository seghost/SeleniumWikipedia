from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt

# select wikipedia pages to use, depending on the localization of wikipedia write in spanish or english
# https://es.wikipedia.org/wiki/ español
# https://en.wikipedia.org/wiki/ english
driver = webdriver.Chrome()
article_titles = [
    "Python (programming language)",
    "Automobile",
    "Data science",
    "Bye Bye Baby",
]

values = []
# iterate trough each page and get the count of the amount of headlines in each page
for title in article_titles:
    url = "https://es.wikipedia.org/wiki/" + title
    driver.get(url)

    headline_counter = driver.find_elements(By.CLASS_NAME, "mw-headline")
    headlines = len(headline_counter)
    # values are stored here
    values.append(headlines)
# data for the pie chart keys/values
data = {
    article_titles[0]: values[0],
    article_titles[1]: values[1],
    article_titles[2]: values[2],
    article_titles[3]: values[3]
}

labels = data.keys()
sizes = data.values()
# formatting of the pie chart
plt.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100), startangle=140)
plt.axis('equal')

plt.show()
