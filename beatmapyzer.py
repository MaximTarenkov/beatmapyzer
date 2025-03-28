# %%
import os
import zipfile


# %%
class Beatmapyzer:
    def __init__(self):
        self.beatmaps = []

    def parse(self, maps, clear=False):
        if clear: self.beatmaps = []
        if isinstance(maps, list):
            for b in maps:
                self.beatmaps.append(self.parse(b))
            return self
        elif isinstance(maps, bytes):
            text = maps.decode('utf-8').split('\n')
            for line in text:
                parts = line.split(":", 1)
                if len(parts) > 1 and parts[0] == 'Title': title = parts[1].strip()
                if len(parts) > 1 and parts[0] == 'BeatmapID': id = parts[1].strip()
                if len(parts) > 1 and parts[0] == 'ApproachRate': ar = parts[1].strip()
                if len(parts) > 1 and parts[0] == 'OverallDifficulty': od = parts[1].strip()
                    

            data = {
                "title": title,
                "id": id,
                "difficulty": {
                    'AR': float(ar),
                    'OD': float(od)
                }
            }
            return data


    def loader(self, input_dir, isOsz=False, clear=False):
        if clear:
            self.beatmaps = []

        if isOsz:
            paths = os.listdir(input_dir)
            for path in paths:
                if str(path).lower().endswith('osz'):
                    with zipfile.ZipFile(os.path.join(input_dir, path), 'r') as zip_ref:
                            names = zip_ref.namelist()
                            for name in names:
                                if name.lower().endswith('.osu'):  
                                    file_content_bytes = zip_ref.read(name)
                                    self.beatmaps.append(self.parse(file_content_bytes))
            return self
        else:
            for name in os.listdir(input_dir):
                if name.lower().endswith('.osu'):
                    with open(os.path.join(input_dir, name), 'rb') as f:
                        self.beatmaps.append(self.parse(f.read()))
            return self



# %%



