""" week7_slides_p1.py

Scaffold with the codes we will discuss during the first part of the class (Week 7)

"""
import pprint as pp

import pandas as pd

# This is an auxiliary function, please do not modify
def printit(obj, msg=None):
    """ Pretty prints `obj` as long as `obj` is not '?'

    Parameters
    ----------
    obj : any object
        If a string equal to '?', do not print anything

    msg : str, optional
        Message preceding obj representation

    """
    sep = '-'*40
    if isinstance(obj, str) and obj == '?':
        return None
    elif isinstance(obj, str):
        prt = obj
    elif isinstance(obj, (pd.DataFrame, pd.Series)):
        prt = obj.to_string()
    else:
        prt = pp.pformat(obj)
    if not isinstance(obj, str):
        prt = f'{prt}\n\nType: {type(obj)}'
    if msg is not None:
        prt = f'{msg}\n\n{prt}'
    to_print = [
        '',
        sep,
        prt,
        sep,
    ]
    print('\n'.join(to_print))


# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
    '2020-01-02',
    '2020-01-03',
    '2020-01-06',
    '2020-01-07',
    '2020-01-08',
    '2020-01-09',
    '2020-01-10',
    '2020-01-13',
    '2020-01-14',
    '2020-01-15',
]
prices = [
    7.1600,
    7.1900,
    7.0000,
    7.1000,
    6.8600,
    6.9500,
    7.0000,
    7.0200,
    7.1100,
    7.0400,
]
# Trading day counter
bday = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10]

# ----------------------------------------------------------------------------
#   Create instances
# ----------------------------------------------------------------------------
# Create a series object
ser = pd.Series(data=prices, index=dates)
#printit(ser, "The series `ser`:")

# Data Frame with close and Bday columns
df = pd.DataFrame(data={'close': ser, 'bday': bday}, index=dates)
#printit(df, "The data frame `df`:")


# ----------------------------------------------------------------------------
#   Selection using Series
#   1. Use ser.loc to select using labels
#       1.1. Single label
#       1.2. List of labels
#       1.2. Slice of labels
#   2. Use ser.iloc to select using position (integers)
#       2.1. Single integer
#       2.2. List integers
#       2.2. Slice of integers
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
#   Series
# ----------------------------------------------------------------------------
# ser:
#   2020-01-02    7.16
#   2020-01-03    7.19
#   2020-01-06    7.00
#   2020-01-07    7.10
#   2020-01-08    6.86
#   2020-01-09    6.95
#   2020-01-10    7.00
#   2020-01-13    7.02
#   2020-01-14    7.11
#   2020-01-15    7.04


# ------------------------------------------------------------
# Series.loc: Selection using a single label
# ser.loc[label] --> scalar if label in index, error otherwise
# ------------------------------------------------------------
label = '2020-01-10'
res  = '?'
# <solution>
#res = ser.loc[label]
# </solution>
printit(res, f"ser.loc[{label}]:")

# IMPORTANT: Label must exist in the index
label = '2020-01-30'
#res = ser.loc[label] # --> KeyError



# ------------------------------------------------------------
# Series.loc: Selection using a sequence of labels
# ser.loc[seq] --> series if labels in index, error otherwise
# ------------------------------------------------------------
label_seq = ['2020-01-10', '2020-01-13']
res  = '?'
# <solution>
#res = ser.loc[label_seq]
# </solution>
printit(res, f"ser.loc[{label_seq}]")

# Every label must exist
label_seq = ['2020-01-10', '2020-01-11']
#res = ser.loc[label_seq] # --> KeyError

# ------------------------------------------------------------
# Series.loc: Selection using slices
# ser.loc[slice] --> series
# ------------------------------------------------------------
# IMPORTANT: ENDPOINTS ARE INCLUDED!!!
start = '2020-01-10'
end = '2020-01-13'
res  = '?'
# <solution>
#res = ser.loc[start:end]
# </solution>
printit(res, f"ser.loc[{start}:{end}]")


# Pandas will return the interval of labels between the slice and index
start = '3020-01-10'
end = '2020-01-13'
res  = '?'
# <solution>
#res = ser.loc[start:end]
# </solution>
printit(res, f"ser.loc['{start}':'{end}']")

