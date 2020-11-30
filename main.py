def parse_cookie(cookie: str) -> dict:
    d = {}
    if len(cookie) == 0: return {}
    cookie = cookie.split(';')
    for i in range(len(cookie)):
        if cookie[i] == '':
            continue
        for j in range(len(cookie[i])):
            if cookie[i].count('=')==0:
                d[cookie[i]] = ''
                continue
            if cookie[i].split('=', 1)[0] == '':
                continue
            d[cookie[i].split('=', 1)[0]] = cookie[i].split('=',1)[1]
    return d




if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('name;') == {'name': ''}
    assert parse_cookie('name=Dima;lastname;') == {'name': 'Dima', 'lastname': ''}
    assert parse_cookie(';') == {}
    assert parse_cookie('name=Dima;;') == {'name': 'Dima'}
    assert parse_cookie('=') == {}
    assert parse_cookie('=;') == {}
    assert parse_cookie('mail=i.ua;=;') == {'mail': 'i.ua'}
    assert parse_cookie('mail==') == {'mail': '='}
    assert parse_cookie('name=Dima;mail=') == {'name': 'Dima', 'mail': ''}
    assert parse_cookie('?n') == {'?n': ''}

