import argparse
from sklearn.model_selection import train_test_split
import pandas as pd



def split_data(args):
    """
    Split data into 6 : 2 : 2
    """
    data = pd.read_csv(args.data_path)
    train_data, test_data = train_test_split(data, test_size=0.4, random_state=args.random_seed)
    test_data, valid_data = train_data(test_data, test_size=0.5, random_state=args.random_seed)
    train_data = train_data.rename({'essay': 'text'})
    test_data = test_data.rename({'essay': 'text'})
    valid_data = valid_data.rename({'essay': 'text'})
    train_data.to_csv(args.train_path)
    test_data.to_csv(args.test_path)
    valid_data.to_csv(args.valid_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Split data'
    )
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--train_path', type=str, required=True)
    parser.add_argument('--test_path', type=str, required=True)
    parser.add_argument('--valid_path', type=str, required=True)
    parser.add_argument('--random_seed', type=int, required=True, default=42)
