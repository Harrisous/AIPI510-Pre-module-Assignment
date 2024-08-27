from src.main import view_n_lines, clean_df
import pandas as pd

def test_view_n_lines():
    # test view 5 lines
    df_tested_result = view_n_lines(pd.read_csv('test_data.csv'),5)
    df_result = pd.read_csv('test_data_view_5_lines.csv')
    assert df_tested_result.equals(df_result)

def test_clean():
    # test df cleaning
    df_tested_result = clean_df(pd.read_csv('test_data.csv'))
    df_result = pd.read_csv('test_data_clean.csv')

    # rearrange index
    df_tested_result.reset_index(drop=True, inplace=True)
    df_result.reset_index(drop=True, inplace=True)

    # type conversion, due to dropna restructure (for some reason)
    last_col = df_tested_result.columns[-1]
    df_tested_result[last_col] = df_tested_result[last_col].astype(int)
    last_col_2 = df_result.columns[-1]
    df_result[last_col_2] = df_result[last_col_2].astype(int)

    assert df_tested_result.equals(df_result)

