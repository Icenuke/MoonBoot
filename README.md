# Launch differents application at the boot.
## example:
	Boot in start session 	
		- Firefox
		- MyFolder
		- cmd
		- MyProg
	This is possible with the Register Database.
	HKCU (CurrentUser)
	/HKEY_CurrentUser/...
	HKLM (LocalMachine)
	/HKEY_LocalMachine/...

## In file addBootExe.ice:
	Add the path of executable application
	this file is used to add the commmand in the Register Database

## In file delBootExe.ice:
	Add the path of executable application
	this file is used to del the command in the Register Database
