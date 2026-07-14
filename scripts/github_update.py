from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
REPOSITORY = os.getenv("GITHUB_REPOSITORY")


def upload_geojson(filepath):

    github = Github(TOKEN)

    repo = github.get_repo(REPOSITORY)

    filename = os.path.basename(filepath)

    repo_path = f"data/{filename}"

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        existing = repo.get_contents(repo_path)

        repo.update_file(
            path=existing.path,
            message="Automatic update from Kobo API",
            content=content,
            sha=existing.sha
        )

        print("Updated existing GeoJSON.")

    except Exception:

        repo.create_file(
            path=repo_path,
            message="Initial upload from Kobo API",
            content=content
        )

        print("Uploaded new GeoJSON.")