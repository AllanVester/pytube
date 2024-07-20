# pytube

![PyPI - Downloads](https://img.shields.io/pypi/dm/pytube)
![PyPI - License](https://img.shields.io/pypi/l/pytube)
![Read the Docs](https://img.shields.io/readthedocs/pytube)
![GitHub Tag](https://img.shields.io/github/v/tag/JuanBindez/pytube?include_prereleases)
<a href="https://pypi.org/project/pytube/"><img src="https://img.shields.io/pypi/v/pytube" /></a>


## Python3 library for downloading YouTube Videos.

----------
## install

    pip install pytube


## Quickstart

#### mp4 video download highest resolution:

```python

from pytube import YouTube
from pytube.cli import on_progress
 
url = "url"
 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
 
ys = yt.streams.get_highest_resolution()
ys.download()
```

#### If you want to save in .mp3 just pass the mp3=True parameter (MPEG-4 AAC audio codec):

```python

from pytube import YouTube
from pytube.cli import on_progress
 
url = "url"
 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
 
ys = yt.streams.get_audio_only()
ys.download(mp3=True) # pass the parameter mp3=True to save in .mp3
```

#### if you want to download complete playlists:

```python

from pytube import Playlist
from pytube.cli import on_progress
 
url = "url"

pl = Playlist(url)

for video in pl.videos:
    ys = video.streams.get_audio_only()
    ys.download(mp3=True) # pass the parameter mp3=True to save in .mp3

```

#### if you want to add authentication

```python

from pytube import YouTube
from pytube.cli import on_progress
 
url = "url"

yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress)
           
ys = yt.streams.get_audio_only()

ys.download(mp3=True) # you will only get the request to authenticate once you download

```

## Subtitle/Caption Tracks:

#### viewing available subtitles:

```python

from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
subtitles = yt.captions

print(subtitles)

```

#### printing the subtitle tracks:

```python

from pytube import YouTube
 

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

caption = yt.captions.get_by_language_code('en')
print(caption.generate_srt_captions())

```

#### now you can save subtitles to a txt file:

```python

from pytube import YouTube
 

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

caption = yt.captions.get_by_language_code('en')
caption.save_captions("captions.txt")

```

## Using Channels:

#### get the channel name:

```python

from pytube import Channel

c = Channel("https://www.youtube.com/@ProgrammingKnowledge/featured")

print(f'Channel name: {c.channel_name}')

```

#### to download all videos from a channel:


```python

from pytube import Channel

c = Channel("https://www.youtube.com/@ProgrammingKnowledge")

print(f'Downloading videos by: {c.channel_name}')

for video in c.videos:
    download = video.streams.get_highest_resolution().download()

```

