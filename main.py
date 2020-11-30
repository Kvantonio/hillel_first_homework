def parse(url: str) -> dict:
    d = {}
    if len(url) == 0: return {}
    if url.count('?') == 0: return {}
    if url.split('?', 1)[1] == '': return {}
    url = url.split('?')[1].split('&')
    for i in range(len(url)):
        if url[i] == '': continue
        if url[i].count('=') == 0:
            d[url[i].split('=', 1)[0]] = ""
            continue
        d[url[i].split('=', 1)[0]] = url[i].split('=', 1)[1]
    return d


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('') == {}
    assert parse('?') == {}
    assert parse('&') == {}
    assert parse('https://www.youtube.com/watch?v')
    assert parse('https://www.youtube.com/watch?v=fgf&g&user=ghhfv') == {'v': 'fgf', 'g': '', 'user': 'ghhfv'}
    assert parse('https://www.youtube.com/watch?v=1PHGmatiaME') == {'v': '1PHGmatiaME'}
    assert parse('https://www.youtube.com/?v=1P&&user=ff') == {'v': '1P', 'user': 'ff'}
    assert parse('https://www.youtube.com/watch?v=1PHGmatiaME=26s') == {'v': '1PHGmatiaME=26s'}
    assert parse('https://www.youtube.com/watch?v=1PHGmatiaME=26s&n=h=j') == {'v': '1PHGmatiaME=26s', 'n':'h=j'}
    assert parse('https://stepik.org/lesson/3380/step/2?unit=963') == {'unit': '963'}
    assert parse('https://www.google.com/search?client=opera-gx&q=anaconda+import+requests&sourceid=opera') == {'client': 'opera-gx', 'q': 'anaconda+import+requests', 'sourceid': 'opera'}

