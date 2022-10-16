# Vynae-Linux
Vynae but in linux! Work in progress, probably won't be a full port. Needed to make a linux compatible version cause it looks like I'll be on a linux box this year.

Connection filter not in yet.

Usage: ./PythonProcessTest.py <param> [option]
	-h, --help
		Displays this menu
	-n, --name
		search processes by name
	-p, -processID
		search processes by pid
	-c, --connection
		accepts 'NetOnly', 'NetSupress', and 'IP=x.x.x.x'
	-m, --parentID
		search by parentID
	-t, --terminal
		search by terminal '/dev/pts/1'
	-u, --user
		search by user
