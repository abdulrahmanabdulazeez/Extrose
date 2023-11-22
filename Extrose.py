import os

# Install colorama if not already installed
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    print("Colorama not installed! Installing now...")
    os.system("python -m pip install colorama")
    from colorama import Fore, Style

# Function to print colored text
def print_color(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)

# Print ASCII art with colors
print_color("_______  _______ ____   ___  ____  _____", Fore.CYAN)
print_color("| ____\ \/ /_   _|  _ \ / _ \/ ___|| ____|", Fore.CYAN)
print_color("|  _|  \  /  | | | |_) | | | \___ \|  _|", Fore.CYAN)
print_color("| |___ /  \  | | |  _ <| |_| |___) | |___", Fore.CYAN)
print_color("|_____/_/\_\ |_| |_| \_ \\___/|____/|_____|", Fore.CYAN)

# Check if Pillow is installed
try:
    from PIL.ExifTags import TAGS
except ModuleNotFoundError:
    print_color("Pillow not installed!!!", Fore.RED)
    print_color("Installing Pillow now...", Fore.YELLOW)
    os.system("pkg install libjpeg-turbo libpng")
    os.system("python -m pip install --no-cache-dir Pillow")
    try:
        from PIL import Image, ExifTags
    except ModuleNotFoundError:
        print_color("Failed to install Pillow. Please check your setup.", Fore.RED)
        exit(1)

# Take image filename as user input
print_color("Enter the filename of the image: ", Fore.RED)
img_path = input()

# Open the image using the found path
imi = Image.open(img_path)

# Dictionary to store image information
img_inf = {
    "Filename": imi.filename,
    "Image Size": imi.size,
    "Image Height": imi.height,
    "Image Width": imi.width,
    "Image Format": imi.format,
    "Image Mode": imi.mode,
    "Image is Animated": getattr(imi, "is_animated", False),
    "Frames in Image": getattr(imi, "n_frames", 1)
}

# Print image information with colors
for label, value in img_inf.items():
    print_color(f"{label:25}: {value}", Fore.GREEN)

exifdata = imi.getexif()

# Print EXIF data with colors
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()
    print_color(f"{tag:25}: {data}", Fore.YELLOW)
