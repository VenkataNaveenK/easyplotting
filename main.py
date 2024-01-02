import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import streamlit as st 
from streamlit_option_menu import option_menu

from seaborn_module.plots import SeabornPlots

# Page configuration
st.set_page_config(
    page_title='EasyPlotting',
    page_icon=':oncoming_automobile:',
    layout='centered'
)

# Side bar
with st.sidebar:
    selected = option_menu(
        menu_title='Seaborn Plots',
        options=['countplot','boxplot','violinplot','stripplot','lmplot'],
        icons=['house','file-earmark-text','body-text','chevron-bar-contract','cloud-check'],
        menu_icon='diagram-3',
        default_index=0
    )

df = sns.load_dataset('tips')
sns_plots = SeabornPlots()
plot_types = ['countplot','boxplot','violinplot','stripplot','lmplot']

if selected == 'boxplot':
    plt, plot_line_text = sns_plots.boxplot(df)
elif selected == 'violinplot':
    plt, plot_line_text = sns_plots.violinplot(df)
elif selected == 'stripplot':
    plt, plot_line_text = sns_plots.stripplot(df)
elif selected == 'countplot':
    plt, plot_line_text = sns_plots.countplot(df)
elif selected == 'lmplot':
    plt, plot_line_text = sns_plots.lmplot(df)
else:
    raise Exception()

st.pyplot(plt)
code=(f"\
      import matplotlib.pyplot as plt\n\
      import seaborn as sns\n\n\
      {plot_line_text}\n\
      ")
st.header("Code:")
st.code(code, language='python')