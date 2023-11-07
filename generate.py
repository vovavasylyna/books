#!/usr/bin/env python3

header = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" /><link rel="stylesheet" href="main.css?4" /><title>Books</title></head><body>'
header += '<header>'
header += '<a href="https://vasylyna.net">Volodymyr Vasylyna`s website</a>'
header += '<h2><a href="index.html">Books</a></h2>'
header += '</header>'
header += '<nav>'
header += '<a href="2023.html">2023</a> | <a href="2022.html">2022</a> | <a href="2021.html">2021</a> | <a href="2020.html">2020</a> | <a href="2017.html">2017</a> | <a href="2016.html">2016</a> | <a href="2015.html">2015</a> | <a href="2014.html">2014</a> | <a href="2013.html">2013</a> | <a href="2012.html">2012</a> | <a href="2011.html">2011</a> | <a href="2010.html">2010</a><br><br>'
header += '</nav><section>'
header += '<header class="site-header">'
footer = '</section></body></html>'

index = header

with open('current.txt') as f:
    current = [x.strip().split(' | ') for x in f.readlines()]
    f.close()

index += '<h2>Currently Reading</h2>'

index += '<ul>'
for b in current:
    index += '<li>' + b[0] + ' <em>– ' + b[1] + '</em></li>'
index += '</ul>'

index += '<p>'
index += 'Source code:<br><a href="https://github.com/vovavasylyna/books" target="_blank">https://github.com/vovavasylyna/books</a><br><br>'
index += '</p>'

index += footer

indexFile = open('index.html', "w+")
indexFile.write(index)
indexFile.close()

for yr in ["2023","2022","2021","2020","2017","2016","2015","2014","2013","2012","2011","2010",]:
    year = header

    with open('read-'+yr+'.txt') as f:
        y = [x.strip().split(' | ') for x in f.readlines()]
        f.close()

    year += '<h2>'+yr+'</h2>'

    if len(y) == 0:
        year += '<p><em>TBD</em></p>'

    for b in y:
        year += '<li>' + b[0] + ' <em>– ' + b[1] + '</em></li>'

    year += footer

    yearFile = open(yr+'.html', "w+")
    yearFile.write(year)
    yearFile.close()