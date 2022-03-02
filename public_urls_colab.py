# Import PyDrive and associated libraries.
# This only needs to be done once per notebook.
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
# This only needs to be done once per notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)


# example code to get public urls of pngs in google drive
newfiles = drive.ListFile({'q': "title contains '.png' and trashed=false"}).GetList()

cnt = 0
save_dic = {}
for i in newfiles:
  cnt += 1
  # if cnt > 3: break
  print(i["title"])
  print(i["webContentLink"].replace("&export=download", ""))


  save_dic[i["title"]] = i["webContentLink"].replace("&export=download", "")