# IMPORTANT: Selection using slices will NOT GENERATE ERRORS as long as the labels
# data type is consistent with the index. For instance:
start = 'start'
end = 'end'
res  = '?'
# <solution>
#res = ser.loc[start:end]
# </solution>
printit(res, f"ser.loc['{start}':'{end}']")



# ------------------------------------------------------------
# ser.loc can be used in assignemnt statements:
# <target> = <expression>
# ------------------------------------------------------------

# Example 1: changing values associated with existing labels
#ser2 = ser.copy()
#old_label = '2020-01-10' # NOTE: This label exists in the index
#ser2.loc[old_label] = -99
#printit(ser2, f"The ser2:")


# Example 2: If the label does not exist, pandas will append it to the series
#new_label = '2020-01-11' # NOTE: This label does not exist
#ser2.loc[new_label] = -99
#printit(ser2, f"The new ser2:")

# Be careful when appending observations and then using slices
#start = '2020-01-10'
#end = '2020-01-13'
#res = ser2.loc[start:end]
#printit(res, f"ser2.loc['{start}':'{end}'] \nNOTE: '{new_label}' not included!")

# The problem is that the index is not sorted
#ser2.sort_index(inplace=True)
#res = ser2.loc[start:end]
#printit(res, f"ser2.loc['{start}':'{end}'] \nNOTE: after sorting")



# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# Series.iloc: Selection using positions
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------


# ------------------------------------------------------------
# Series.iloc: Selection using a single pos
# ser.iloc[pos] --> scalar if pos <= ser.size
# ------------------------------------------------------------
#printit(ser.size, f"ser.size:")
pos = 0
res  = '?'
# <solution>
#res = ser.iloc[0]
# </solution>
printit(res, f"ser.iloc[{pos}]")

# ------------------------------------------------------------
# Series.iloc: Selection using a seq of positions
# ser.iloc[seq of pos] --> series if pos <= ser.size
# ------------------------------------------------------------
# Try it first!
pos_seq = [0, 1]
#res = ser.iloc[pos_seq]
#printit(res, f"ser.iloc[{pos_seq}]")

# ------------------------------------------------------------
# Series.iloc: Selection using slices
#   ser.iloc[slice] --> series
#
# IMPORTANT: Endpoints are NOT included
# ------------------------------------------------------------
# Try it first!
start = 0
end = 1
res  = '?'
# <solution>
#res = ser.iloc[start:end]
# </solution>
printit(res, f"ser.iloc[{start}:{end}]:")

res = '?'
#printit(res, f"ser.iloc[0]")


# pandas will try to return the interval of "positions" inside the slice
start = 0
end = 100000
res  = '?'
# <solution>
#res = ser.iloc[start:end]
# </solution>
printit(res, f"ser.iloc[{start}:{end}]")

# Very common mistake...
start = -1
end = 0
#res = ser.iloc[start:end]
#printit(res, f"ser.iloc[{start}:{end}]")


# --------------------------------------------------------------------------------------------
# Series[] : In the past, you sould use [] with both positions and labels.
# Using ser[pos] will be deprecated
#
# My advice: Always use either loc or iloc, not []
#
# | Selection                     | Result       | Notes                                     |
# |-------------------------------|--------------|-------------------------------------------|
# | Series[label]                 | scalar value | Label must exist, otherwise KeyError      |
# | Series[list of labels]        | Series       | All labels must exist, otherwise KeyError |
# | Series[start_label:end_label] | Series       | Behaviour will vary                       |
# --------------------------------------------------------------------------------------------

pos = 0
#x1  = ser[pos] # -> Deprecation warning
#res = ser.iloc[pos]
#printit(res, f"This is res")
#printit(x1, f"This is x1")

# You can use labels and []
label = '2020-01-02'
#x2  = ser[label]
#res = ser.loc[label]
#printit(res, f"This is res")
#printit(x2, f"This is x2")




# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
#   Secting observations from data frames
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# df:
#             close  bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
# 2020-01-06   7.00     3
# 2020-01-07   7.10     4
# 2020-01-08   6.86     5
# 2020-01-09   6.95     6
# 2020-01-10   7.00     7
# 2020-01-13   7.02     8
# 2020-01-14   7.11     9
# 2020-01-15   7.04    10


