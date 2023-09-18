# SQLDatabasesWithPython
By Qidu(Quentin) Fu

## Outline
- [1 Introduction](#1)
- [2 Methodology](#2)
- [3 Results](#3)
  - [3.1 Project 1](#3.1)
  - [3.2 Project 2](#3.2)
- [Acknowledgements](#4)

<a name='1'></a>
## 1 Introduction 
These repository includes two projects, specifically, these two project aim for the tasks below respectively:
- project1 (multi-table databases): Build and join tables/database to organize musical tracks with artists, albums, and genres on the [give dataset](http://www.py4e.com/code3/tracks.zip)
- project2 (mapping students and classes): Build and join tables/dataset to organize students/classes memberships on the [given dataset](https://www.py4e.com/tools/sql-intro/roster_data.php?PHPSESSID=3d761449819ed661d68425bb071933cb)

<a name='2'></a>
## Methodology
To complete the aformentioned tasks, my project code files:
- (project 1) read an iTunes export file in XML and produce a properly normalized database
- (project 2) read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables

<a name='3'></a>
## Results 
Content below presents and visualizes the answers to the questions in the introduction. 

<a name='3.1'></a>
### 3.1 Project 1
Customers were segmented into three categories(which included seven clusters). Specially, as image 1 shown, 75% customers were in the inactive/infrequent category, about 17% customers were in the recent/low-spending group, whereas around 8% were in the high value/frequent group. 

**Image 1**

<img align='center' src='images/image1.png' width=800, height=600>

Specifically, these categories included (as the table 1 below shown):
  - Inactive/Infrequent Customers: clusters 0
  - Recent/Low-Spending Customers: clusters 4 & 6
  - High Value/Frequent Customers: clusters 1, 2, 3, 5, & 7


<a name='3.2'></a>
### 3.2 Project 2
Less than 10% items (around 34000 out of 400000) were of high value/purchased frequently (as the image below shown).


**Image 3**

<img align='center' src='images/image3.png' width=800, height=600>

<a name='4'></a>
## Acknowledgements
These are assignments completed for the coursera course: Using Databases with Python by Charles Russell Severance
