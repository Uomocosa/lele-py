import subprocess

def run_shell_command(
	cmd, 
	cwd=None, 
	shell=True,
):
	# print(f"~!~ RUNNING shell command: '{cmd}'")
	sub_output = subprocess.run(
		cmd, 
		cwd=cwd,
		capture_output=True, 
		universal_newlines=True, 
		text=True, 
		shell=shell, 
		encoding = "windows-1252",
	)
	output = str(sub_output.stdout) + str(sub_output.stderr)
	return output.strip()



def test_():
	assert run_shell_command("echo Hi!") == "Hi!"
