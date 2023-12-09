import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    
    df=pd.read_csv(df).pivot(index='id_1', columns='id_2', values='car').fillna(0)

    return df
result_df=generate_car_matrix(/datasets/dataset-1.csv)
print(result_df)


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    df=pd.read_csv(df)
    df['car_type']=pd.cut(df['car'],bins=[float('-inf'),15,25,float('inf')], labels=['low', 'medium', 'high'], right=False)
    type_counts= df['car_type'].value_counts().sort_index()
    return dict(sorted(type_counts.items()))
result=get_type_count('/Users/HP/Downloads/dataset-1.csv')
print(result)


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    df=pd.read_csv(df)
    bus_mean=df['bus'].mean()
    bus_indexes= df[df['bus']> 2*bus_mean].index.tolist()
    bus_indexes.sort()
    
    return bus_indexes
result=get_bus_indexes('/Users/HP/Downloads/dataset-1.csv')
print(result)


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
