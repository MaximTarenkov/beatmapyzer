# beatmapyzer
###### [Russian README](README_ru.md)

### A simple tool for analyzing **osu!** beatmaps in Python.

#### TODO:
*   Calculation of the proportion of bursts and streams relative to the total number of notes
*   Beatmap clustering
*   Identification of frequently occurring patterns

---
## Usage

```python
from beatmapyzer import Beatmapyzer

mapper = Beatmapyzer()
```
### Loading maps from files

```python
 # Load from a directory containing .osz files
mapper = Beatmapyzer().loader('example/path/to/files', isOsz=True)

# Similarly for .osu files
mapper = Beatmapyzer().loader('example/path/to/files')

# If you need to overwrite existing data
mapper = Beatmapyzer().loader('example/path/to/files', clear=True)
```


###

If the `.osu` file data is already loaded into memory as `bytes` or a list of bytes `list[bytes]`:

```python
mapper = Beatmapyzer().parse(maps, clear=True)
```

## Working with Data

You can access `beatmaps` to get basic information for all maps:

```python
print(new_map.beatmaps[0]['title']) # Prints the title of the first map in the list
```

