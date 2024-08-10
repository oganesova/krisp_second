# Cheap Crowdfunding Problem

## Description

![image](https://github.com/user-attachments/assets/0f58dd78-2e92-4ab6-aa28-c7cb9a905c02)

This project includes a Python function `find_min_pledge` designed to solve the problem of finding the smallest positive pledge amount that has not yet been made.
The goal is to identify the minimum positive integer that is not present in a given list of already pledged amounts.
This function is useful for supporting crowdfunding projects where each pledge must be unique.

**Function Overview**:
- **Name**: `find_min_pledge`
- **Purpose**: To find the smallest positive amount that has not been pledged yet.
- **Parameters**: A list of integers representing previously made pledge amounts.
- **Returns**: The smallest positive integer that is not included in the pledge list.

**Logging**:
The function is equipped with detailed logging using Python's `logging` module.
It provides debug-level logs to help track the function's execution and understand the values being processed.

**Testing**:
The function has been tested with various inputs to ensure its correctness. Example test cases include:
- For the input `[1, 3, 6, 4, 1, 2]`, the function returns `5`.
- For the input `[1, 2, 3]`, the function returns `4`.
- For the input `[-1, -3]`, the function returns `1`.

