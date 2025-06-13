from pathlib import Path
from instagrapi import Client
import os
from dotenv import load_dotenv


def login() -> Client:
    cl = Client()
    cl.login(
        os.environ["INSTAGRAM_AKUN_USERNAME"],
        os.environ["INSTAGRAM_AKUN_PASSWORD"],
    )
    return cl


def login_and_save_session():
    cl = login()
    cl.dump_settings(Path("./instagrapi.client"))


if __name__ == "__main__":
    load_dotenv(".env")
    login_and_save_session()
