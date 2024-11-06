import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="e5c7d1f314e8421ebf8b816205c97f79",
    client_secret="2650658be8544433b4621334a81450b6",
    redirect_uri="http://localhost:8888/callback",
    scope="user-top-read"))

results = sp.current_user_top_artists(limit=5, time_range='short_term')
