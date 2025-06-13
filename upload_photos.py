from pathlib import Path
import os
from instagrapi import Client


def upload_photos(cl: Client):
    folder_path = "./photos"
    all_images = [
        Path(os.path.join(folder_path, f))
        for f in os.listdir(folder_path)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]
    all_images = sorted(all_images)

    batch_size = 20
    for i in range(0, len(all_images), batch_size):
        batch = all_images[i : i + batch_size]
        batch_number = i // batch_size + 1
        print("====================")
        print("====================")
        print([i.as_posix() for i in batch])
        print(f"Uploading batch {batch_number}")
        try:
            cl.album_upload(paths=batch, caption="")
            print(f"Uploaded batch {batch_number}")
        except Exception as e:
            print(f"Failed to upload batch {batch_number}: {e}")


if __name__ == "__main__":
    cl = Client()
    cl.load_settings(Path("./instagrapi.client"))
    upload_photos(cl)
