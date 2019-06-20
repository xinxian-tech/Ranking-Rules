import argparse
import pandas as pd
import numpy as np
import glob
import os

arg_parser = argparse.ArgumentParser(
    description='Rank the team member\'s contribution according to vote tables.'
)
arg_parser.add_argument(
    '--input_dir', 
    help='input directory of the vote table files. all .csv files in this directory will be processed.', 
    type=str,
    default='./'
)
args = arg_parser.parse_args()

matrix_list = []
name_list = []
prev_file_name = ''

os.chdir(args.input_dir)
for file_name in glob.glob('*.csv'):
        df = pd.read_csv(args.input_dir + file_name)
        name_list = [*df['name']]
        df = df.drop(['name', 'Filling Guide'], axis=1)
        if len(matrix_list) != 0 and df.values.shape != matrix_list[-1].shape:
            print('Vote table shape mismatch:', file_name, 'and', prev_file_name)
            exit()
        for element in np.nditer(df.values):
            if element < 0:
                print('Non-positive value detected in', file_name, ', abort ranking.')
                exit()
        matrix_list.append(df.values)
        prev_file_name = file_name

ahp_matrix = np.mean(np.array(matrix_list), axis=0)
assert ahp_matrix.shape[0] == ahp_matrix.shape[1]
ahp_weights = np.mean(ahp_matrix, axis=1)
ahp_weights = ahp_weights / np.sum(ahp_weights)
eigen_max = np.mean(np.matmul(ahp_matrix, ahp_weights) / ahp_weights)
ci = (eigen_max - ahp_matrix.shape[0]) / (ahp_matrix.shape[0] - 1)

name_list = [name for _, name in sorted(zip(ahp_weights, name_list), reverse=True)]
ahp_weights = sorted(ahp_weights, reverse=True)

print('_' * 70)
print("{:>10s}{:>20s}{:^40s}".format('ranking', 'weight', 'name'))
for index in range(ahp_matrix.shape[0]):
    print("{:>10d}{:>20.5f}{:^40s}".format(index + 1, ahp_weights[index], name_list[index]))
print('CI:', ci)
print('-' * 70)