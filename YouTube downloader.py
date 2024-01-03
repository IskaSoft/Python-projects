import streamlit as st

from pathlib import Path
from youtube import Downloader

st.title('YouTube Downloader')

"""
Download videos or entire playlists from youtube.    
You can specify if you want only audio, the video or both 
in separated files.
"""

"""
What do you want to download?
"""

selection = st.selectbox("", ['Video', 'Playlist'])

link = st.text_input(f'Add the link of your {selection}')

"""
Choose download type
- Video: Normal youtube video
- Only Audio: Just the audio of the youtube video  
- Audio and Video: This option downloads the audio and the video
in separate files.

#### Note:  
- If you are downloading a playlist, these options apply to every link
- If the resolution is not available, it will download the highest
"""

download_type, resolution = st.beta_columns(2)

with download_type:
    download_selection = st.selectbox("Download Type", ['Video', 'Only Audio', 'Audio and Video'])

with resolution:
    quality = st.selectbox("Quality", ['highest', '720p', '480p', '320p', '240p', '144p'])

if st.button('Download'):
    if selection == 'Playlist':
        playlist = True
    else:
        playlist = False
    if download_selection == 'Video':
        video = True
        audio = False
    elif download_selection == 'Only Audio':
        video = False
        audio = True
    else:
        video = True
        audio = True

    info = st.empty()

    downloader = Downloader(link, video=video, audio=audio, playlist=playlist, quality=quality, convert=True)

    info.info('Downloading...')
    downloader.download()
    text = f"""
    The download was successful  
    Search for it at: {'./youtube_downloader/downloads/'}
    """
    info.success(text)