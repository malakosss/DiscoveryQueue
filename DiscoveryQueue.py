# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 00:08:55 2021

@author: malakoss
"""
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

def main():
    os.environ["SPOTIPY_CLIENT_ID"] = "______________________________"
    os.environ["SPOTIPY_CLIENT_SECRET"] = "_______________________________"
    os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"
    
    scope = "user-read-currently-playing user-modify-playback-state"
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path="user.cache"))
    
    startingArtist = str(input("Initiate your discovery by providing the name for your desired Starting Artist: \n (i.e., Sylvan LaCue, Jack Johnson)\n--> "))
    print("\n======================================================================")
    topSongDepth = int(input("\nDefine how many songs from the top 10 of related artists should be added to the queue: \n (i.e., 3 [top 3 songs]) \n--> "))
    print("\n======================================================================")
    countryCode = str(input("\nThe top 10 songs are by country. Define which country you would like to use: \n (use ISO 3166-1 alpha-2 country codes) \n  (i.e., US or GB or DE) \n--> ")).upper()
                                                
    results = sp.search(startingArtist, limit=1, offset=0, type='artist')
    artist_id = results['artists']['items'][0]['uri']
    related_artists = sp.artist_related_artists(artist_id)['artists']
    
    print("\n======================================================================")
    selectionMode = str(input("\nWould you like to have a choice on which related artists to include? \n YES (Y) or NO (N)\n--> ")).upper()
    
    if selectionMode in ["Y","YES"]:
        print("\n======================================================================")
        print("\nThese are your options for related artists: \n")
        a=1
        for name in related_artists:
            print("{index} -- {name}\n".format(index=a, name=name['name']))
            a += 1
    
        relatedArtist_lowbound = int(input("\nDefine the index of the first related artist that you would like to include: \n (Choose number from 1 to 19) \n--> "))
        relatedArtist_highbound = int(input("\nDefine the index of the last related artist you would like to include: \n (Must be a number higher than index of first related artist [max of 20]) \n--> "))
        
        for artist in range(relatedArtist_lowbound-1, relatedArtist_highbound):
            related_id = related_artists[artist]['uri']
            topTen = sp.artist_top_tracks(related_id, country=countryCode)['tracks']
            for song in range(0, topSongDepth):
                sp.add_to_queue(topTen[song]['uri'])
    else:
        relatedArtistAmount = int(input("\nDefine the number of related artists you would like to include: \n (Choose number from 1 to 20) \n--> "))
        
        for artist in range(0, relatedArtistAmount):
            related_id = related_artists[artist]['uri']
            topTen = sp.artist_top_tracks(related_id, country=countryCode)['tracks']
            for song in range(0, topSongDepth):
                sp.add_to_queue(topTen[song]['uri'])
    
if __name__ == "__main__":
    main()