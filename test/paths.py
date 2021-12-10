import os

input_path = os.path.join('..', 'data')
tabs_path = os.path.join(input_path, 'tabs')
maps_path = os.path.join(input_path, 'maps')
shps_path = os.path.join(input_path, 'shps')
imgs_path = os.path.join(input_path, 'imgs')

os.makedirs(input_path, exist_ok=True)
os.makedirs(tabs_path, exist_ok=True)
os.makedirs(maps_path, exist_ok=True)
os.makedirs(shps_path, exist_ok=True)
os.makedirs(imgs_path, exist_ok=True)