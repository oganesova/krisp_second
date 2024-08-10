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
![image](https://github.com/user-attachments/assets/d26cb5c8-0e2e-4e7d-bc0e-2a7f2b9b18e2)


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
## Usage
  python task_2.py

# 3.Streaming Payments Processor
![image](https://github.com/user-attachments/assets/de127eba-a03e-47c3-8b05-f7afe9d41092)


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
  
## Usage
   python task_3.py


# 4. Payment Processor
![Uploading image.png…]()


## Overview

This script processes payments from a streaming source and stores them in a remote system. The system is designed to handle a large, but finite amount of payments in a streaming fashion using two vendor functions:

- `stream_payments(callback_fn)`: Streams payments and invokes the callback function for each payment.
- `store_payments(amount_iterator)`: Stores payments provided by an iterator.

Due to incompatibilities between the two vendor functions, the script includes glue code to integrate these functions effectively.

## How It Works

1. **Stream Payments**: The `process_payments_2()` function uses `stream_payments()` to stream payments.
2. **Buffer Payments**: Payments are collected in a buffer.
3. **Store Payments**: When the buffer reaches its capacity, the payments are flushed and stored using `store_payments()`.
4. **Final Flush**: Any remaining payments in the buffer are flushed and stored after streaming completes.

## Usage
   python task_4.py

