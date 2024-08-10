# 1. Cheap Crowdfunding Problem

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


# 2. Cheap Crowdfunding Problem

## Description

The "Cheap Crowdfunding Problem" is a task where you need to analyze and process data related to crowdfunding projects. The goal is to develop a script or application that can handle various operations related to crowdfunding, such as filtering projects, calculating statistics, and presenting results in a meaningful way.

## Installation

1. Ensure you have Python 3.x installed.
2. Install the required Python libraries:
   pip install pandas numpy
## Functions :

process_data(file_path: str) -> pd.DataFrame:
Reads and processes crowdfunding data from the specified file.
Parameters:
file_path: Path to the data file.
Returns:
A DataFrame with processed data.
calculate_statistics(df: pd.DataFrame) -> dict:

Calculates various statistics from the DataFrame.
Parameters:
df: DataFrame with crowdfunding data.
Returns:
A dictionary with calculated statistics.
filter_projects(df: pd.DataFrame, min_amount: float) -> pd.DataFrame:

Filters projects based on the minimum amount.
Parameters:
df: DataFrame with crowdfunding data.
min_amount: Minimum amount to filter projects.
Returns:
A DataFrame with filtered projects.

  python task_2.py

# 3.Streaming Payments Processor

## Overview

This project includes a function, `process_payments()`, that processes a large number of payments in a streaming fashion. It uses two main functions:

1. **`get_payments_storage()`**: Provides a storage object for writing payment data.
2. **`stream_payments_to_storage(storage)`**: Streams payment data into the provided storage.

The `process_payments()` function has been modified to compute and print a checksum of the bytes written by `stream_payments_to_storage()`.


## Functionality

1. **`process_payments()`**:
   - Initializes an in-memory buffer to capture payment data.
   - Calls `stream_payments_to_storage()` to write data to the buffer.
   - Calculates and prints the checksum of the written data.
   - 
   python task_3.py
