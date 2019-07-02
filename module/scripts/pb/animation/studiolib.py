import studiolibrary
from pb.general.assets import get_assets_dir
import os

def open_shared_lib():
    assets_dir = get_assets_dir()
    shared_lib = os.path.join(assets_dir, "_studiolibrary")

    if not os.path.exists(shared_lib):
        os.makedirs(shared_lib)

    studiolibrary.main(name="Project Borealis Animation Library", path=shared_lib)
