#!/usr/bin/env python
import simplejson as json
import requests
import subprocess
from gallery import OverlayGallery

URL_ROOT = 'http://localhost:18888'

req = requests.get(URL_ROOT + '/api/overview')


overview = json.loads(req.text)

for x in overview['SUMMARY']:
    if x['key'] == 'TOTAL_IMAGES':
        N = x['value']

print N
gal = OverlayGallery('out')

for i in range(N):
    path1, path2 = gal.next()
    subprocess.check_call('wget "%s/api/image?max_size=3000&id=%d&channels=3&perturb=0&norm=0&annotate=json&anno_palette=default" -O %s' % (URL_ROOT, i, path1), shell=True)
    subprocess.check_call('wget "%s/api/image?max_size=3000&id=%d&channels=3&perturb=0&norm=0&anno_palette=default" -O %s' % (URL_ROOT, i,  path2), shell=True)

gal.flush()
