from pathlib import Path
import os
P = lambda path: Path(path).absolute() 

synchting_Paths = {
    'Uomocosa-PC':    P("D:/Program Files (x86)/Syncthing"),
	'Simone-PC':      P("C:/Users/acer/Desktop/Samuele/Syncthing"),
	'Uomocosa-Linux': P("/home/uomocosa/Syncthing"),
}

desktop_Paths = {
	'Uomocosa-PC': 	  P("C:/Users/Uomocosa/Desktop"),
	'Simone-PC': 	  P("C:/Users/acer/Desktop"),
	'Uomocosa-Linux': P("/home/uomocosa/Desktop"),
}

download_Paths = {
	'Uomocosa-PC':    P("D:/Download"),
	'Simone-PC': 	  P("C:/Users/acer/Downloads"),
	'Uomocosa-Linux': P("/home/uomocosa/Downloads"),
}

def which_PC():
	for PC, abs_Path in synchting_Paths.items():
		if os.path.exists(abs_Path): return PC
	err_msg  = f"Folder Not Found"
	err_msg += f"\n>>> No folder was found in this PC"
	err_msg += f"\n>>> Here's what I searched for:"
	err_msg += f"\n\t>> {synchting_Paths}"
	err_msg += f"\n>>> To edit this, please change the file:"
	err_msg += f"\n\t>> {__file__}"

current_PC = which_PC()
synchting_Path = synchting_Paths[current_PC]
desktop_Path = desktop_Paths[current_PC]
download_Path = download_Paths[current_PC]
help_folder_Path = desktop_Path/"__HELPER_FOLDER__"
help_folder_Path.mkdir(parents=False, exist_ok=True)
