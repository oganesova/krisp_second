import logging
from collections import deque

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def stream_payments(callback_fn):
    """
    Reads payments from a payment processor and calls `callback_fn(amount)` for each payment.
    Returns when there is no more payments.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in range(10):
        callback_fn(i)

def store_payments(amount_iterator):
    """
    Iterates over the payment amounts from amount_iterator
    and stores them to a remote system.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in amount_iterator:
        print(i)

def process_payments_2():
    """
    Glue code to connect `stream_payments()` and `store_payments()`.
    Uses an in-memory buffer to collect payments and then stores them.
    """
    buffer = deque()
    buffer_size = 5  # Adjust the buffer size as necessary

    def callback_fn(amount):
        if len(buffer) >= buffer_size:
            logger.debug(f"Buffer is full. Flushing buffer: {list(buffer)}")
            store_payments(iter(buffer))
            buffer.clear()
        buffer.append(amount)
        logger.debug(f"Payment amount {amount} added to buffer")

    logger.info("Starting to stream payments")
    stream_payments(callback_fn)

    # Flush remaining payments in buffer
    if buffer:
        logger.debug(f"Flushing remaining buffer: {list(buffer)}")
        store_payments(iter(buffer))

    logger.info("Completed processing payments")

if __name__ == "__main__":
    process_payments_2()

