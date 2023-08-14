# Pandas Visuals
#
# @author: Dr Musashi Jacobs-Harukawa
# @date: 12-08-2023

# %% Imports
import pandas as pd
from uuid import uuid4
from dataclasses import dataclass
from typing import Optional, Iterable

# %% Styling utils
@dataclass
class ColorTheme:
    fg: str
    bg: str
    sel: str
    ln: str
    cm: str
    win: str
    r: str
    o: str
    y: str
    g: str
    a: str
    b: str
    p: str
    border: str

# Tomorrow theme: https://github.com/chriskempson/tomorrow-theme
theme = ColorTheme(**dict(
    fg   = "4d4d4c", bg   = "ffffff", sel  = "d6d6d6", ln   = "efefef",
    cm   = "8e908c", win  = "efefef", r    = "c82829",
    o    = "f5871f", y    = "eab700", g    = "718c00", a    = "3e999f",
    b    = "4271ae", p    = "8959a8",
    border = "4d4d4c"
))

# Define styles
styles = {
    'base': lambda x: f"background-color: #{theme.bg}; color: #{theme.fg}",
    'hl1':  lambda x: f"background-color: #{theme.g}; color: #{theme.bg}",
    'hl2':  lambda x: f"background-color: #{theme.cm}; color: #{theme.fg}",
    'll1':  lambda x: f"background-color: #{theme.ln}; color: #{theme.sel}",
    'idxn': lambda x: f"background-color: #{theme.sel}; color: #{theme.fg}",
}

    

#  Reset utility to base theme
def reset_style(df, base_style=styles['base']):
    df = df.applymap(base_style)
    df = df.applymap_index(base_style, axis=0)
    df = df.applymap_index(base_style, axis=1)
    # Reset uuid
    df.set_uuid(str(uuid4())[:8])
    (
    df.applymap(lambda x: styles['ll1'](x) + f"border-right: 1px solid {theme.border}; font-weight: bold",
                subset=df.columns[0])
    .applymap_index(lambda x:
                    styles['idxn'](x) + f"border-right: 1px solid {theme.border}; border-bottom: 2px solid {theme.border};"
                        if x==df.columns[0] else
                    styles['ll1'](x) + f"border-bottom: 1px solid {theme.border};"
                    , axis=1)
    )
    return df

# %% Read in data
df_scores = pd.read_csv('data/scores.csv')
fake_index = pd.Series(index=df_scores.loc[:, df_scores.columns[0]],
                       data=df_scores.index)

df = df_scores.style
df.set_uuid('0')
reset_style(df)
df.hide(names=False)
df.to_html('figures/pandas_base.html')

# Give borders
# df.applymap(
#     lambda x: "border-right: 1px solid {theme.border}; font-weight: bold;",
#     subset=pd.IndexSlice[:, df.columns[0]])
# df.applymap_index(lambda x:
#                   "border-right: 1px solid {theme.border}; border-bottom: 1px solid {theme.border};"
#                   if x==df.columns[0] else "border-bottom: 1px solid {theme.border};",
#                   axis=1)

# df.to_html('test.html')

# %% Function
def loc_highlighter(
        df: pd.io.formats.style.Styler,
        idxs: Optional[Iterable]=None,
        cols: Optional[Iterable]=None,
        ) -> pd.io.formats.style.Styler:
    reset_style(df)

    # Get the right index
    if idxs is None:
        idxs = fake_index
    else:
        idxs = fake_index[idxs]
    if cols is None:
        cols = df.columns[1:]
    # Build it
    return (
    df.applymap(styles['ll1']) # LL all
    .applymap(styles['base'],  # ML selected idxs
              subset=pd.IndexSlice[idxs, df.columns[1:]])
    .applymap(styles['base'],  # ML selected cols
              subset=pd.IndexSlice[:, cols])
    .applymap(styles['hl1'],   # HL selected elements
              subset=pd.IndexSlice[idxs, cols])
    .applymap(lambda x: # Color fake index
              (styles['hl2'](x)
                if x in fake_index[idxs].index
                else styles['ll1'](x)
                ) + f"border-right: 1px solid {theme.border}; font-weight: bold;",
              subset=df.columns[0])
    .applymap_index(lambda x:
                    styles['idxn'](x) + f"border-right: 1px solid {theme.border}; border-bottom: 2px solid {theme.border};"
                        if x==df.columns[0] else
                    styles['hl2'](x) + f"border-bottom: 1px solid {theme.border};"
                        if x in cols else
                    styles['ll1'](x) + f"border-bottom: 1px solid {theme.border};"
                    , axis=1)
    )



# %% Base look
df.to_html('figures/pandas_base.html')
# %%
loc_highlighter(df, ['5a01']).to_html('figures/pandas_loc_row.html')
loc_highlighter(df, cols=['history']).to_html('figures/pandas_loc_col.html')
loc_highlighter(df, ['5a01', '5a12']).to_html('figures/pandas_loc_multi_row.html')
loc_highlighter(df, cols=['art', 'history']).to_html('figures/pandas_loc_multi_col.html')
loc_highlighter(df, ['5a01'], ['history']).to_html('figures/pandas_loc_cell.html')
loc_highlighter(df, ['5a12'], ['history', 'art']).to_html('figures/pandas_loc_multi1.html')
loc_highlighter(df, ['5a01', '5a12', '5b05'], ['biology', 'art']).to_html('figures/pandas_loc_multi2.html')
loc_highlighter(df, ['5a01', '5b05', '5e04'], ['math', 'history', 'art']).to_html('figures/pandas_loc_multi3.html')


