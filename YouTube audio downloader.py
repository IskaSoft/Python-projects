import pafy
#pip install pafy
url = input("Enter Youtube Url : ")
video = pafy.new(url)
audios = video.getbestaudio()
audios.download()