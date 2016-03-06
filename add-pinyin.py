

from collections import defaultdict
import pysrt as ps
import sys

only_pinyin = False
if '--only-pinyin' in sys.argv:
    sys.argv.remove('--only-pinyin')
    only_pinyin = True

infile = sys.argv[1]

# Read Unihan data base

data_dir = '/home/martial/Documents/chinese/unihan'
f = data_dir + '/Unihan_Readings.txt'

lines = open(f).readlines()
lines[:] = [l for l in lines if not l.startswith('#')]
lines[:] = [l for l in lines if l.find('kMandarin') >= 0]

h = defaultdict()
codepoint = defaultdict()
for l in lines:
    w, _ , p = l.strip().split('\t', 2)
    key = chr(int(w[2:], 16))
    h[key] = p
    codepoint[key] = w

keys = list(h.keys())


# Add pinyin
lines = open(infile).readlines()
n = len(lines)
for i in range(n):
    pinyin_text = list(lines[i])
    for j in range(len(pinyin_text)):
        c = pinyin_text[j]
        if c in h:
            pinyin_text[j] = h[c]
    pinyin_text = ' '.join(pinyin_text)
    if only_pinyin:
        lines[i] = pinyin_text
    else:
        lines[i] += pinyin_text

print('\n'.join(lines))

