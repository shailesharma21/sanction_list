import requests
def data_scrap(url):
	filename = url.split('/')[-1]
	print(filename)
	sl = requests.get(url, stream=True)
	f = open(filename,'wb')
	for chunk in sl.iter_content(chunk_size=1024):
		if chunk:
			f.write(chunk)
	f.close()
	return

data_scrap('https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1059386/UK_Sanctions_List.ods')
