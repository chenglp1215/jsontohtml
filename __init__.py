__author__ = 'chenglp'



class Json2HTML(object):
	key_value_conf = {}
	type_config = {}
	depth = 0
	html_data = ""
	color_config = {
		'{' : 'color: #ff0000',
	    '[' : 'color: #ff0000',
	    ':' : 'color: #ff00ff',
	    'key': 'color: #0000ff',
	    'value': 'color: #000088',
	}
	indent = 4

	def __init__(self):
		pass

	def set_conf(self, type_config=None, indent=4, color_config=None, **kwargs):
		self.indent = indent
		if type_config:
			self.type_config.update(type_config)
		if color_config:
			self.color_config.update(color_config)


	def __add_indent(self):
		self.html_data += '%s' % '&nbsp;' * self.indent*self.depth

	def __dict_start(self):
		self.__add_indent()
		self.html_data += "<span style='%s'>{</span></br>" % self.color_config['{']
		self.depth += 1
	def __dict_end(self):
		self.depth -= 1
		self.__add_indent()
		self.html_data += "<span style='%s'>}</span>,</br>" % self.color_config['{']
	def __list_start(self):
		self.__add_indent()
		self.html_data += "<span style='%s'>[</span></br>" % self.color_config['[']
		self.depth += 1
	def __list_end(self):
		self.depth -= 1
		self.__add_indent()
		self.html_data += "<span style='%s'>]</span>,</br>" % self.color_config['[']
	def __add_key(self, key):
		self.__add_indent()
		self.html_data += "<span style='%s'>%s</span>:" % (self.color_config['key'], self.add_type_tip(key))

	def add_type_tip(self, value):
		if isinstance(value, str):
			return '"%s"' % value
		if isinstance(value, bool):
			return "1" if value else 0
		return value



	def __add_value(self, value):
		self.html_data += "&nbsp;"
		self.html_data += "<span style='%s'>%s</span>,</br>" % (self.color_config['value'], self.add_type_tip(value))
	def __add_list_item(self, value):
		self.__add_indent()
		self.html_data += "<span style='%s'>%s</span>,</br>" % (self.color_config['value'], self.add_type_tip(value))

	def __play_list(self, data):
		self.__list_start()
		for each in data:
			if isinstance(each, dict):
				self.html_data += '</br>'
				self.__play_dict(each)
			elif isinstance(each, list):
				self.html_data += '</br>'
				self.__play_list(each)
			else:
				self.__add_list_item(each)
		self.__list_end()

	def __play_dict(self, data):
		self.__dict_start()
		for each in data.keys():
			self.__add_key(each)
			if isinstance(data[each], dict):
				self.html_data += '</br>'
				self.__play_dict(data[each])
			elif isinstance(data[each], list):
				self.html_data += '</br>'
				self.__play_list(data[each])
			else:
				self.__add_value(data[each])
		self.__dict_end()

	def play(self, data):
		self.html_data = ""
		if isinstance(data, dict):
			self.__play_dict(data)
		if isinstance(data, list):
			self.__play_list(data)

		return self.html_data



