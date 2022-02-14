from PIL import Image
import os

folder_dir = "imgs"
for infile in os.listdir(folder_dir) :
    print(infile)
    startImg = Image.open(f"{folder_dir}/{infile}")
    head = Image.new("RGBA", (2475, 1155), (255, 0, 0, 0))
    test = startImg.copy()
    head.paste(test, (130, 134))
    head.paste(test, (2475 - (130 + test.size[0]), 134))

    head.save(f"out/resized {infile}", "png")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
