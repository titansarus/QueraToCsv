# QueraToCsv

QueraToCSV is a simple project to convert the Quera results file into CSV files.

[Quera](https://quera.ir/) is an Iranian Learning management system (LMS) that has an online judge for programming
languages. Some Iranian universities use it to automate the evaluation of programming assignments.

Quera is currently more than an LMS and features other services such as programming contest and talent acquisition, but
this project only focuses on its use as an LMS.

## What is this project?

This project uses a simple python script to convert Quera result files into CSV.

Quera shows the score of each individual in its system and also generates a .txt log for each student
submission. Most courses tend to use Google Sheets (or Excel) to gather all the grades in one place, and lecturers or
teaching assistants usually should put the scores on the Google Sheets manually, because usually students outside of the
course register in the Quera class, and Quera's Excel output includes a lot of extra data from students of other classes
and even TAs, So the excel needs a lot of cleaning, and usually manually  copy-pasting the scores was faster than cleaning
this Excel.

This project is developed to automate this process. Lecturers and Teaching Assistants can get a cumulative log file for
all submissions of an assignment ordered by Student-IDs. These output files include a result.txt log file for each
student with the final score of that student in the assignment. This python project gets a CSV file of Student IDs
and then finds each student's score in those log files and puts them in another CSV file.
## Example Usage

For simple usage, you can use this command on the source of this repository:


```shell
python ./src/main.py -s ./example/students.csv -d ./example/1.csv -f ./example/scores/1 
```

or

```shell
python3 ./src/main.py -s ./example/students.csv -d ./example/1.csv -f ./example/scores/1 
```

`-s` indicates source CSV file that includes student-IDs.

`-d` indicates the name of output CSV.

`-f` indicates the folder in which we have subfolders for each student's assignments.

Source CSV file should have a structure like this:

```csv
Students,Score
90101234,   0
90101235,   0
90101236,   0
90101237,   0
```

| Students | Score |
|----------|-------|
| 90101234 |   0 (or blank)   |
| 90101235 |   0 (or blank)    |
| 90101236 |   0 (or blank)    |
| 90101237 |   0 (or blank)    |

By default, it expects `Students` as the name of the Student-ID column and `Score` for the scores column, but you can override it by `--id` and `--score` parameter.

Example:

Let us assume we have a class with students `90101234`,`90101235`,`90101236`,`90101237`. We put them in a CSV file named students.csv.

We have a programming assignment with two questions. We use the 'download final submission ordered by question button.'
(دانلود ارسال‌های نهایی، دسته‌بندی‌شده بر اساس سؤال) in Quera.

After that, we will have a zip. We extract it in a directory named `scores`. Now we should have a directory tree-like
this:

```tree
├── main.py
├── students.csv
├── scores
│   ├── 1
│   │   ├── 90101234
│   │   │   └── result.txt
│   │   ├── 90101235
│   │   │   └── result.txt
│   │   └── 90101236
│   │       └── result.txt
│   └── 2
│       ├── 90101234
│       │   └── result.txt
│       ├── 90101235
│       │   └── result.txt
│       └── 90101237
│           └── result.txt
```

Now we can simply run these commands to get the csv files of scores of each assignment:

```shell
python main.py -s students.csv -d 1.csv -f scores/1
python main.py -s students.csv -d 2.csv -f scores/2
```