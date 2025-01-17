import logging
import os
import subprocess

import requests
from dotenv import load_dotenv

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

UPSTREAM_REPO = os.environ.get('UPSTREAM_REPO')
UPSTREAM_BRANCH = os.environ.get('UPSTREAM_BRANCH')
try:
    if len(UPSTREAM_REPO) == 0:
       raise TypeError
except:
    UPSTREAM_REPO = "https://github.com/yasirarism/ATidal-DL-Telegram"
try:
    if len(UPSTREAM_BRANCH) == 0:
       raise TypeError
except:
    UPSTREAM_BRANCH = 'main'

if UPSTREAM_REPO is not None:
    if os.path.exists(".git"):
        subprocess.run(["rm", "-rf", ".git"])

    update = subprocess.run(
        [
            f"git init -q \
                     && git config --global user.email yasiramunandar@gmail.com \
                     && git config --global user.name ml \
                     && git add . \
                     && git commit -sm update -q \
                     && git remote add origin {UPSTREAM_REPO} \
                     && git fetch origin -q \
                     && git reset --hard origin/{UPSTREAM_BRANCH} -q"
        ],
        shell=True,
    )

    if update.returncode == 0:
        logging.info("Successfully updated with latest commit from UPSTREAM_REPO")
    else:
        logging.error("Something went wrong while updating, check UPSTREAM_REPO if valid or not!")
