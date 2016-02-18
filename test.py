from json2html import Json2HTML


data = {
	'a': 'f',
    'b': 'c',
    'sfdsaf': [
	    'fdsf','23','fds','vcxz'
    ],
    'dict': {
	    '123': 'fds',
        'vcx': {
	        '123':'vcx',
            '321':'re',
        },
        '56': [1,2,3,4,5]
    }

}
j2h = Json2HTML()
j2h.set_conf(indent=8)
html = j2h.play(data)
print html
