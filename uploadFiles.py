import os
import dropbox
from dropbox.files import WriteMode

class TransferData :
    def __init__(self, access_token):
        self.acces_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.acces_token)

        for root, dirs, files in os.walk(file_from):
            for name in files:
                local_path = (os.path.join(root, name))
            for name in dirs:
                local_path = (os.path.join(root, name))

            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A9POg0-iuAjHmo-Zpg6mipdC6sJ2WPc7w7bkiL7qx1a0Hh0JJfB9SC1a96NmBfaaTZbCSHLk9WZa7XwUkzf5HMUjX-GubuWk3XaVhIgD7mDsuuQL3oPN-Uvk3ihQBOl__DitUT8'

    transferData = TransferData(access_token)

    file_from = input("Please enter the file path to transfer : ")

    file_to = input("Please enter the file path to transfer to dropbox : ")

    transferData.upload_file(file_from, file_to)

    print("Your file has been moved")

main()