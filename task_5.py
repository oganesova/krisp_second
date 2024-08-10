import logging
from enum import Enum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DeltaDays(Enum):
    DAY_BEFORE = 'DAY_BEFORE'
    DAY_AFTER = 'DAY_AFTER'


def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or returns default if the key isn't present.
    If a lookup enum is provided, this value is then transformed to its enum value.
    If a mapper function is provided, this value is then transformed by applying mapper to it.
    """
    try:
        return_value = data.get(key, default)  # Use .get() to handle missing keys safely

        if return_value is None or return_value == "":
            return_value = default

        if lookup:
            if return_value in lookup:
                return_value = lookup[return_value]
            else:
                logger.warning(f"Value {return_value} not found in lookup table.")

        if mapper:
            return_value = mapper(return_value)

        return return_value
    except Exception as e:
        logger.error(f"Error getting value for key {key}: {e}")
        raise

def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the string with
    the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    if not namespace or '.' not in namespace:
        logger.warning(f"Invalid namespace format: {namespace}")
    return ".".join(namespace.split(".")[:-1]) + '.ftp'

def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is 'false' case-insensitive.
    Raises ValueError for any other input.
    """
    string = string.strip().lower()
    if string == 'true':
        return True
    elif string == 'false':
        return False
    else:
        logger.error(f"Invalid boolean string: {string}")
        raise ValueError(f'String {string} is neither true nor false')

def config_from_dict(config_dict):
    """
    Given a dict representing a row from a namespaces CSV file,
    returns a DAG configuration as a pair whose first element is the DAG name
    and whose second element is a dict describing the DAG's properties.
    """
    try:
        namespace = config_dict.get('Namespace', '')
        if not namespace:
            logger.warning("Namespace is missing in configuration dictionary.")

        dag_name = config_dict.get('Airflow DAG', 'Unnamed DAG')
        dag_config = {
            "earliest_available_delta_days": 0,
            "lif_encoding": 'json',
            "earliest_available_time": get_value(config_dict, 'Available Start Time', '07:00'),
            "latest_available_time": get_value(config_dict, 'Available End Time', '08:00'),
            "require_schema_match": get_value(config_dict, 'Requires Schema Match', 'True', mapper=string_to_bool),
            "schedule_interval": get_value(config_dict, 'Schedule', '1 7 * * *'),
            "delta_days": get_value(config_dict, 'Delta Days', 'DAY_BEFORE', lookup=DeltaDays),  # Ensure DeltaDays is defined
            "ftp_file_wildcard": get_value(config_dict, 'File Naming Pattern', None),
            "ftp_file_prefix": get_value(config_dict, 'FTP File Prefix', ftp_file_prefix(namespace)),
            "namespace": namespace
        }

        return (dag_name, dag_config)

    except KeyError as e:
        logger.error(f"Missing key in configuration dictionary: {e}")
        raise
    except Exception as e:
        logger.error(f"Error processing configuration dictionary: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Example input dictionary
    config_dict = {
        'Namespace': 'a.b.c',
        'Airflow DAG': 'my_dag',
        'Available Start Time': '06:00',
        'Available End Time': '18:00',
        'Requires Schema Match': 'True',
        'Schedule': '0 6 * * *',
        'Delta Days': 'DAY_BEFORE',
        'File Naming Pattern': '*.csv',
        'FTP File Prefix': 'my_prefix'
    }

    # Example usage
    dag_name, dag_config = config_from_dict(config_dict)

    print(f"DAG Name: {dag_name}")
    print("DAG Configuration:")
    for key, value in dag_config.items():
        print(f"{key}: {value}")
