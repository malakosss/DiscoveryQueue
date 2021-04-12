# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 00:08:55 2021

@author: malakoss
"""
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

def logo():
    print("\n===========================================================================================================================================")
    print("\n8888888b.  d8b                                                               .d88888b.                                      ")
    print("888  'Y88b Y8P                                                              d88P' 'Y88b                                     ")
    print("888    888                                                                  888     888                                     ")
    print("888    888 888 .d8888b   .d8888b .d88b.  888  888  .d88b.  888d888 888  888 888     888 888  888  .d88b.  888  888  .d88b.  ")
    print("888    888 888 88K      d88P'   d88''88b 888  888 d8P  Y8b 888P'   888  888 888     888 888  888 d8P  Y8b 888  888 d8P  Y8b ")
    print("888    888 888 'Y8888b. 888     888  888 Y88  88P 88888888 888     888  888 888 Y8b 888 888  888 88888888 888  888 88888888 ")
    print("888  .d88P 888      X88 Y88b.   Y88..88P  Y8bd8P  Y8b.     888     Y88b 888 Y88b.Y8b88P Y88b 888 Y8b.     Y88b 888 Y8b.     ")
    print("8888888P'  888  88888P'  'Y8888P 'Y88P'    Y88P    'Y8888  888      'Y88888  'Y888888'   'Y88888  'Y8888   'Y88888  'Y8888  ")
    print("                                                                        888        Y8b                                      ")
    print("                                                                   Y8b d88P              \    / ___  __   __     __           __        ___")
    print("                                                                    'Y88P'                \  / |__  |__) /__` | /  \ |\ |    /  \ |\ | |__ ")
    print("                                                                                           \/  |___ |  \ .__/ | \__/ | \|    \__/ | \| |___ ")
                
    print("\n __                                     __   __   __ ")
    print("|__) \ / .    |\/|  /\  |     /\  |__/ /  \ /__` /__` ")
    print("|__)  |  .    |  | /~~\ |___ /~~\ |  \ \__/ .__/ .__/ ")
    print("\n===========================================================================================================================================")
    
def main():
    os.environ["SPOTIPY_CLIENT_ID"] = "______________________________"
    os.environ["SPOTIPY_CLIENT_SECRET"] = "_____________________________"
    os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"
    
    scope = "user-read-currently-playing user-modify-playback-state"
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path="user.cache"))
    
    logo()
    
    startingArtist = str(input("\nInitiate your discovery by providing the name for your desired Starting Artist: \n (i.e., Sylvan LaCue, Jack Johnson)\n\n--> "))
    print("\n===========================================================================================================================================")
    topSongDepth = int(input("\nDefine how many songs from the Related Artist's top 10 should be added to the queue: \n (i.e., 3 [top 3 songs]) \n\n--> "))
    print("\n===========================================================================================================================================")
    countryCode = str(input("\nThe top 10 songs are determined by country. Define which country you would like to use: \n (use ISO 3166-1 alpha-2 country codes) \n  (i.e., US or GB or DE) \n\n--> ")).upper()
                                                
    results = sp.search(startingArtist, limit=1, offset=0, type='artist')
    artist_id = results['artists']['items'][0]['uri']
    related_artists = sp.artist_related_artists(artist_id)['artists']
    
    print("\n===========================================================================================================================================")
    selectionMode = str(input("\nWould you like to have a choice on which Related Artists to include? \n YES (Y) or NO (N)\n--> ")).upper()
    
    if selectionMode in ["Y","YES"]:
        print("\n===========================================================================================================================================")
        print("\nThese are your options for Related Artists: \n")
        a=1
        for name in related_artists:
            print("{index} -- {name}\n".format(index=a, name=name['name']))
            a += 1
    
        relatedArtist_lowbound = int(input("\nDefine the index of the first Related Artist that you would like to include: \n (Choose number from 1 to 19) \n\n--> "))
        relatedArtist_highbound = int(input("\nDefine the index of the last Related Artist you would like to include: \n (Must be a number higher than index of first Related Artist [max of 20]) \n\n--> "))
        
        for artist in range(relatedArtist_lowbound-1, relatedArtist_highbound):
            related_id = related_artists[artist]['uri']
            topTen = sp.artist_top_tracks(related_id, country=countryCode)['tracks']
            for song in range(0, topSongDepth):
                sp.add_to_queue(topTen[song]['uri'])
    else:
        relatedArtistAmount = int(input("\nDefine the number of Related Artists you would like to include: \n (Choose number from 1 to 20) \n\n--> "))
        
        for artist in range(0, relatedArtistAmount):
            related_id = related_artists[artist]['uri']
            topTen = sp.artist_top_tracks(related_id, country=countryCode)['tracks']
            for song in range(0, topSongDepth):
                sp.add_to_queue(topTen[song]['uri'])
    
if __name__ == "__main__":
    main()