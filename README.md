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


# 2. Extract headers RSS
![image](https://github.com/user-attachments/assets/d26cb5c8-0e2e-4e7d-bc0e-2a7f2b9b18e2)


## Description
Create a Python script that extracts and returns article titles from an RSS feed URL using the feedparser library, with logging implemented for debugging and error handling.

## Functions :
get_headlines(rss_url: str) -> List[str]:
Purpose: Extracts and returns a list of article titles from the specified RSS feed URL.
Parameters:
rss_url (str): The URL of the RSS feed.
Returns:
A list of strings, each representing an article title.
Key Operations:
Parses the RSS feed.
Logs the progress and any errors.
Handles errors gracefully by logging and returning an empty list if parsing fails.

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
![image](https://github.com/user-attachments/assets/aea0ea24-9b41-48f3-aa7b-6f38651ffae9)


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

# 5.Configs 
![image](https://github.com/user-attachments/assets/b9b8dcea-1233-4e5d-b043-5ff2146f7d88)


## Overview

This project provides utilities for processing configuration data related to Directed Acyclic Graphs (DAGs) used in Airflow workflows. The utilities include functions for fetching and transforming values from dictionaries, handling boolean strings, and constructing FTP file prefixes. The code is equipped with logging to facilitate debugging and error tracking.

## Features

- **`get_value(data, key, default, lookup=None, mapper=None)`**: Retrieves a value from a dictionary, applying transformations and default values as needed.
- **`ftp_file_prefix(namespace)`**: Modifies a namespace string to replace the final token with 'ftp'.
- **`string_to_bool(string)`**: Converts a string to a boolean value, handling case-insensitive 'true' and 'false' inputs.
- **`config_from_dict(config_dict)`**: Processes a dictionary representing a row from a CSV file to generate a DAG configuration.

## Usage
   python task_5.py
