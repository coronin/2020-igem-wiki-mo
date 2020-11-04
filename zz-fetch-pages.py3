import bs4
from os import system, walk

baseURL = 'https://2020.igem.org/wiki/index.php?action=edit&title=Team:Fudan'


def fetch_create(filename):
    pageHead = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <script src="/jquery-1.11.1.min.js"></script>
  <link rel="stylesheet" href="/0igem.css">
  <title>%s</title>
</head>
<body class="mediawiki ltr sitedir-ltr ns-0 ns-subject page-Team_Fudan_%s skin-igem action-view">
<div class="igem_content_wrapper">
<div class="igem_column_wrapper">
<!--
                      仅仅复制20行之后的内容，并注意去掉22行末的 右向文本尖头 的三个字符
                      ////////////





''' % ( filename, filename )
    system('curl "%s/%s" -o %s.txt' % (baseURL, filename,filename) )
    f = open('%s.txt' % filename, 'r+')
    page = f.read()
    soup = bs4.BeautifulSoup(page, 'lxml')
    C = soup.find(id="wpTextbox1")
    #print(C.contents[0])
    f.seek(0,0)
    f.write( pageHead )
    f.write( C.contents[0] )
    f.truncate()
    f.close()
    print('%s.txt created' % filename)


ff = []
for (dirpath, dirnames, filenames) in walk('./'):
    ff.extend(filenames)
    break
fff = []
for f in ff:
    if f != 'index.html' and f.endswith('.html'):
        print(f)
        fetch_create( f[:-5] )
