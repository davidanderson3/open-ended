import argparse
import json
from pathlib import Path
from bs4 import BeautifulSoup

PROFILES_FILE = Path('profiles.json')
TABLE_FILE = Path('table.json')


def load_profiles():
    if PROFILES_FILE.exists():
        with PROFILES_FILE.open() as f:
            return json.load(f)
    return []


def save_profiles(profiles):
    with PROFILES_FILE.open('w') as f:
        json.dump(profiles, f, indent=2)


def add_profile(args):
    profiles = load_profiles()
    profile = {
        'name': args.name,
        'annual_income': args.income,
        'filing_status': args.filing_status,
        'dependents': args.dependents,
        'deduction_type': args.deduction_type,
        'state': args.state,
    }
    profiles.append(profile)
    save_profiles(profiles)
    print(f"Added profile for {args.name}")


def list_profiles(_args):
    profiles = load_profiles()
    if not profiles:
        print('No profiles stored.')
        return
    for p in profiles:
        print(json.dumps(p, indent=2))


def table_to_json(args):
    html_path = Path(args.html)
    with html_path.open() as f:
        soup = BeautifulSoup(f, 'html.parser')
    table = soup.find('table')
    header_cells = table.find('tr').find_all(['th', 'td'])
    headers = [h.get_text(strip=True) for h in header_cells]
    rows = []
    for tr in table.find_all('tr')[1:]:
        cells = [td.get_text(strip=True) for td in tr.find_all('td')]
        if cells:
            rows.append(dict(zip(headers, cells)))
    with TABLE_FILE.open('w') as f:
        json.dump(rows, f, indent=2)
    print(f"Saved {len(rows)} rows to {TABLE_FILE}")


def main():
    parser = argparse.ArgumentParser(description='Manage profiles and table data')
    sub = parser.add_subparsers(dest='command')

    add_p = sub.add_parser('add-profile', help='Add a profile')
    add_p.add_argument('--name', required=True)
    add_p.add_argument('--income', type=float, required=True)
    add_p.add_argument('--filing-status', required=True, dest='filing_status')
    add_p.add_argument('--dependents', type=int, default=0)
    add_p.add_argument('--deduction-type', default='standard', dest='deduction_type')
    add_p.add_argument('--state', default='')
    add_p.set_defaults(func=add_profile)

    list_p = sub.add_parser('list-profiles', help='List profiles')
    list_p.set_defaults(func=list_profiles)

    t2j = sub.add_parser('table-to-json', help='Convert table HTML to JSON')
    t2j.add_argument('--html', default='index.html')
    t2j.set_defaults(func=table_to_json)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
