import subprocess
import time
import sys
import os

gallery_dl_path = r"gallery-dl.exe"
if not os.path.exists(gallery_dl_path):
    print("[ X_X ] Error: gallery-dl.exe not found. Please install it first.")
    sys.exit(1)

ascii_art = r'''
  __  __                     _       _             __     ___ 
 |  \/  | __ ___  _____ __ _| |_ ___| |__   ___ _ _\ \   / / |
 | |\/| |/ _` \ \/ / __/ _` | __/ __| '_ \ / _ \ '__\ \ / /| |
 | |  | | (_| |>  < (_| (_| | || (__| | | |  __/ |   \ V / | |
 |_|  |_|\__,_/_/\_\___\__,_|\__\___|_| |_|\___|_|    \_/  |_|         
'''

print(ascii_art)

print("Loaded! Welcome to Maxcatcher V1, a Gallery-DL Companion Script.\nWindows-Port made for BnBigus by fuchs.gay\nBased on the original Marecaptcher Script by Schneili\nHave fun archiving!\nPS: Some Websites like Derpibooru need a custom Config.\nMake sure to read the Gallery-DL Docu if you need some Information about the Configs.\nRead more about it here: https://github.com/mikf/gallery-dl")
time.sleep(2)

print("\nOptions:")
print("[1] Start now")
print("[2] Cancel")
choice = input("Enter your choice: ")

# Define the URLs you wanna download here!
urls = [
    "https://e621.net/posts?tags=bnbigus",
    "https://e621.net/posts?tags=mintyderg",
    "https://e621.net/posts?tags=lezified"
]

if choice == "1":
    print(">> Starting downloads...")
elif choice == "2":
    print(">> Cancelled.")
    sys.exit(0)
else:
    print("Invalid choice.")
    sys.exit(1)

try:
    while True:
        success_count = 0
        error_count = 0

        for url in urls:
            if not url:
                continue

            print(f"\n[ Info ] Downloading from: {url}")

            try:
                result = subprocess.run(
                    [gallery_dl_path, "--retries", "1", "--filename", "{filename[:50]}.{extension}", "--rename", "{filename[:50]}", url],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                print("[ >> ] Success: " + url)
                success_count += 1
            except subprocess.CalledProcessError as e:
                print(f"[ >> ] Failed to download from: {url}")
                print("Error:", e.stderr.decode())
                error_count += 1

        print(f"\nDownload summary:")
        print(f"  [ >> ] Success: {success_count}")
        print(f"  [ >> ] Errors: {error_count}")

        print("\n[ >> ] Finished ripping.")
        print("Sleeping for 12 hours...")
        time.sleep(43200)  # Sleeping for 12h

except KeyboardInterrupt:
    print("\n\n[ Bye! ] Script stopped! See you next time uwu")
    sys.exit(0)

