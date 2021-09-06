import urllib.request

# url = 'https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg'
url = input("IMG to Download here->  ")
file_name = input("Which is the file name? ")


def downloadIMG(url, file_name):
    fullPath =  file_name + '.jpg'
    urllib.request.urlretrieve(url, fullPath)


downloadIMG(url, file_name)
