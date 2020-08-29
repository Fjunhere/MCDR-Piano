import os, time


def log(server, msg, player=None):
	if player == None:
		server.say(msg)
	else:
		server.execute(f'tell {player} {msg}')
	
def create_path(path_name):
	if os.path.exists(path_name):
		break
	else:
		os.mkdir(path_name)
		
def read_file(file_name):
	file_path = path_name + file_name
	with open(file_name, 'r') as f:
		music = f.read()
		for i in music.split(' '):
			j = i.split(',')
			if len(j) == 3:
				tone = int(j[0])
				sec = float(j[1])
				block_type = int(j[2])
			elif len(j) == 2:
				tone = int(j[0])
				sec = float(j[1])
				block_type = 0
			else:
				log(f'[MCDR-Piano] 乐谱内参数错误，具体音符为：{i}' )
				