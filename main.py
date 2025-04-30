try: 
    from PIL import Image
    from tqdm import tqdm
    import os
except:
    print("Could not resolve imports")
    exit()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def get_all_png_files(folder):
    png_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.png'):
                png_files.append(os.path.join(root, file))
    return png_files

def convert_png_to_ico(folder):
    png_files = get_all_png_files(folder)
    total_files = len(png_files)

    if total_files == 0:
        print(bcolors.WARNING + "No .png files found." + bcolors.ENDC)
        return

    print(bcolors.OKCYAN + f"Found {total_files} .png file(s).\n" + bcolors.ENDC)

    for index, png_path in enumerate(tqdm(png_files, desc="Converting", unit="file")):
        file = os.path.basename(png_path)
        ico_path = os.path.splitext(png_path)[0] + ".ico"

        try:
            img = Image.open(png_path)
            img.save(ico_path, format='ICO', sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)])
            tqdm.write(bcolors.OKGREEN + f"Converted: {file} → {os.path.basename(ico_path)} ({index + 1} / {total_files})" + bcolors.ENDC)
        except Exception as e:
            tqdm.write(bcolors.FAIL + f"Failed to convert {file}: {e}" + bcolors.ENDC)

if __name__ == "__main__":
    print(bcolors.HEADER + "PNG to ICO CLI\nWritten by Tobias Kisling using the Pillow library\n" + bcolors.ENDC)
    folder_path = input("Enter the absolute folder path containing .png files: ").strip()

    if os.path.isdir(folder_path):
        convert_png_to_ico(folder_path)
        print(bcolors.WARNING + "Conversion finished!" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Invalid folder path." + bcolors.ENDC)
