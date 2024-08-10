import io
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def get_payments_storage():
    return io.BytesIO()

def stream_payments_to_storage(storage):
    for i in range(10):  # Simulate writing 10 chunks of data
        storage.write(bytes([1, 2, 3, 4, 5]))

def process_payments():
    """Processes payments and prints the checksum of the data written."""
    # Create an in-memory bytes buffer to capture written data
    buffer = io.BytesIO()

    # Get the storage instance (in this case, the buffer itself)
    storage = buffer

    # Define a function to calculate the checksum
    def calculate_checksum(byte_data):
        return sum(byte_data)

    logging.info("Starting to process payments...")

    try:
        # Stream payments to our in-memory storage
        logging.debug("Calling stream_payments_to_storage()")
        stream_payments_to_storage(storage)

        # Retrieve the data from the in-memory buffer
        written_data = buffer.getvalue()
        logging.debug("Data successfully written to buffer.")

        # Calculate and print the checksum
        checksum = calculate_checksum(written_data)
        logging.info(f"Checksum calculated: {checksum}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Call the modified process_payments function
process_payments()
