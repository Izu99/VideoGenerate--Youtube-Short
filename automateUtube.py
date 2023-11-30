import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

scopes = ["https://www.googleapis.com/auth/youtube.upload"]

def main(author):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    credentials = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # Create a MediaFileUpload object and set resumable to True to allow
    # resumable uploads.
    media = MediaFileUpload("final_video.mp4", chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
          "snippet": {
            "categoryId": "27",
            "description": f"In this video, I share a powerful quote by {author}, that will inspire you to make a positive impact in the world. This quote will motivate you to pursue your passion, overcome your challenges, and achieve your goals. Watch this video and discover how you can make a difference with one quote.",
            "title": f"How to Make a Difference in Life: A Powerful Quote by {author}",
            "tags": ["motivational quote", f"{author}", "make a difference", "inspirational video", "self improvement tips", "personal growth journey", "quotes for success", "positive mindset", "self-help advice", "personal development goals", "life lessons", "success mindset", "change your life with one quote", "motivation for life", "Life Changing", "Success Quote"]

          },
          "status": {
            "privacyStatus": "public"
          }
        },
        media_body=media
    )

    response = None
    while response is None:
        # Execute the upload request and get the response.
        status, response = request.next_chunk()

        if status:
            # If a status object exists, the upload is not yet complete,
            # so we print the amount of the file that's been uploaded.
            print("Uploaded %d%%." % int(status.progress() * 100))

    print("Upload complete!")

if __name__ == "__main__":
    main()
