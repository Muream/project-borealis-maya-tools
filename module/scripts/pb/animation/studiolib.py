import studiolibrary
from pb.general.assets import assets_dir
import os

def open_shared_lib():
    path = assets_dir()
    shared_lib = os.path.join(path, "_studiolibrary")

    if not os.path.exists(shared_lib):
        os.makedirs(shared_lib)

    studiolibrary.main(name="Project Borealis Animation Library", path=shared_lib)
