import time
from tqdm import tqdm

def process_items(items):
    for item in tqdm(items, desc="Processing items"):
        time.sleep(0.1)
        processed_item = item * 2
        print(f"Processed: {processed_item}")

if __name__ == "__main__":
    items_to_process = list(range(100))
    process_items(items_to_process)