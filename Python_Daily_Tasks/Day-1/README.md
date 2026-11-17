# Python Conditional Statement Programs

This repository contains four beginner-friendly Python programs that
practise `if`, `elif`, and `else` statements.

## Programs

### 1. Check whether a number is positive, negative, or zero

-   Positive number: greater than `0`
-   Negative number: less than `0`
-   Zero: equal to `0`

``` python
a = int(input("Enter Number: "))

if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero value")
```

### 2. Check whether a number is even or odd

A number is even when it is exactly divisible by `2`. Otherwise, it is
odd.

``` python
a = int(input("Enter the Number: "))

if a % 2 == 0:
    print("Even Number", a)
else:
    print("Odd Number", a)
```

### 3. Check age eligibility

This example classifies an age as invalid, not eligible, eligible, or
senior.

``` python
age = int(input("Enter Age: "))

if age < 0 or age > 100:
    print("Invalid")
elif age < 18:
    print("Not Eligible")
elif age < 60:
    print("Eligible")
else:
    print("Senior")
```

**Age ranges used:**

  Age                    Result
  ---------------------- --------------
  Below 0 or above 100   Invalid
  0--17                  Not Eligible
  18--59                 Eligible
  60--100                Senior

### 4. Calculate a grade from marks

The program checks the mark and prints the corresponding grade.

``` python
stu = int(input("Enter One Subject Mark: "))

if stu < 0 or stu > 100:
    print("Invalid")
elif stu > 90:
    print("Grade O")
elif stu > 80:
    print("Grade A+", stu)
elif stu > 70:
    print("Grade A", stu)
elif stu > 60:
    print("Grade B+", stu)
elif stu > 45:
    print("Grade B", stu)
elif stu > 35:
    print("Grade C", stu)
else:
    print("Work Hard", stu)
```

**Mark ranges used:**

  Marks                  Result
  ---------------------- -----------
  Below 0 or above 100   Invalid
  91--100                Grade O
  81--90                 Grade A+
  71--80                 Grade A
  61--70                 Grade B+
  46--60                 Grade B
  36--45                 Grade C
  0--35                  Work Hard

## How to Run

1.  Install Python 3.
2.  Save each program in a `.py` file, for example
    `positive_negative.py`, `even_odd.py`, `age_check.py`, and
    `grade_check.py`.
3.  Open a terminal in the folder containing the files.
4.  Run a program with:

``` bash
python filename.py
```

Replace `filename.py` with the name of the program you want to run.

## Concepts Practised

-   Reading input with `input()`
-   Converting input to an integer with `int()`
-   Using comparison operators such as `>`, `<`, and `==`
-   Using logical operators such as `or`
-   Using the modulo operator (`%`)
-   Making decisions with `if`, `elif`, and `else`

## Note

The age and marks ranges in this README use clearly defined boundary
values. Adjust the ranges if your assignment or institution follows a
different eligibility or grading system.