# ----------------------------------------------------------------------------
# DataFrames.loc[row indexer, col indexer] :  Indexing by row and column labels
#
# where indexer can be:
#
#   - a single label
#   - a sequence of labels
#   - a slice of labels
#
# Note:
#   df.loc[row indexer] same as df.loc[row indexer, :]
#
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# DataFrames.loc using single labels
# ----------------------------------------------------------------------------
#printit(df.index, "The df.index:")
#printit(df.columns, "The df.columns:")


# df.loc[row label, col label] --> scalar
rlabel = '2020-01-02'
clabel = 'close'
res  = '?'
# <solution>
#res = df.loc[rlabel, clabel]
# </solution>
printit(res, f"df.loc[{rlabel}, {clabel}]")


# df.loc[row label] --> df.loc[row label, :]
# In both cases, the result is a SERIES
res1 = '?'
res2 = '?'
# <solution>
#res1 = df.loc[rlabel, :]
#res2 = df.loc[rlabel]
# </solution>
printit(res1, f"This is df.loc['{rlabel}', :]")
printit(res2, f"This is df.loc['{rlabel}']")

# df.loc[ column label ] --> KeyError (unless there row with same label exists)
#res = df.loc[rlabel]

# df.loc[:, clabel] --> series with column values (same index)
res = '?'
#printit(res, f"df.loc[:, 'close']")

# ----------------------------------------------------------------------------
# DataFrames.loc using seq of labels
#
# NOTE:
#   df.loc[label, seq of labels] --> series with COLUMN labels
#   df.loc[seq of labels, label] --> series with ROW (index) labels
# ----------------------------------------------------------------------------
rlabel = '2020-01-02'
rlabel_seq = ['2020-01-02', '2020-01-06']

clabel = 'close'
clabel_seq = ['close', 'bday']

# -------------------
# df.loc[seq labels, label] --> series with rows as index labels
# df.loc[label, seq labels] --> series with cols as index labels
# -------------------

# 1. df.loc[label, seq labels]
res = '?'
# <solution>
#res = df.loc[rlabel, clabel_seq]
# </solution>
printit(res, f"df.loc['{rlabel}', {clabel_seq}]")

# 1. df.loc[seq labels, label]
res = '?'
# <solution>
#res = df.loc[rlabel_seq, clabel]
# </solution>
printit(res, f"df.loc[{rlabel_seq}, '{clabel}'] is:")



# ----------------------------------------------------------------------------
# DataFrames.loc using slices
# ----------------------------------------------------------------------------
clabel_start = 'close'
clabel_end =   'bday'

rlabel_start = '2020-01-10'
rlabel_end = '2020-01-15'

# df.loc[slice, slice] --> data frame
res  = '?'
# <solution>
#res = df.loc[\
#      '2020-01-10':'2020-01-15',
#      'bday':'close']
# </solution>
printit(res, f"df.loc['2020-01-10':'2020-01-15','bday':'close']")

# Remember that pandas will not sort the index before selecting the objs
#df2 = df.copy()
#df2.sort_index(axis=1, inplace=True)
#res = df2.loc[ \
#      '2020-01-10':'2020-01-15',
#      'bday':'close']
#printit(res, f"df2.loc['2020-01-10':'2020-01-15','bday':'close']")



# ----------------------------------------------------------------------------
# Exercise: Use df.loc[slice, label] so the following series is returned:
#   2020-01-10     7
#   2020-01-13     8
#   2020-01-14     9
#   2020-01-15    10
# ----------------------------------------------------------------------------
res = '?'
# <solution>
#res = df.loc['2020-01-10':'2020-01-15', 'bday']
# </solution>
printit(res)


# ----------------------------------------------------------------------------
# Exercise: Use df.loc[label, '2020-01-02'] WITHOUT MODIFYING DF,
# so the following series is returned for '2020-01-02':
#  close    7.16
#  bday     1.00
# ----------------------------------------------------------------------------
rlabel = '2020-01-02'
res = '?'
# <solution>
# Remember that 'label':  will return all obs from 'label' until the end
# of the index
#res = df.loc[rlabel, 'close':]
# </solution>
printit(res)




# ----------------------------------------------------------------------------
# DataFrames.iloc[row indexer, col indexer] :  Indexing by row and column positions
#
# where indexer can be:
#
#   - a single position
#   - a sequence of positions
#   - a slice of positions
#
# Note:
#   df.iloc[row indexer] same as df.iloc[row indexer, :]
#
# ----------------------------------------------------------------------------

# Analogous to moving from ser.loc to ser.iloc. Will be left as an exercise

