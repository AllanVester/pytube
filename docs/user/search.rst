.. _search:

Using the Search Feature
========================

pytube includes functionality to search YouTube and return results almost
identical to those you would find using the search bar on YouTube's website.
The integration into pytube means that we can directly provide you with
YouTube objects that can be inspected and dowloaded, instead of needing to do
additional processing.

Using the Search object is really easy::

    >>> from pytube import Search
    >>> s = Search('YouTube Rewind')
    >>> len(s.results)
    17
    >>> s.results
    [\
        <pytube.__main__.YouTube object: videoId=YbJOTdZBX1g>, \
        <pytube.__main__.YouTube object: videoId=PKtnafFtfEo>, \
        ...\
    ]
    >>> 

Due to the potential for an endless stream of results, and in order to prevent
a user from accidentally entering an infinite loop of requesting additional
results, the ``.results`` attribute will only ever request the first set of
search results. Additional results can be explicitly requested by using the
``.get_next_results()`` method, which will append any additional results to
the ``.results`` attribute::

    >>> s.get_next_results()
    >>> len(s.results)
    34
    >>> 

Additional functionality
========================

In addition to the basic search functionality which returns YouTube objects,
searches also have associated autocomplete suggestions. These can be accessed
as follows::

    >>> s.completion_suggestions
    [\
        'can this video get 1 million dislikes', \
        'youtube rewind 2020 musical', \
        ...\
    ]


The .videos method will only return the videos::

    s = Search('YouTube Rewind')

    print(s.videos)


Output::

    [<pytube.__main__.YouTube object: videoId=_GuOjXYl5ew>, <pytube.__main__.YouTube object: videoId=FlsCjmMhFmw>, <pytube.__main__.YouTube object: videoId=KK9bwTlAvgo>, <pytube.__main__.YouTube object: videoId=YbJOTdZBX1g>, <pytube.__main__.YouTube object: videoId=H7jtC8vjXw8>, <pytube.__main__.YouTube object: videoId=iCkYw3cRwLo>, <pytube.__main__.YouTube object: videoId=zKx2B8WCQuw>, <pytube.__main__.YouTube object: videoId=2lAe1cqCOXo>, <pytube.__main__.YouTube object: videoId=By_Cn5ixYLg>, <pytube.__main__.YouTube object: videoId=Q5vQawTFJ0I>, <pytube.__main__.YouTube object: videoId=DpOCWIvpoE8>, <pytube.__main__.YouTube object: videoId=TjkRhh3Gh1U>, <pytube.__main__.YouTube object: videoId=PKtnafFtfEo>, <pytube.__main__.YouTube object: videoId=s7LNSuJHVww>, <pytube.__main__.YouTube object: videoId=diT6jc9flkc>, <pytube.__main__.YouTube object: videoId=SmnkYyHQqNs>, <pytube.__main__.YouTube object: videoId=glc2_--ZWoY>]


The .shorts method will only return the shorts.::

Here it is interesting to note that videos and shorts are from the same class of objects::

    s = Search('YouTube Rewind')

    print(s.shorts)


Output::

    [<pytube.__main__.YouTube object: videoId=cu7g_MB8uF4>, <pytube.__main__.YouTube object: videoId=sLbrJ9qWHwM>, <pytube.__main__.YouTube object: videoId=hNsFChiug28>, <pytube.__main__.YouTube object: videoId=6Qs1k7DKyfE>, <pytube.__main__.YouTube object: videoId=_6N44bZRJKE>, <pytube.__main__.YouTube object: videoId=rownH_IdP28>, <pytube.__main__.YouTube object: videoId=McIHLyoc2zk>, <pytube.__main__.YouTube object: videoId=8LEJmOzCfas>, <pytube.__main__.YouTube object: videoId=nbO3_bxYHx4>, <pytube.__main__.YouTube object: videoId=aFOmxMKsFwo>, <pytube.__main__.YouTube object: videoId=j28LZp08GIQ>, <pytube.__main__.YouTube object: videoId=u5HFzlkQ6hU>, <pytube.__main__.YouTube object: videoId=GNRe864aQq4>, <pytube.__main__.YouTube object: videoId=egdkRjY8OsE>, <pytube.__main__.YouTube object: videoId=luM--KkUwCc>, <pytube.__main__.YouTube object: videoId=HEc18y-QQYM>, <pytube.__main__.YouTube object: videoId=W4ET-jP6yd4>, <pytube.__main__.YouTube object: videoId=lxF5sF9hHPI>, <pytube.__main__.YouTube object: videoId=T50I0hqULkA>, <pytube.__main__.YouTube object: videoId=FXezutlwJog>, <pytube.__main__.YouTube object: videoId=rownH_IdP28>, <pytube.__main__.YouTube object: videoId=McIHLyoc2zk>, <pytube.__main__.YouTube object: videoId=8LEJmOzCfas>, <pytube.__main__.YouTube object: videoId=nbO3_bxYHx4>, <pytube.__main__.YouTube object: videoId=aFOmxMKsFwo>, <pytube.__main__.YouTube object: videoId=j28LZp08GIQ>, <pytube.__main__.YouTube object: videoId=u5HFzlkQ6hU>, <pytube.__main__.YouTube object: videoId=GNRe864aQq4>, <pytube.__main__.YouTube object: videoId=egdkRjY8OsE>, <pytube.__main__.YouTube object: videoId=luM--KkUwCc>]


The .playlist method will only return playlists::

	s = Search('python tutorial')

	print(s.playlist)


Output::

    [<pytube.contrib.Playlist object: playlistId=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3>, <pytube.contrib.Playlist object: playlistId=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU>, <pytube.contrib.Playlist object: playlistId=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB>, <pytube.contrib.Playlist object: playlistId=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0>]


The .channel method will return only the channels::

    s = Search('python channel')

    print(s.channel)


Output::

    [<pytube.contrib.Channel object: channelUri=/channel/UCI0vQvr9aFn27yR6Ej6n5UA>, <pytube.contrib.Channel object: channelUri=/channel/UCdu8D9NV9NP1iVPTYlenORw>, <pytube.contrib.Channel object: channelUri=/channel/UCqC1iSQnRIDz_rOy8LHe69g>, <pytube.contrib.Channel object: channelUri=/channel/UCKQdc0-Targ4nDIAUrlfKiA>, <pytube.contrib.Channel object: channelUri=/channel/UC3Qe9c8dZqnjwcDD2vCZBKQ>, <pytube.contrib.Channel object: channelUri=/channel/UC68KSmHePPePCjW4v57VPQg>, <pytube.contrib.Channel object: channelUri=/channel/UCGDlapuq4c7611vw44yfcNQ>, <pytube.contrib.Channel object: channelUri=/channel/UCripRddD4BnaMcU833ExuwA>, <pytube.contrib.Channel object: channelUri=/channel/UC8butISFwT-Wl7EV0hUK0BQ>, <pytube.contrib.Channel object: channelUri=/channel/UCTVGjydBHM2g5_K18MZqE4Q>]
