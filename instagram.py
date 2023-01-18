import requests
import json

link = "https://www.instagram.com/reel/CmcLWqkKALH/"
def it(link):
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

	querystring = {"url": link}

	headers = {
		"X-RapidAPI-Key": "67245c9693msh1f099e00a255af6p15aa40jsn668796498800", #go to rapidapi.com to get Api
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.text
	rest = json.loads(result)
	return {'smth': rest['media']}

#print(it(link))