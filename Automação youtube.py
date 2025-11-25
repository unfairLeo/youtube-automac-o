
# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "cliente.json"

    # conseguir as  credentials e criar uma API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # executar
    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=25,
        playlistId="PLpdAy0tYrnKyjl4SSIkt0l6DFzMVmtfLd"
    )
    response = request.execute()
    videos = response["items"]
    # print(response)
    ids_video = [video["contentDetails"]["videoId"] for video in videos]

    # extrair as estatítiscas do vídeo
    request = youtube.videos().list(
        part="statistics",
        id=",".join(ids_video)
    )
    response = request.execute()
    videos = response["items"]
    for video in videos:
        id_video = video["id"]
        views = video["statistics"]["viewCount"]
        print(id_video, "-", views)


if __name__ == "__main__":
    main()