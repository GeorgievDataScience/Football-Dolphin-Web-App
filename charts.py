import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json




def vertical_bar_chart(dataFrame):
    label_title = pd.DataFrame(dataFrame.pop(dataFrame.columns[0])).to_string(index=False)    
    label_x = pd.DataFrame(dataFrame.pop(dataFrame.columns[0])).to_string(index=False)
    
    fig = plt.figure(figsize=(9,7))
    sns.set_theme(style="white")
    ax = sns.barplot( data=dataFrame)
    ax.bar_label(ax.containers[0])
    ax.set_xlabel(label_x, fontsize = 10)
    ax.set(title=label_title)
    return fig



def horizontal_bar_chart(dataFrame):
    label_title = pd.DataFrame(dataFrame.pop(dataFrame.columns[0])).to_string(index=False)    
    label_x = pd.DataFrame(dataFrame.pop(dataFrame.columns[0])).to_string(index=False)
    
    fig = plt.figure(figsize=(9,9))
    sns.set_theme(style="white")
    ax = sns.barplot( data=dataFrame, orient = 'h')
    ax.bar_label(ax.containers[0])
    ax.set_xlabel(label_x, fontsize = 10)
    #ax.set(title=label_title)
    ax.set(title=label_title)
    return fig


