#!/usr/bin/env python3

import psutil, getopt, sys

def Usage():
	print("\nVynae - Linux flavored\n")
	print ("Usage: "+sys.argv[0]+" <param> [option]")
	print("\t-h, --help\n\t\tDisplays this menu\n\t-n, --name\n\t\tsearch processes by name\n\t-p, -processID\n\t\tsearch processes by pid\n\t-c, --connection\n\t\taccepts 'NetOnly', 'NetSupress', and 'IP=x.x.x.x'\n\t-m, --parentID\n\t\tsearch by parentID\n\t-t, --terminal\n\t\tsearch by terminal '/dev/pts/1'\n\t-u, --user\n\t\tsearch by user\n")

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hn:p:c:m:t:u:", ["help","name=","processID=","connection=","parentID=","terminal=","user="])
	except:
		print(err)
		usage()
		sys.exit(2)
	output = None
	verbose = False
	for o, a in opts:
		if o in ('-h', '--help'):
			Usage()
			sys.exit(2)
		elif o in ('-n', '--name'):
			global name
			name = a
		elif o in ('-p', '--processID'):
			global pid
			pid = int(a)
		elif o in ('-c', '--connection'):
			global c
			connection = a
		elif o in ('-m', '--parentID'):
			global ppid
			ppid = int(a)
		elif o in ('-t', '--terminal'):
			global terminal
			terminal = a
		elif o in ('-u', '--user'):
			global user
			user = a
	processinfo()

def processinfo():	
	global name, pid, connection, ppid, terminal, user
	# default function

	# Excepting on name if it isn't used. Can't run other params. Might need to wrap each in
	try:
		if name:
			for proc in psutil.process_iter():			
				if proc.name() == name:
					for conn in psutil.net_connections(kind='all'):
						proc_conn = None
						try:
							if conn.pid == proc.pid and conn.status != 'NONE':
								proc_conn = conn
						except:
							pass
					procInfo = psutil.Process(pid=proc.pid)
					if proc_conn != None:
						print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username(), '\nNetwork Connections:\n', '\tLocal Address: ',proc_conn.laddr, '\n\tRemote Address:', proc_conn.raddr)
						print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
					else:
						print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username())
						print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
			sys.exit(0)
	except:
		pass
	try:
		if pid:
			proc = psutil.Process(pid=pid)
			for conn in psutil.net_connections(kind='all'):
				proc_conn = None
				try:
					if conn.pid == proc.pid and conn.status != 'NONE':
						proc_conn = conn
				except:
					pass
			procInfo = psutil.Process(pid=proc.pid)
			if proc_conn != None:
				print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username(), '\nNetwork Connections:\n', '\tLocal Address: ',proc_conn.laddr, '\n\tRemote Address:', proc_conn.raddr)
				print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
			else:
				print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username())
				print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
			sys.exit(0)
	except:
		pass
	try:
		if ppid:
			proc_conn = None
			proc = psutil.Process(pid=ppid)
			for child in proc.children():
				for conn in psutil.net_connections(kind='all'):
					try:
						if conn.pid == child.pid and conn.status != 'NONE':
							proc_conn = conn
					except:
						pass
				procInfo = psutil.Process(pid=child.pid)
				childproc = psutil.Process(pid=child.pid)
				if proc_conn != None:
					print('Name:',childproc.name(),'\nPID:', childproc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',childproc.username(), '\nNetwork Connections:\n', '\tLocal Address: ',proc_conn.laddr, '\n\tRemote Address:', proc_conn.raddr)
					print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
				else:
					print('Name:',childproc.name(),'\nPID:', childproc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username())
					print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
			sys.exit(0)
	except:
		pass
	try:
		if terminal:
			for proc in psutil.process_iter():
				if psutil.Process(pid=proc.pid).terminal() != terminal:
					pass
				else:
					proc_conn = None
					for conn in psutil.net_connections(kind='all'):
						try:
							if conn.pid == proc.pid and conn.status != 'NONE':
								proc_conn = conn
						except:
							pass
					procInfo = psutil.Process(pid=proc.pid)
					if proc_conn != None:
						print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username(), '\nNetwork Connections:\n', '\tLocal Address: ',proc_conn.laddr, '\n\tRemote Address:', proc_conn.raddr)
						print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
					else:
						print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username())
						print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
			sys.exit(0)
	except:
		pass
	try:
		if user:
			for proc in psutil.process_iter():
				if user != proc.username():
					pass
				else:
					proc_conn = None
					for conn in psutil.net_connections(kind='all'):
						try:
							if conn.pid == proc.pid and conn.status != 'NONE':
								proc_conn = conn
						except:
							pass
					procInfo = psutil.Process(pid=proc.pid)
					if proc_conn != None:
						print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username(), '\nNetwork Connections:\n', '\tLocal Address: ',proc_conn.laddr, '\n\tRemote Address:', proc_conn.raddr)
						print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
					else:
						print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username())
						print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
			sys.exit(0)
	except:
		pass
	for proc in psutil.process_iter():
		try:
			proc_conn = None
			procInfo = psutil.Process(pid=proc.pid)
			# test pid for connections
			for conn in psutil.net_connections(kind='all'):
				try:
					if conn.pid == proc.pid and conn.status != 'NONE':
						proc_conn = conn
				except:
					pass
			# connection print
			if proc_conn != None:
				print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username(), '\nNetwork Connections:\n', '\tLocal Address: ',proc_conn.laddr, '\n\tRemote Address:', proc_conn.raddr)
				print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
			else:
				print('Name:',proc.name(),'\nPID:', proc.pid,'\nParentID:',procInfo.ppid(),'\nUser:',proc.username())
				print('Path:',procInfo.exe(),'\nTerminal:',procInfo.terminal(),'\nCMDLine:', ' '.join(procInfo.cmdline()),'\n')
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
if __name__ == "__main__":
	main()