import os

input_path = os.path.join('..', 'data', 'input')
output_path = os.path.join('..', 'data', 'output')
os.makedirs(input_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True)

tabs_path = os.path.join(output_path, 'tabs')
maps_path = os.path.join(output_path, 'maps')
shps_path = os.path.join(output_path, 'shps')
imgs_path = os.path.join(output_path, 'imgs')


os.makedirs(tabs_path, exist_ok=True)
os.makedirs(maps_path, exist_ok=True)
os.makedirs(shps_path, exist_ok=True)
os.makedirs(imgs_path, exist_ok=True)