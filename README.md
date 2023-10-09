# Extract From and Organize Data Into Databases
By Qidu(Quentin) Fu

## Outline
- [1 Introduction](#1)
- [2 Methodology](#2)
- [3 Results](#3)
  - [3.1 Project 1](#3.1)
  - [3.2 Project 2](#3.2)
- [4 Acknowledgements](#4)

<a name='1'></a>
## 1 Introduction 
These repository includes two projects, specifically, these two project aim for the tasks below respectively:
- project1 (multi-table databases): Build and join tables/database to organize musical tracks with artists, albums, and genres on the [give dataset](http://www.py4e.com/code3/tracks.zip)
- project2 (mapping students and classes): Build and join tables/dataset to organize students/classes memberships on the [given dataset](https://www.py4e.com/tools/sql-intro/roster_data.php?PHPSESSID=3d761449819ed661d68425bb071933cb)

<a name='2'></a>
## 2 Methodology
To complete the aformentioned tasks, my project code files:
- (project 1) read(s) an iTunes export file in XML and produce a properly normalized database
- (project 2) read(s) roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables

<a name='3'></a>
## 3 Results 
Below presents the project results through the two different codes files. 

<a name='3.1'></a>
### 3.1 Project 1
Project 1 ([code file](https://github.com/Qidu-Quentin-Fu/SQLDatabasesWithPython/blob/1f7decb91c4a9d9d64e362569c27e2560a0d03c1/tracksProject1.py)) reads an iTunes export file in XML and produce a properly normalized database

**Image 1**

<img align='center' src='image1.png'>

<a name='3.2'></a>
### 3.2 Project 2
Project 2 ([code file](https://github.com/Qidu-Quentin-Fu/SQLDatabasesWithPython/blob/1f7decb91c4a9d9d64e362569c27e2560a0d03c1/studentRosterProject2.py))reads roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables

**Image 2**

<img align='center' src='image2.png'>

<a name='4'></a>
## 4 Acknowledgements
These are assignments completed for the coursera course: Using Databases with Python by Charles Russell Severance
