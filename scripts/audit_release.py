"""Mechanical integrity checks only; does not validate scientific correctness."""
from pathlib import Path
import csv,hashlib,sys
root=Path(__file__).resolve().parents[1]
errors=[]
for line in (root/'SHA256SUMS.txt').read_text().splitlines():
    if not line.strip(): continue
    digest,relative=line.split('  ',1)
    p=root/relative
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest: errors.append(relative)
key=root/'data/benchmark/ArticleC_Frozen_180Item_Reference_Key_20261009.csv'
with key.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
ids=[r['item_id'] for r in rows]
print('Benchmark rows:',len(rows),'unique IDs:',len(set(ids)))
if len(rows)!=180 or len(set(ids))!=180: errors.append('benchmark row or ID count')
for relative in ['data/execution/ArticleC_Execution_Manifest_FROZEN_v2_4MODEL.csv','data/results/ArticleC_CrossModel_Joined_Responses_20261009.csv']:
    with (root/relative).open(encoding='utf-8-sig',newline='') as f: n=sum(1 for _ in csv.DictReader(f))
    print(relative,n)
    expected=4872 if 'Manifest' in relative else 3654
    if n!=expected: errors.append(relative+' row count')
if errors:
    print('FAILED:',errors);sys.exit(1)
print('PASS: file digests and core row counts (not scientific validation)')
