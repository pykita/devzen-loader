import requests

def load():
    links = ["devzen-0147-2017-06-17-491b2be99c611757.mp3", "devzen-0147a-2017-06-17-7a87ce025cf5d677.mp3", "devzen-0148-2017-07-01-abad3d963dc338e3.mp3", "devzen-0149-2017-07-08-d69bf011d7bd6e72.mp3", "devzen-0150-2017-07-15-2e93827d7eb6ed4f.mp3", "devzen-0151-2017-07-22-7e12a87a42c6e14d.mp3", "devzen-0152-2017-07-29-19a40b73153cc917.mp3", "devzen-0153-2017-08-05-fade5dc9d6a9a101.mp3", "devzen-0154-2017-08-12-b7a55f94a274e757.mp3", "devzen-0155-2017-08-19-2b89b2fbbaed80a7.mp3", "devzen-0156-2017-08-26-f50c7febeb58a9c8.mp3", "devzen-0157-2017-09-02-914f79d69211d04e.mp3", "devzen-0157a-2017-09-02-9e8edf766fc4c641.mp3", "devzen-0158-2017-09-09-0bb3ca442d04d02d.mp3", "devzen-0159-2017-09-16-7296e82218b2708c.mp3", "devzen-0160-2017-09-23-661374257668bf68.mp3", "devzen-0161-2017-09-30-872cd3112d0b3f88.mp3", "devzen-0162-2017-10-07-a2a62f95ae4967d2.mp3", "devzen-0163-2017-10-14-021697319667b71d.mp3", "devzen-0164-2017-10-21-46c7662af4258314.mp3", "devzen-0165-2017-10-28-c1a0c74db249f195.mp3", "devzen-0166-2017-11-04-f47d0e0651914130.mp3", "devzen-0167-2017-11-11-d6e9356b984a925c.mp3", "devzen-0168-2017-11-18-a9114c596b7c138d.mp3"]
    links_2017 = ["devzen-0154-2017-08-12-b7a55f94a274e757.mp3", "devzen-0155-2017-08-19-2b89b2fbbaed80a7.mp3", "devzen-0156-2017-08-26-f50c7febeb58a9c8.mp3", "devzen-0157-2017-09-02-914f79d69211d04e.mp3", "devzen-0157a-2017-09-02-9e8edf766fc4c641.mp3", "devzen-0158-2017-09-09-0bb3ca442d04d02d.mp3", "devzen-0159-2017-09-16-7296e82218b2708c.mp3", "devzen-0160-2017-09-23-661374257668bf68.mp3", "devzen-0161-2017-09-30-872cd3112d0b3f88.mp3", "devzen-0162-2017-10-07-a2a62f95ae4967d2.mp3", "devzen-0163-2017-10-14-021697319667b71d.mp3", "devzen-0164-2017-10-21-46c7662af4258314.mp3", "devzen-0165-2017-10-28-c1a0c74db249f195.mp3", "devzen-0166-2017-11-04-f47d0e0651914130.mp3", "devzen-0167-2017-11-11-d6e9356b984a925c.mp3", "devzen-0168-2017-11-18-a9114c596b7c138d.mp3", "devzen-0169-2017-11-25-cc13b2e9cc365ea7.mp3", "devzen-0170-2017-12-02-2306494c72d3d466.mp3", "devzen-0171-2017-12-09-35066c0948f7828e.mp3", "devzen-0172-2017-12-16-e51c890b66746ba5.mp3", "devzen-0173-2017-12-23-a941c9d437ab9861.mp3"]
    links_2018 = ["devzen-0174-2018-01-13-e5ccf00cead536b5.mp3", "devzen-0175-2018-01-20-db7f1fd0ebb7ac58.mp3", "devzen-0176-2018-01-27-d34f695225e2ea93.mp3", "devzen-0177-2018-02-03-ec2bb30df8e2eeb5.mp3", "devzen-0178-2018-02-10-4953247617d029b5.mp3", "devzen-0179-2018-02-17-2c097a73aee2c6cf.mp3", "devzen-0180-2018-02-24-06a3cc098c7271ed.mp3", "devzen-0181-2018-03-03-450bbf951fc01e2a.mp3", "devzen-0182-2018-03-10-c8f57230f8ed8d43.mp3", "devzen-0183-2018-03-17-18648d2dada4387c.mp3", "devzen-0184-2018-03-24-582c1f50c23791c7.mp3", "devzen-0185-2018-03-31-113aeeb3c9e3dfba.mp3", "devzen-0186-2018-04-07-78312c563f6a8b0b.mp3", "devzen-0187-2018-04-14-50cf539e5ccd3a56.mp3"]

    for link in links_2018:
        response = requests.get('https://download.devzen.ru/2018/%s' % link, verify=False)
        with open((link),'wb') as output:
            output.write(response.content)
            print('file %s is downloaded' % link)

    # for link in links_2018:
    #     mp3file = http.request('GET','https://download.devzen.ru/2018/%s' % link)
    #     with open((link),'wb') as output:
    #         output.write(mp3file.data)

if __name__ == '__main__':
    load()