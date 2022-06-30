# QueraToCsv

---


- [English](#english)
    - [What is this project?](#what-is-this-project)
    - [Example Usage](#example-usage)

- [فارسی](#فارسی)

    - [این پروژه چیست؟](#این-پروژه-چیست؟)

    - [نمونه استفاده](#نمونه-استفاده)

- [Maintainer](#Maintainer)
---

# English

QueraToCSV is a simple python CLI project to convert the Quera results file into CSV files.

[Quera](https://quera.ir/) is an Iranian Learning management system (LMS) that has an online judge for programming
languages. Some Iranian universities use it to automate the evaluation of programming assignments.

Quera is currently more than an LMS and features other services such as programming contest and talent acquisition, but
this project only focuses on its use as an LMS.

## What is this project?

This project uses a simple python script to convert Quera result files into CSV.

Quera shows the score of each individual in its system and also generates a .txt log for each student submission. Most
courses tend to use Google Sheets (or Excel) to gather all the grades in one place, and lecturers or teaching assistants
usually should put the scores on the Google Sheets manually, because usually students outside of the course register in
the Quera class, and Quera's Excel output includes a lot of extra data from students of other classes and even TAs, So
the excel needs a lot of cleaning, and usually manually copy-pasting the scores was faster than cleaning this Excel.

This project is developed to automate this process. Lecturers and Teaching Assistants can get a cumulative log file for
all submissions of an assignment ordered by Student-IDs. These output files include a result.txt log file for each
student with the final score of that student in the assignment. This python project gets a CSV file of Student IDs and
then finds each student's score in those log files and puts them in another CSV file.

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

| Students | Score        |
| -------- | ------------ |
| 90101234 | 0 (or blank) |
| 90101235 | 0 (or blank) |
| 90101236 | 0 (or blank) |
| 90101237 | 0 (or blank) |

By default, it expects `Students` as the name of the Student-ID column and `Score` for the scores column, but you can
override it by `--id` and `--score` parameter.

Example:

Let us assume we have a class with students `90101234`,`90101235`,`90101236`,`90101237`. We put them in a CSV file named
students.csv.

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
│       └── other_student
│           └── result.txt
```

Now we can simply run these commands to get the csv files of scores of each assignment:

```shell
python main.py -s students.csv -d 1.csv -f scores/1
python main.py -s students.csv -d 2.csv -f scores/2
```

Also, the scores for other_student which was not in our class will be ignored, and we need not worry about cleaning the
CSV file.

Our program also handles persian alphabets for student-IDs.

<div dir="rtl">

# فارسی

QueraToCSV یک پروژه ساده پایتون برای تبدیل فایل‌نتایج کوئرا به CSV است .

[کوئرا](https://quera.ir/) یک سیستم مدیریت آموزش (LMS) به همراه سیستم داوری آنلاین برای زبان‌های برنامه‌نویسی است.
تعدادی از دانشگاه‌های ایران از کوئرا برای اتوماسیون و خودکارسازی فرآیند تصحیح تمرین‌های برنامه نویسی استفاده‌ می‌کنند.

البته کوئرا در حال حاضر فراتر از یک سیستم مدیریت آموزش است و سرویس‌های مختلفی نظیر مسابقات و آگهی‌های جذب استعداد و
استخدام هم در آن قرار گرفته‌اند. با این حال این پروژه فقط بر جنبه داوری‌ آنلاین و سیستم LMS کوئرا تمرکز دارد.

## این پروژه چیست؟

این پروژه از یک اسکریپت ساده پایتون برای تبدیل فایل‌های نتایج کوئرا به فایل CSV استفاده می‌کند.

سامانه کوئرا امتیاز هر یک از دانشجویان را در سیستم خود نشان داده و به ازای هر ارسال هر دانشجو یک فایل log هم ایجاد
می‌کنند. بیش‌تر درس‌های دانشگاه از Google Sheet (یا اکسل) برای تجمیع نمرات دانشجویان استفاده می‌کنند و مدرسان یا
دستیاران آموزشی دروس این نمرات را در نهایت در Google Sheets قرار می‌دهند. با این حال این کار معمولا به صورت دستی انجام
می‌شود، زیرا علیرغم این که کوئرا خروجی Excel هم تولید می‌کند، معمولا دانشجویانی غیر از دانشجویان اصلی درس هم در صفحه
کوئرا آن ثبت نام کرده و خروجی Excel کوئرا شامل داده‌های بسیار زیادی برای دانشجویان متفرقه و یا حتی دستیاران آموزشی
می‌شود که عملا باعث می‌شود نتوان آن ها را به صورت یکجا در Sheets کپی پیست کرد و عموما راهکار، کپی کردن دستی نمرات
دانشجویان درس است؛ زیرا تمیز کردن این فایل اکسل گاهی اوقات بیش از وارد کردن دستی نمرات زمان می‌برد.

این پروژه توسعه یافته‌است تا این فرآیند را تا حد امکان اتوماتیک کند. مدرسان و دستیاران آموزشی امکان دریافت فایل‌های Log
تمامی ارسال‌های دانشجویان برای یک تمرین و سوالات آن را به صورت تجمیعی دارند. این فایل‌های خروجی هر کدام شامل یک فایل
result.txt هستند که نمره نهایی دانشجو در آن نوشته شده است. این پروژه پایتون به عنوان ورودی یک فایل CSV شامل شماره
دانشجویی دانشجویان اصلی درس و همچنین پوشه‌ای شامل این Log ها را گرفته و در خروجی، یک CSV جدید شامل شماره دانشجویی و نمره
هر یک از دانشجویان در آن تمرین تولید می‌کند.

## نمونه استفاده

برای استفاده خیلی ساده، شما می‌توانید دستور زیر را در ریشه این مخزن گیتهاب اجرا کنید تا با کمک فایل‌های نمونه‌ای که قرار
داده شده، شاهد تولید فایل خروجی باشید:

<div dir="ltr">

```shell
python ./src/main.py -s ./example/students.csv -d ./example/1.csv -f ./example/scores/1
```

</div>

یا

<div dir="ltr">

```shell
python3 ./src/main.py -s ./example/students.csv -d ./example/1.csv -f ./example/scores/1
```

</div>

`s-`:
نشان‌دهنده فایل CSV ورودی‌ است که شماره‌دانشجویی دانشجویان در آن قرار گرفته است.

`d-`: نشان‌دهنده نام فایل CSV خروجی است.

`f-`:
نشان‌دهنده پوشه‌ای است که در آن زیرپوشه‌های شامل result.txt برای هر دانشجو وجود دارد.

فایل CSV اولیه‌ای که به عنوان ورودی می‌دهید باید ساختاری به صورت زیر داشته باشد:

<div dir="ltr">

```csv
Students,Score
90101234,   0
90101235,   0
90101236,   0
90101237,   0
```

</div>

<div dir="ltr">

| Students | Score        |
| -------- | ------------ |
| 90101234 | 0 (or blank) |
| 90101235 | 0 (or blank) |
| 90101236 | 0 (or blank) |
| 90101237 | 0 (or blank) |

</div>

به طور پیش‌ُفرض انتظار می‌رود که ستون مربوط به شماره دانشجویی‌ها به نام `Students`
بوده و ستون نمرات هم `Score`
باشد. با این حال می‌توانید این دو را به کمک
`id--`
و
`score--`
تغییر بدهید.

مثال-

فرض کنید یک کلاس داریم که شامل دانشجویانی با شماره دانشجویی‌های
`90101234`,`90101235`,`90101236`,`90101237`
باشد. این شماره‌دانشجویی‌ها معمولا در اختیار مدرسان درس هستند و به راحتی می‌توان آن‌ها را در یک CSV با فرمت بالا
کپی‌پیست کرد.

حال فرض کنید یک تمرین برنامه‌نویسی در کوئرا قرار داده‌ایم که دو سوال داشته است. با کلیک روی گزینه «دانلود ارسال‌های
نهایی، دسته بندی شده براساس سوال» یک فایل فشرده zip از کوئرا دانلود می‌کنیم.

پس از آن با استخراج این فایل zip در یک پوشه مثلا با نام scores، ساختاری مشابه زیر بدست می‌آوریم:

<div dir="ltr">

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
│       └── other_student
│           └── result.txt
```

</div>

حال به راحتی با اجرای دو دستور زیر می‌توانیم نمرات را برای دانشجویان کلاس در یک فایل csv بدست بیاوریم. نمره دانشجویان
متفرقه هم در نظر گرفته نمی‌شود و نیازی به نگرانی برای پاکسازی فایل csv نخواهیم داشت.

<div dir="ltr">

```shell
python main.py -s students.csv -d 1.csv -f scores/1
python main.py -s students.csv -d 2.csv -f scores/2
```

</div>

این برنامه، اعداد فارسی که بعضا دانشجویان به عنوان شماره دانشجویی وارد می‌کنند را هم به خوبی هندل می‌کند.

</div>

----

# Maintainer

- [Amirmahdi Namjoo](https://github.com/titansarus)
