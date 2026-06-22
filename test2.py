print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
print("test")
def get_extension(image_url):
    extension: list[str] = ['.png','.png','.jpeg','.gif','.svg']
    for exe in extension:
        if exe in image_url:
            return exe
        # else:
        #     raise ValueError("oops extension not find")


def download_image(image_url:str, image_name:str,folder:str):
    exe = get_extension(image_url)
    if exe:
        if folder:
            name = f"{folder}/{image_name}{exe}"
        else:
            name = f"{image_name}{exe}"
    else:
        raise Exception("extension not found")
    if os.path.isfile(name):
        raise ValueError("this path already exist")
ewtg