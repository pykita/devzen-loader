import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing

cpus = multiprocessing.cpu_count() - 1

def get_and_save(link):
    response = requests.get('https://download.devzen.ru/2018/%s' % link, verify=False)
    with open((link),'wb') as output:
        output.write(response.content)
        return link

def load():
    # $('#content-wrapper pre a').map(function(i, v){ return $(v).attr('href')})
    links = ["devzen-0188-2018-04-21-5bf6a2934b8ab45e.mp3", "devzen-0189-2018-04-28-d7efaeb6f9abbfd0.mp3", "devzen-0190-2018-05-05-b4ff2496e4b1a766.mp3", "devzen-0191-2018-05-12-a46f6402e65bdd12.mp3", "devzen-0192-2018-05-19-71d1d9daa8cd0446.mp3", "devzen-0193-2018-05-27-7147dd8cc85ec45c.mp3", "devzen-0194-2018-06-02-6ece914292243045.mp3", "devzen-0195-2018-06-09-0dac994ee23e6d9a.mp3", "devzen-0196-2018-06-16-dc771a9fe11dbe4a.mp3", "devzen-0197-2018-06-23-b4d3dbac5c57e076.mp3", "devzen-0198-2018-06-30-8868bce1814b9ae8.mp3", "devzen-0199-2018-07-07-149fb0c6907fe150.mp3", "devzen-0200-2018-07-14-30c65811aa487d2a.mp3", "devzen-0201-2018-07-21-d7f4fb42937ad278.mp3", "devzen-0202-2018-07-28-fc13568195f0ba37.mp3", "devzen-0203-2018-08-04-7f9cca49c6967bb1.mp3", "devzen-0204-2018-08-11-a5f3dd087cbddd06.mp3", "devzen-0205-2018-08-18-18c01b1e1cc7bd54.mp3", "devzen-0206-2018-08-26-f9c8980c0e100538.mp3", "devzen-0207-2018-09-01-6f2733d57e773e7d.mp3", "devzen-0208-2018-09-08-61969ea5b5402c4b.mp3", "devzen-0209-2018-09-16-c4f4af2ff074876a.mp3", "devzen-0210-2018-09-22-0ec531a14bcd5aa5.mp3", "devzen-0211-2018-09-29-fbc395bde1c1a91b.mp3", "devzen-0212-2018-10-06-cda619f44b00481e.mp3", "devzen-0213-2018-10-13-f9e57fef40ce0586.mp3"]

    with ThreadPoolExecutor(max_workers=cpus) as executor:
        futures = [executor.submit(get_and_save, link) for link in links]
        for future in as_completed(futures):
            try:
                key = future.result()
            except Exception as exc:
                print('generated an exception: %s' % exc)
            else:
                print('Key %s is done.' % key)

if __name__ == '__main__':
    load()