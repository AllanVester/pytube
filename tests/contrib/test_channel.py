from unittest import mock

from pytube import Channel


@mock.patch('pytube.request.get')
def test_init_with_url(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html
    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.channel_url == 'https://www.youtube.com/c/ProgrammingKnowledge'
    assert c.videos_url == f'{c.channel_url}/videos'
    assert c.playlists_url == f'{c.channel_url}/playlists'
    assert c.community_url == f'{c.channel_url}/community'
    assert c.featured_channels_url == f'{c.channel_url}/channels'
    assert c.about_url == f'{c.channel_url}/about'


@mock.patch('pytube.request.get')
def test_channel_uri(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.channel_uri == '/c/ProgrammingKnowledge'

    c = Channel('https://www.youtube.com/channel/UCs6nmQViDpUw0nuIx9c_WvA/videos')
    assert c.channel_uri == '/channel/UCs6nmQViDpUw0nuIx9c_WvA'


@mock.patch('pytube.request.get')
def test_channel_name(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.channel_name == 'ProgrammingKnowledge'


@mock.patch('pytube.request.get')
def test_channel_id(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.channel_id == 'UCs6nmQViDpUw0nuIx9c_WvA'


@mock.patch('pytube.request.get')
def test_channel_vanity_url(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.vanity_url == 'http://www.youtube.com/@ProgrammingKnowledge'


@mock.patch('pytube.request.get')
def test_channel_video_list(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    first_ten = ('[<pytube.__main__.YouTube object: videoId=jZGxjmKOH0c>, '
                 '<pytube.__main__.YouTube object: videoId=sZFH6sEbt9E>, '
                 '<pytube.__main__.YouTube object: videoId=WUDivf0NEso>, '
                 '<pytube.__main__.YouTube object: videoId=YbVHEKwlAOY>, '
                 '<pytube.__main__.YouTube object: videoId=ChwsFldra-o>, '
                 '<pytube.__main__.YouTube object: videoId=iECqUHiR5ao>, '
                 '<pytube.__main__.YouTube object: videoId=-9P4CxRWL8c>, '
                 '<pytube.__main__.YouTube object: videoId=vVrIDJ--GOA>, '
                 '<pytube.__main__.YouTube object: videoId=uXP9KatdbBs>, '
                 '<pytube.__main__.YouTube object: videoId=n6fcDbOr7Rg>]')
    assert str(c.videos[:10]) == first_ten


@mock.patch('pytube.request.get')
def test_videos_html(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge')
    assert c.html == channel_videos_html

# Because the Channel object subclasses the Playlist object, most of the tests
# are already taken care of by the Playlist test suite.
