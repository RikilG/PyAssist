import traceback
import pytube

def download(query) :

	download_destination = "E:\\Downloads\\ChromeDownloads"

	combined = '\t'.join(query)
	if 'youtube' in combined or 'youtu.be' in combined:
		try:
			link = query[1]
			yt = pytube.YouTube(link)
			videos = yt.get_videos()
			s=1
			for v in videos :
				print(str(s) + ". " + str(v))
				s+=1
			print("Enter your choice : ", end='')
			n = int(input())
			vid = videos[n-1]
			print("Please Wait for download to complete...")
			vid.download(download_destination)
			print(yt.filename + "\nHas been successfully downloaded to\n" + download_destination)
		except Exception as e:
			# traceback.print_exc()
			print(e)