import yaml

for code, yaml_p in [
    ('HLTINF006', 'answers_HLTINF006.yaml'),
    ('CHCAGE013', 'answers_CHCAGE013.yaml')
]:
    print(f"\n{'='*20} {code} REMAINING EMPTY {'='*20}")
    with open(yaml_p, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    empty = [f for f in data['fields'] if f['type'] == 'text' and f['section'] != 'Assessor Section' and (not f['value'] or not str(f['value']).strip())]
    print(f"Total: {len(empty)}")
    for e in empty:
        print(f"  Table {e['table_idx']:2d} R{e['row_idx']} C{e['col_idx']} idx{e['index_in_cell']} [{e['field_id']}]: {e['label'][:70]}")
