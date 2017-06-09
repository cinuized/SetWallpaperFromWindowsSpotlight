#!/usr/bin/env python
import os
from PIL import Image
import time

# Importang Directories
spotlightSource = os.path.join(os.environ['LOCALAPPDATA'], "Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")
spotlightRoot = os.path.join(os.environ['USERPROFILE'], r"Pictures\Spotlight")
copyAssetsRoot = os.path.join(os.environ['USERPROFILE'], r"Pictures\Spotlight\CopyAssets")
horizontalRoot = os.path.join(os.environ['USERPROFILE'], r"Pictures\Spotlight\Horizontal")
verticalRoot = os.path.join(os.environ['USERPROFILE'], r"Pictures\Spotlight\Vertical")


# Create directory for Spotlight pictures
if not os.path.exists(spotlightRoot):
  os.makedirs(copyAssetsRoot)
  os.makedirs(horizontalRoot)
  os.makedirs(verticalRoot)
else:
  for oldfile in os.listdir(copyAssetsRoot):
    os.remove(os.path.join(copyAssetsRoot, oldfile))

# Paste all Image larger than 100kb to USERPROFILE\Picture\Spotlight\CopyAssets
for file in os.listdir(spotlightSource): 
  if os.path.getsize(os.path.join(spotlightSource, file)) < 100000: # file size < 100kb
    continue
  f = open(os.path.join(spotlightSource, file), "rb").read()
  
  if f[0] == 0:
    continue
  if not os.path.exists(os.path.join(copyAssetsRoot, file + r'.jpg')):
    open(os.path.join(copyAssetsRoot, file + r'.jpg'), "wb").write(open(os.path.join(spotlightSource, file), "rb").read())
  else:
    continue

# delivery jpg to h/v directories
for newfile in os.listdir(copyAssetsRoot):
  image = Image.open(os.path.join(copyAssetsRoot, newfile))
  if image.size[0] == 1080:
    f = open(os.path.join(verticalRoot, newfile), "wb")
    f.write(open(os.path.join(copyAssetsRoot, newfile), "rb").read())
    f.close()
  if image.size[0] == 1920:
    f = open(os.path.join(horizontalRoot, newfile), "wb")
    f.write(open(os.path.join(copyAssetsRoot, newfile), "rb").read())
    f.close()
  image.close()

for oldfile in os.listdir(copyAssetsRoot):
  os.remove(os.path.join(copyAssetsRoot, oldfile))

# log
open(os.path.join(spotlightRoot, "log.log"), "a+").write("Update at " + time.strftime('%Y-%m-%d: %H:%M:%S',time.localtime(time.time())) + "\n")