from lib import *
from tqdm import tqdm

BASE_URL = "https://networks.skewed.de/net/"

all_online_networks = pd.read_csv(DATA_DIR_PATH / "online_social_networks.csv")

progress = tqdm(unit="network", total=len(all_online_networks))
# download all online networks
for i, row in all_online_networks.iterrows():
    size = row["nodes_qcut"]
    url = BASE_URL + row["group"] + "/files/" + row["name"] + ".gml.zst"
    groupname = Path(get_group_name_from_url(url))
    filename = Path(get_filename_from_url(url))
    local_dir = DATA_DIR_PATH / "online" / size / groupname
    local_dir.mkdir(parents=True, exist_ok=True)
    local_path = remove_file_suffix(str(local_dir / filename))
    download_and_extract(url, local_path)
    progress.update(1)
    
    
all_offline_networks = pd.read_csv(DATA_DIR_PATH / "offline_social_networks.csv")

progress = tqdm(unit="network", total=len(all_online_networks))

# download all offline networks
for i, row in all_offline_networks.iterrows():
    size = row["nodes_qcut"]
    url = BASE_URL + row["group"] + "/files/" + row["name"] + ".gml.zst"
    groupname = Path(get_group_name_from_url(url))
    filename = Path(get_filename_from_url(url))
    local_dir = DATA_DIR_PATH / "offline" / size / groupname
    local_dir.mkdir(parents=True, exist_ok=True)
    local_path = remove_file_suffix(str(local_dir / filename))
    download_and_extract(url, local_path)
    progress.update(1)