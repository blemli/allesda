# allesda
unsere schöne Stadt

## Requirements
- python3
- (watchdog)

## develop

```bash
code . && watchmedo shell-command --patterns="*.py;*.json" --command='python3 allesda.py'
```

## Tricks
- [taginfo](https://taginfo.openstreetmap.org/)
- delete cache: `rm cache.sqlite`