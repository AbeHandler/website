# Theory concordance

## Files

- `filtered_ft50.csv` — metadata for papers (title, authors, abstract, plink, doi, etc.), filtered to full-text available
- `papers/` — PDFs downloaded from EBSCO, named by plink ID (e.g. `a4718fb4-c88d-36ed-880f-dd53d514f5cc.pdf`)
- `runner.py` — downloads PDFs from EBSCO via Playwright; reads plink URLs from `filtered_ft50.csv`
- `filter_ft50.py` — filters source CSVs to produce `filtered_ft50.csv`

## Joining metadata to PDFs

The PDF filename stem is the plink ID. To join back to metadata:

```python
import pandas as pd
df = pd.read_csv("filtered_ft50.csv")
df["plink_id"] = df["plink"].str.split("/").str[-1]
# then match plink_id to pdf filename stem
```

## Backup

```
just backup
```

Produces `dsr_papers_YYYYMMDD.tar.gz` containing `filtered_ft50.csv` and `papers/`.

Upload to [OneDrive / DSR papers](https://o365coloradoedu-my.sharepoint.com/:f:/r/personal/abha4861_colorado_edu/Documents/DSR%20papers?csf=1&web=1&e=ltTJcn).
