from win32com import client
import subprocess

def killChromeProcess():
    """
    Get the process ID of Microsoft Edge
    """
    for task in client.GetObject('winmgmts:').InstancesOf('win32_process'):
        if task.name == 'chrome.exe':
            subprocess.check_output(f"Taskkill /PID {task.processID} /F")
            break
if __name__ == '__main__':
    killChromeProcess()
