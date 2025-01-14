# Simple script to dump all dns records for a domain

## Preparation

- Install the `dnspython` package: `pip install -r requirements.txt` or `pip install dnspython`

## Run

```bash
python3 dns-dump.py <domain>
```

## Result

The result will be saved to `dns-dump-<domain>.txt`

## Example

```bash
python3 dns-dump.py digistate.nl
```

Result: `dns-dump-digistate.nl.txt`

## Notes

The file `DNS-types.csv` is a copy of the table from [Wikipedia](https://en.wikipedia.org/wiki/List_of_DNS_record_types).
