import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def find_min_pledge(pledge_list):
    logging.debug("Starting find_min_pledge function")

    pledged_set = set(pledge_list)
    logging.debug(f"Pledged amounts: {pledged_set}")

    min_pledge = 1
    logging.debug(f"Initial minimum pledge: {min_pledge}")

    while min_pledge in pledged_set:
        logging.debug(f"{min_pledge} is already pledged. Checking next value.")
        min_pledge += 1
        logging.debug(f"New minimum pledge to check: {min_pledge}")

    logging.debug(f"Found minimum pledge: {min_pledge}")
    return min_pledge

# Test cases
assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1
