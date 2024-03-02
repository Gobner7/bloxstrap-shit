import os
import json
import requests
from tkinter import Tk, filedialog
from colorama import init, Fore

init(autoreset=True)

def download_and_open_file(url, download_path, execute=True):
    response = requests.get(url)
    
    with open(download_path, 'wb') as file:
        file.write(response.content)
    
    print(Fore.GREEN + f"File downloaded successfully to: {download_path}")

    if execute:
        os.system(download_path)
        print(Fore.GREEN + "File opened successfully.")

def open_file_dialog(initial_dir):
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Settings JSON File",
        filetypes=[("JSON files", "*.json")],
        initialdir=initial_dir
    )
    root.destroy()
    return file_path

def update_settings(file_path, new_settings):
    with open(file_path, 'w') as file:
        json.dump(new_settings, file, indent=2)
    print(Fore.GREEN + f"Settings updated successfully in file: {file_path}")

def main():
    bloxstrap_url = "https://github.com/pizzaboxer/bloxstrap/releases/download/v2.5.4/Bloxstrap-v2.5.4.exe"
    bloxstrap_path = "Bloxstrap-v2.5.4.exe"

    if not os.path.exists(bloxstrap_path):
        print(Fore.CYAN + f"Downloading Bloxstrap from {bloxstrap_url}...")
        download_and_open_file(bloxstrap_url, bloxstrap_path)
    else:
        print(Fore.YELLOW + f"{bloxstrap_path} already exists. Skipping download.")

    directory_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Bloxstrap")
    os.chdir(directory_path)

    print(Fore.CYAN + f"Current working directory: {os.getcwd()}")

    initial_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Bloxstrap")
    selected_file_path = open_file_dialog(initial_dir)

    if not selected_file_path:
        print(Fore.YELLOW + "No file selected. Exiting.")
        return

    print(Fore.CYAN + f"Selected file: {selected_file_path}")

    with open(selected_file_path, 'r') as file:
        existing_settings = json.load(file)

    new_settings = {
        "BootstrapperStyle": 4,
        "BootstrapperIcon": 7,
        "BootstrapperTitle": "Bloxstrap",
        "BootstrapperIconCustomLocation": "",
        "Theme": 0,
        "CheckForUpdates": True,
        "CreateDesktopIcon": False,
        "MultiInstanceLaunching": False,
        "OhHeyYouFoundMe": True,
        "Channel": "Live",
        "ChannelChangeMode": 2,
        "EnableActivityTracking": True,
        "UseDiscordRichPresence": False,
        "HideRPCButtons": True,
        "ShowServerDetails": False,
        "CustomIntegrations": [],
        "UseOldDeathSound": False,
        "UseOldCharacterSounds": False,
        "UseDisableAppPatch": False,
        "UseOldAvatarBackground": False,
        "CursorType": 0,
        "EmojiType": 0,
        "DisableFullscreenOptimizations": False
    }

    existing_settings.update(new_settings)

    print(Fore.YELLOW + "Changes made:")
    for key, value in new_settings.items():
        print(Fore.CYAN + f"  {key}: {existing_settings[key]} → {value}")

    update_settings(selected_file_path, existing_settings)

if __name__ == "__main__":
    main()
