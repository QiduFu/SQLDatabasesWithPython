# Organize and Store Data Into Normalized Databases
By Qidu(Quentin) Fu

## Outline
- [1 Introduction](#1)
- [2 Projects](#2)
  - [2.1 Project 1](#2.1)
  - [2.2 Project 2](#2.2)
  - [2.3 Project 2](#2.3)
- [3 Acknowledgements](#3)

<a name='1'></a>
## 1 Introduction 
This repository includes two projects, specifically, these two project aim for the tasks below respectively:
- project1 (multi-table databases): Build a database and 4 tables to organize musical tracks with artists, albums, and genres on the [given dataset](http://www.py4e.com/code3/tracks.zip). This database uses the one-to-many design schema. 
- project2 (mapping students and classes): Build a database and 3 tables to organize students/classes memberships on the [given dataset](https://www.py4e.com/tools/sql-intro/roster_data.php?PHPSESSID=3d761449819ed661d68425bb071933cb). This database uses the many-to-many design schedma.
- project3 (mapping Instagram data with 7 tables): Design and build a database with 7 tables for organizing, normalizing, and storing Instagram data. This database uses the many-to-many design schedma. 

<a name='2'></a>
## 2 Projects

<a name='2.1'></a>
### 2.1 Project 1
Project 1 ([code file](https://github.com/Qidu-Quentin-Fu/SQLDatabasesWithPython/blob/1f7decb91c4a9d9d64e362569c27e2560a0d03c1/tracksProject1.py)) reads an iTunes export file in XML and produce a properly normalized database, containing the Artist, Albums, Genres, and Tracks tables through Python and SQLite.

<a name='2.2'></a>
### 2.2 Project 2
Project 2 ([code file](https://github.com/Qidu-Quentin-Fu/SQLDatabasesWithPython/blob/1f7decb91c4a9d9d64e362569c27e2560a0d03c1/studentRosterProject2.py)) reads roster data in JSON format, parse the file, and then produce a database that contains User, Course, and Member tables and populate the tables through Pythong and SQLite.

<a name='2.3'></a>
### 2.3 Project 3
Project 3 ([code file](https://github.com/Qidu-Quentin-Fu/SQLDatabasesWithPython/blob/1f7decb91c4a9d9d64e362569c27e2560a0d03c1/studentRosterProject2.py](https://github.com/Qidu-Quentin-Fu/SQLDatabasesWithPython/blob/main/ig_case_study.sql))) create 7 tables (including users, likes, tags, photos, comments, photo_tags, follows) based on logical modeling and populate them with Instagram data through mySQL queries. 

<a name='3'></a>
## 3 Acknowledgements
Projects 1 and 2 are completed for the Coursera's course Using Databases with Python by Charles Russell Severance available at: https://www.coursera.org/learn/python-databases. Project 3 is complerted for the Udemy's course The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert by Colt Steele available at: https://www.udemy.com/course/the-ultimate-mysql-bootcamp-go-from-sql-beginner-to-expert/. The code base, dataset, and problem statements are from the courses, but the code is written by myself.
