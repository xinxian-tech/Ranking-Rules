import argparse
import pandas as pd

arg_parser = argparse.ArgumentParser(
    description='Generate the vote table files for all team members.'
)
arg_parser.add_argument(
    '--names',
    help='names of the team members, separate by \',\'.',
    type=str,
    required=True
)
arg_parser.add_argument(
    '--output_dir', 
    help='output directory of the vote table files', 
    type=str,
    default='./'
)
args = arg_parser.parse_args()

member_names = args.names.split(',')
for name in member_names:
    print(name)
if len(member_names) == 0 or any(len(name) == 0 for name in member_names):
    print('Invalid --name argument. Use -h to see the requirements.')
    exit()
elif len(member_names) == 1:
    print('Number of names should be more than 1.')
    exit()

df_content = {'name': [name for name in member_names]}
df_content = {**df_content, **{name: [1 for _ in range(len(member_names))] for name in member_names}}
df_content = {** df_content, **{'Filling Guide': 'https://github.com/xinxian-tech/Ranking-Rules'}}

unfilled_table = pd.DataFrame(df_content).set_index('name')

unfilled_table.to_csv(args.output_dir + 'vote_table.csv')

print('Generation complete. See the output files at', args.output_dir)
print('After filling the tables, run rank.py')