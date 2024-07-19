name = input("File name: ")

name = name.casefold().strip()

if name.endswith(".gif"):
    print("image/gif")
elif name.endswith(".jpg"):
    print("image/jpg")
elif name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith(".pdf"):
    print("application/pdf")
elif name.endswith(".txt"):
    print("text/txt")
elif name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
