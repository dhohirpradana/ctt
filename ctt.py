import requests
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER + '\n[!] COOKIE KE TOKEN (FACEBOOK) [!]\n' + bcolors.ENDC)
cookie = input(bcolors.OKCYAN + '|---MASUKAN COOKIE : ' + bcolors.ENDC)
try:
    data = requests.get('https://business.facebook.com/business_locations', headers={
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
        'referer': 'https://www.facebook.com/',
        'host': 'business.facebook.com',
        'origin': 'https://business.facebook.com',
        'upgrade-insecure-requests': '1',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type': 'text/html; charset=utf-8'
    }, cookies={
        'cookie': cookie
    })

    print("|---Sedang Mengambil Token")
    find_token = re.search('(EAAG\w+)', data.text)
    with open('access_token.txt', 'w') as f:
        f.write(find_token.group(1))

    results = bcolors.FAIL + '   |---\n[x] Gagal: Cookie tidak valid !!' if (
        find_token is None) else '   |---\n[✓] ACCESS TOKEN => ' + bcolors.OKGREEN + find_token.group(1) + bcolors.ENDC
except requests.exceptions.ConnectionError:

    results = bcolors.FAIL + '   |---\n[x] Gagal : Tidak ada koneksi internet !!'
except:
    results = bcolors.FAIL + \
        '   |---\n[x] Gagal : Kesalahan tidak diketahui, coba kembali !!'

print(results)
