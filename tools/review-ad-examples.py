#!/usr/bin/env python3
"""Keep chat review decisions outside the public checkout; never edit the library."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'how-to-make-good-ads-hooks-curiosity' / 'content.json'
PRIVATE = ROOT.parent / 'private-reviews' / 'make-good-ads.json'
STATES = ('keep', 'revise', 'remove', 'skip')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('init')
    commands.add_parser('list')
    show = commands.add_parser('show')
    show.add_argument('id', nargs='?', help='Original post ID; omit to show next unreviewed example.')
    record = commands.add_parser('set')
    record.add_argument('id')
    record.add_argument('status', choices=STATES)
    record.add_argument('--note', default='')
    record.add_argument('--replacement', default='', help='Proposed description; does not change public content.')
    args = parser.parse_args()
    source = json.loads(CONTENT.read_text())
    entries = source['entries']
    by_id = {entry['id']: entry for entry in entries}
    state = json.loads(PRIVATE.read_text()) if PRIVATE.exists() else {
        'schemaVersion': 1, 'source': source['source'], 'entries': {}, 'history': []
    }
    if args.command in ('init', 'set'):
        for entry in entries:
            state['entries'].setdefault(entry['id'], {'status': 'unreviewed', 'note': '', 'proposedDescription': '', 'reviewedAt': None})
        if args.command == 'set':
            if args.id not in by_id:
                parser.error('Unknown original post ID; no review was written.')
            decision = {'status': args.status, 'note': args.note, 'proposedDescription': args.replacement,
                        'reviewedAt': datetime.now(timezone.utc).isoformat()}
            state['entries'][args.id] = decision
            state['history'].append({'id': args.id, **decision})
        PRIVATE.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        temporary = PRIVATE.with_suffix('.tmp')
        temporary.write_text(json.dumps(state, indent=2, ensure_ascii=False) + '\n')
        temporary.chmod(0o600)
        temporary.replace(PRIVATE)
        print(json.dumps({'saved': str(PRIVATE), 'publicLibraryChanged': False}))
    elif args.command == 'list':
        print(json.dumps([{'number': i, 'id': e['id'], 'title': e['title'],
                           **state['entries'].get(e['id'], {'status': 'unreviewed'})}
                          for i, e in enumerate(entries, 1)], indent=2, ensure_ascii=False))
    else:
        selected = args.id
        if selected and selected not in by_id:
            parser.error('Unknown original post ID.')
        if not selected:
            selected = next((e['id'] for e in entries if state['entries'].get(e['id'], {}).get('status', 'unreviewed') == 'unreviewed'), None)
            if not selected:
                selected = next((e['id'] for e in entries if state['entries'].get(e['id'], {}).get('status') == 'skip'), None)
        if not selected:
            print(json.dumps({'complete': True, 'message': 'Every example has a decision. No public changes have been applied.'}))
            return
        entry = by_id[selected]
        print(json.dumps({'number': entries.index(entry) + 1, 'total': len(entries), **entry,
                          'screenshot': str(CONTENT.parent / entry['image']),
                          'review': state['entries'].get(selected, {'status': 'unreviewed'})}, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
