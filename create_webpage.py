import html
import os

def get_files(path):
    fA = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        fA.extend(filenames)
    return fA

path = '/home/niranjan/Projects/VR/test_results_combined/22/combined/images'
webpage = html.HTML(path.replace('images',''),'Combined Images 22',refresh=30)
img = []
txts = []
links = []
files = get_files(path)
files.sort()
img.extend(files)
links.extend(files)
txts.extend(files)
for i in range(len(img)):
    webpage.add_header(txts[i])
    webpage.add_images([img[i]],[txts[i]],[links[i]],width=1280)
webpage.save()
