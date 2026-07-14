from fetch_kobo import fetch_kobo
from merge import merge_data
from github_update import upload_geojson
import os
from dotenv import load_dotenv

load_dotenv()

BUILDINGS = os.getenv("BUILDING_FILE")
OUTPUT = os.getenv("OUTPUT_FILE")

print("Fetching Kobo submissions...")
kobo = fetch_kobo()

print("Joining data...")
merged = merge_data(BUILDINGS, kobo)

merged.to_file(
    OUTPUT,
    driver="GeoJSON"
)

print("Uploading merged GeoJSON to GitHub...")
upload_geojson(OUTPUT)

print("Finished successfully.")