# pip install pandas
import pandas as pd
import time
import os

FILE_PATH = 'price-data-set.csv'
CHUNK_SIZE = 1000
# Log progress every N rows (must be a multiple of CHUNK_SIZE)
PROGRESS_LOG_INTERVAL = 1000


def create_csv(path, num_rows):
    print(f"Creating csv file with {num_rows:,} rows...")
    df = pd.DataFrame({
        'id': range(num_rows),
        'name': [f'item_{i}' for i in range(num_rows)],
        'price': [i % 100 + 0.5 * (i % 2) for i in range(num_rows)]  # Varying prices
    })
    df.to_csv(path, index=False)
    print("csv file created successfully.")
    print("-" * 30)


if not os.path.exists(FILE_PATH):
    create_csv(FILE_PATH, 5_000)


# --- Main Processing Logic ---
def process_dataset(file_path, chunk_size, log_interval):
    """
    Processes a large CSV file chunk-by-chunk.
    Args:
        file_path (str): Path to the CSV file.
        chunk_size (int): Number of rows to read per chunk.
        log_interval (int): Frequency of logging progress (in rows).
    """
    start_time = time.time()
    total_rows = 0
    total_price_sum = 0.0
    # Use iterator=True and chunk_size to enable chunk processing
    csv_reader = pd.read_csv(
        file_path,
        chunksize=chunk_size,
        # Add 'usecols' to only load necessary columns, saving more memory
        usecols=['price']
    )
    print(f"Starting processing with CHUNK_SIZE={chunk_size:,} and LOG_INTERVAL={log_interval:,}...")
    print("-" * 60)

    try:
        for i, chunk in enumerate(csv_reader):
            current_chunk_rows = len(chunk)
            total_rows += current_chunk_rows
            total_price_sum += chunk['price'].sum()
            if total_rows % log_interval == 0:
                elapsed = time.time() - start_time
                print(f"Processed {total_rows:10,} rows | Chunk {i + 1} completed | Elapsed: {elapsed:.2f}s")
    except Exception as e:
        print(f"An error occurred during processing: {e}")
        return None, None

    end_time = time.time()
    print("-" * 60)
    print("✨ **Processing Complete** ✨")
    print(f"Total time taken: **{end_time - start_time:.2f} seconds**")

    return total_rows, total_price_sum


# Run the process
final_rows, final_sum = process_dataset(
    FILE_PATH,
    CHUNK_SIZE,
    PROGRESS_LOG_INTERVAL
)

if final_rows is not None:
    print(f"Total Rows Counted: **{final_rows:,}**")
    print(f"Total Price Sum: **{final_sum:,.2f}**")

# --- Cleanup (optional) ---
# if os.path.exists(FILE_PATH) and 'price-data-set.csv' in FILE_PATH:
#     os.remove(FILE_PATH)
#     print("-" * 30)
#     print(f"Cleaned up file: {FILE_PATH}")
