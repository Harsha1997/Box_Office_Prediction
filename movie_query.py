from youtube_videos import youtube_search
from youtube_videos import geo_query
import httplib2

test = youtube_search("< movie name > trailer")
newlis=test[1]
newdic=dict(newlis[0])
dic2=dict(newdic['id'])
id=str(dic2['videoId'])
print(id)

link='https://www.youtube.com/watch?v='
link=link+id
print(link)

dic3=dict(geo_query(id))

list2=[dic3['items']]


dictfinal=dict(list2[0][0]['statistics'])

views=dictfinal['viewCount']
likes=dictfinal['likeCount']
dislikes=dictfinal['dislikeCount']
comments=dictfinal['commentCount']

print('views:: ',views)
print('likes:: ',likes)
print('dislikes:: ',dislikes)
print('comments:: ',comments)
