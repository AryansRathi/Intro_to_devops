
import os

rightdir = "C:\\Users\\aryansrathi\\Desktop\\folder\\DevOps"
rightimages = []
for subdir, dirs, files in os.walk(rightdir):
    for file in files:
        rightimages.append(os.path.join(subdir, file))

wrongdir = "C:\\Users\\aryansrathi\\Desktop\\folder\\DevOps"
wrongimages = []
for subdir, dirs, files in os.walk(wrongdir):
    for file in files:
        wrongimages.append(os.path.join(subdir, file))

print(rightimages)
print(wrongimages)

for i in range(len(rightimages)):
    right_image_dir = rightimages[i]
    wrong_image_dir = wrongimages[i]
