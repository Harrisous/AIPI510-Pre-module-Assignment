import pandas as pd
import click
import os

# function to display the information of the file
def show_info(df):
    return df.info()

# function to display the first n lines of the file
def view_n_lines(df, num_lines):
    return df.head(num_lines)

# function to clean the file and save it to a new file
def clean_df(df):
    # drop columns then rows
    df.dropna(axis=1, how='all', inplace=True)
    df.dropna(inplace=True)
    return df

# function to save the cleaned file
def save_to_csv(df):
    # save the cleaned file
    output_path = os.path.join('.', 'data', 'processed', 'cleaned_file.csv') # avoid system specific path issues
    df.to_csv(output_path, index=False) # do not include the index
    print('File cleaned and saved at ./data/processed/cleaned_file.csv')


@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--info', is_flag=True, help="Display the information of the file")
@click.option('--view', type=int, help="Display the first n lines of the file")
@click.option('--clean', is_flag=True, help="Clean the file and save it to a new file")
def main(file_path, info, view, clean):
    # read the file
    try:
        with open(file_path, 'r') as file:
            df = pd.read_csv(file_path)
            # check the flags in sequence
            if info:
                print(show_info(df))
            if view:
                print(view_n_lines(df, view))
            if clean:
                cleaned_df = clean_df(df)
                save_to_csv(cleaned_df)
    except Exception as e:
        print(e)
        return

# entry point for the application
if __name__ == '__main__':
    main()