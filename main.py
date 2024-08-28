from pytube import YouTube
# Ask for youtube link
link = input("Paste youtube link you want to download")
yt = YouTube(link)
# show details
print("Title", yt.title)
print("Number of views: ", yt.views)
print("Length of video:", yt.length)
print("Raiting of of video:", yt.rating)
ys = yt.streams.get_highest_resolution()
if ys:
  print("start downloading")
  ys.download()
  print("download complete")
else:
  print("No suitable stream found.")