# %% Make a bunch
loc_highlighter(df, [0]).to_html('figures/pandas_loc_row.html')
loc_highlighter(df, cols=['history']).to_html('figures/pandas_loc_col.html')
loc_highlighter(df, [0], ['history']).to_html('figures/pandas_loc_cell.html')
loc_highlighter(df, [1], ['history', 'art']).to_html('figures/pandas_loc_multi1.html')
loc_highlighter(df, [0, 1, 2], ['biology', 'art']).to_html('figures/pandas_loc_multi2.html')
loc_highlighter(df, [0, 2, 4], ['math', 'history', 'art']).to_html('figures/pandas_loc_multi3.html')


# %% Change index to be 'student_id'
df_scores.set_index('student_id', inplace=True)
df_scores.index.name=None
df = df_scores.style
reset_style(df)
loc_highlighter(df, [101, 102], ['history']).to_html('figures/pandas_loc_new_index.html', table_uuid='7')

# %%


# %% GRAVEYARD
# %% loc row
reset_style(df)
(
df.applymap(styles['ll1'])
  .applymap(styles['hl1'], subset=pd.IndexSlice[0,:])
  .applymap_index(lambda x: styles['hl2'](x) if x==0 else styles['ll1'](x), axis=0)
  .applymap_index(styles['hl2'], axis=1)
)

# %% loc col
reset_style(df)
(
df.applymap(styles['ll1'])
  .applymap(styles['hl1'], subset=pd.IndexSlice[:, 'history'])
  .applymap_index(styles['hl2'], axis=0)
  .applymap_index(lambda x: styles['hl2'](x) if x=='history' else styles['ll1'](x), axis=1)
)

# %% loc single cell
reset_style(df)
(
df.applymap(styles['ll1'])
  .applymap(styles['base'], subset=pd.IndexSlice[0, :])
  .applymap(styles['base'], subset=pd.IndexSlice[:, 'history'])
  .applymap(styles['hl1'], subset=pd.IndexSlice[0, 'history'])
  .applymap_index(lambda x: styles['hl2'](x) if x==0 else styles['ll1'](x), axis=0)
  .applymap_index(lambda x: styles['hl2'](x) if x=='history' else styles['ll1'](x), axis=1)
)

# %% df.loc[0, ['history, 'biology']]
reset_style(df)
(
df.applymap(styles['ll1'])
  .applymap(styles['base'], subset=pd.IndexSlice[0,:])
  .applymap(styles['base'], subset=pd.IndexSlice[:, ['history', 'biology']])
  .applymap(styles['hl1'], subset=pd.IndexSlice[0, ['history', 'biology']])
  .applymap_index(lambda x: styles['hl2'](x) if x==0 else styles['ll1'](x), axis=0)
  .applymap_index(lambda x: styles['hl2'](x) if x in ['history', 'biology'] else styles['ll1'](x), axis=1)
)

# %% df.loc[:3, 'english':] 
reset_style(df)
(
df.applymap(styles['ll1'])
  .applymap(styles['base'], subset=pd.IndexSlice[1:3, :])
  .applymap(styles['base'], subset=pd.IndexSlice[:, 'english':])
  .applymap(styles['hl1'], subset=pd.IndexSlice[1:3, 'english':])
  .applymap_index(lambda x: styles['hl2'](x) if x in df.index[1:4] else styles['ll1'](x), axis=0)
  .applymap_index(lambda x: styles['hl2'](x) if x in df.columns[2:] else styles['ll1'](x), axis=1)
)

# %% df.loc[[0, 2, 4], ['math', 'biology']] 
reset_style(df)
idxs = [0, 2, 4]; cols=['math', 'biology']
(
df.applymap(styles['ll1'])
  .applymap(styles['base'], subset=pd.IndexSlice[idxs, :])
  .applymap(styles['base'], subset=pd.IndexSlice[:, cols])
  .applymap(styles['hl1'], subset=pd.IndexSlice[idxs, cols])
  .applymap_index(lambda x: styles['hl2'](x) if x in idxs else styles['ll1'](x), axis=0)
  .applymap_index(lambda x: styles['hl2'](x) if x in cols else styles['ll1'](x), axis=1)
)

# %% Highlight index
(
df.applymap_index(styles['hl1'], axis=0)
  .applymap_index(styles['ll1'], axis=1)
  .applymap(styles['ll1'])
)#.to_html('figures/pandas_index.html')

# %% Highlight columns
reset_style(df)
(
df.applymap_index(styles['ll1'], axis=0)
  .applymap_index(styles['hl1'], axis=1)
  .applymap(styles['ll1'])
)#.to_html('figures/pandas_columns.html')

# df = df_scores.copy()
# idxs = ['5a01', '5a12', '5b05']
# df.loc[fake_index[idxs], :]
# fake_index[idxs]
