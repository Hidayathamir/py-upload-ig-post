from .login_save_session import login
from .upload_photos import upload_photos

if __name__ == "__main__":
    cl = login()
    upload_photos(cl)
