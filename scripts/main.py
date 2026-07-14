import os
from dotenv import load_dotenv

from fetch_kobo import fetch_kobo
from merge import merge_data

load_dotenv()

BUILDINGS = os.getenv("BUILDING_FILE")
OUTPUT = os.getenv("OUTPUT_FILE")


print("Downloading Kobo submissions...")
kobo = fetch_kobo()

print(f"Retrieved {len(kobo)} records")

print("Joining data...")

merged = merge_data(BUILDINGS, kobo)

print(f"Writing {len(merged)} features...")

merged.to_file(
    OUTPUT,
    driver="GeoJSON"
)

print("Finished.")
