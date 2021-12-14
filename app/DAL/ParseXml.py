import requests
import xml.etree.ElementTree as ET

def get_xml(url_file):
    """ Fonction qui prend une URL vers un XML et renvoie son contenu
    """
    xml = requests.get(url_file)
    #transforme du xml sous forme de texte en structure exploitable
    element = ET.fromstring(xml.text)
    playlists = element.find('Blobs').findall('Blob')
    return playlists

def get_url(playlists):
    """ Cette fonction prend et renvoie une liste
        avec deux éléments;
        le premier pour les top_50
        le second pour les caractéristiques des chansons (songs)
    """
    list_top_50 = list()
    lists_songs = list()
    for url in playlists:
        if 'top_50' in url.find('Url').text:
            list_top_50.append(url.find('Url').text)
        
        if 'songs' in url.find('Url').text:
            lists_songs.append(url.find('Url').text)
    return list_top_50, lists_songs

if __name__ == '__main__':
    data = get_url(get_xml("https://dlsandboxweu002.blob.core.windows.net/spotify?comp=list"))
    print(len(data))
    print(len(data[0]))
    print(len(data[1]))