# ----------------------------------------------------------------------------
# DataFrames.iloc using single labels
# ----------------------------------------------------------------------------

# Exercise: Use df.iloc to return the element in the first column and second row,
# or 7.19
res = '?'
# <solution>
# df.iloc[pos, pos] --> scalar
#cpos = 0
#rpos = 1
#res = df.iloc[rpos, cpos]
# </solution>
printit(res)

# Exercise: Use df.iloc[pos] to select the last row of df, which will be the folllowing
# series:
#   close     7.04
#   bday     10.00
res = '?'
# <solution>
# Note: df.iloc[pos] --> df.iloc[pos, :] --> series iff pos <= df.shape[0]
# If pos > df.shape[0], exception
#res = df.iloc[-1]
#printit(df.shape)
# </solution>
printit(res)

# ----------------------------------------------------------------------------
# DataFrames.iloc using seq of labels and slices
# ----------------------------------------------------------------------------
# Exercise:
# Use .iloc to produce the following objects from df
#   1. a DF with all rows from df but with the order of columns reversed
#   2. a SERIES with the last two values from the 'bday' column
#   3. a DF with the the first two rows of df (and all columns)

# 1. a DF with all rows from df but with the order of columns reversed:
#               bday  close
#   2020-01-02     1   7.16
#   2020-01-03     2   7.19
#   2020-01-06     3   7.00
#   2020-01-07     4   7.10
#   2020-01-08     5   6.86
#   2020-01-09     6   6.95
#   2020-01-10     7   7.00
#   2020-01-13     8   7.02
#   2020-01-14     9   7.11
#   2020-01-15    10   7.04
res1 = '?'
# <solution>
# Different approaches which give the same results:
# I think the most elegant is the first one
#res1 = df.iloc[:, ::-1]
#
#res1  = df.iloc[:, [1, 0]]
#res1 = df.iloc[:, reversed(range(len(df.columns)))]
# </solution>
printit(res1)


#  2. a SERIES with the last two values from the 'bday' column:
#   2020-01-14    7.11
#   2020-01-15    7.04
res2  = '?'
# <solution>
#res2 = df.iloc[-2:, 0]
# </solution>
printit(res2)

#   3. a DF with the the first two rows of df (and all columns)
#             close  bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
res3  = '?'

# <solution>
#res3 = df.iloc[:2]
# </solution>
printit(res3)


# ----------------------------------------------------------------------------
# DataFrames.iloc using slices
# ----------------------------------------------------------------------------
# Exercise:
# Use .iloc and slices to produce the following objects from df
#   1. a DF with all rows from df except the first one
#   2. a DF (NOT A SERIES) with the last column of df
#   3. a DF with the first two rows of df (using slices, not seq of positions)
#   4. a df with the last 100 (one hundred) rows from df (assume you don't know how many
#       rows the data frame df has)

#   1. a DF with all rows from df except the first one
res1  = '?'
# <solution>
#res1 = df.iloc[1:]
# </solution>
printit(res1)

#   2. a DF (NOT A SERIES) with the last column of df
res2  = '?'
# <solution>
#res2 = df.iloc[:, -1:]
# </solution>
printit(res2)

#   3. a DF with the first two rows of df (using slices, not seq of positions)
res3  = '?'
# <solution>
#res3 = df.iloc[:2]
# </solution>
printit(res3)

#   4. a df with the last 100 (one hundred) rows from df (assume you don't know how many
#       rows the data frame df has)
res4  = '?'
# <solution>
#res4 = df.iloc[-100:]
# </solution>
printit(res4)


# ----------------------------------------------------------------------------
# DataFrames and []
#
# | Selection            | Result | Notes                              |
# |----------------------|--------|------------------------------------|
# | df[colname]          | series | colname must exist                 |
# | df[list of colnames] | df     | All colname must exist             |
# | df[slices]           | df     | Operates on row index, not columns |
# ----------------------------------------------------------------------------

# df[label] --> series with the elements from the COLUMN labeled 'label'
res = '?'
# <solution>
#res  = df['close']
# </solution>
printit(res)

# df[label] -->KeyError if column label not found
#res = df['2020-01-02']


# df[seq of labels] --> DF with the column labels in the order provided
clabel_seq = ['bday', 'close'] 
res = '?'
# <solution>
#res = df[clabel_seq]
# </solution>
printit(res)





