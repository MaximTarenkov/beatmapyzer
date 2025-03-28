# beatmapyzer

### Простой инструмент для анализа карт **osu!** на Python.

#### Пока планируется:
* Расчёт доли бёрст и стримов от общего числа нот
* Кластеризация карт
* Выявление частовстречающихся паттернов

---
## Использование

```python
from beatmapyzer import Beatmapyzer

mapper = Beatmapyzer()
```
### Загрузка карт из файлов

```python
 # Загрузка из директории с файлами .osz
mapper = Beatmapyzer().loader('пример/какого/то/пути', isOsz=True)

# Аналогично для файлов .osu
mapper = Beatmapyzer().loader('пример/какого/то/пути')

# Если необходимо перезаписать данные
mapper = Beatmapyzer().loader('пример/какого/то/пути', clear=True)
```


###

Если данные `.osu` файла уже загружены в память в виде байтов `bytes` или списка байтов `list[bytes]`:

```python
mapper = Beatmapyzer().parse(maps, clear=True)
```

## Работа с данными

Можно обратиться к `beatmaps`, чтобы получить базовую информацию всех карт:

```python
print(new_map.beatmaps[0]['title']) # Выводит название первой карты в списке
```

