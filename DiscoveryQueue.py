# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 00:08:55 2021

@author: malakoss
"""
import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

def main():
    load_dotenv('.env')
    
    os.environ["SPOTIPY_CLIENT_ID"] = str(os.getenv("SPOTIPY_CLIENT_ID"))
    os.environ["SPOTIPY_CLIENT_SECRET"] = str(os.getenv("SPOTIPY_CLIENT_SECRET"))
    os.environ["SPOTIPY_REDIRECT_URI"] = str(os.getenv("SPOTIPY_REDIRECT_URI"))
    
    scope = "user-read-currently-playing user-modify-playback-state"
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    
    startingArtist = str(input("Initiated your discovery by inputting the name your desired Starting Artist: \n (i.e., Sylvan LaCue, Jack Johnson)\n-->"))
    relatedArtistAmount = int(input("Define the number of related artists you would like to include: \n (Choose number up to 20) \n-->"))
    topSongDepth = int(input("Define how many songs from the top 10 of related artists should be added to the queue: \n (i.e., 3 [top 3 songs]) \n-->"))
    countryCode = str(input("The top 10 songs are by country. Define which country you would like to use: \n (use ISO 3166-1 alpha-2 country codes) \n  (i.e., US or GB or DE) \n-->")).upper()
                                                
    results = sp.search(startingArtist, limit=1, offset=0, type='artist')
    artist_id = results['artists']['items'][0]['uri']
    related_artists = sp.artist_related_artists(artist_id)['artists']
    
    for artist in range(0, relatedArtistAmount):
        related_id = related_artists[artist]['uri']
        topTen = sp.artist_top_tracks(related_id, country=countryCode)['tracks']
        for song in range(0, topSongDepth):
            sp.add_to_queue(topTen[song]['uri'])
    
if __name__ == "__main__":
    main()