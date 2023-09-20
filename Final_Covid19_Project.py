

from dash.dependencies import Input, Output
import webbrowser
import datetime
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import sys
import plotly as p
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pylab as plt1
import dash
import dash_core_components as dcc
import dash_html_components as html


boss_size=1600
boss_height=800
#reading the csv file
df = pd.read_csv("covid_de.csv")
pdf = pd.read_csv("demographics_de.csv")
#extracting column data's
pdf1 = pdf['state']
pdf2 = pdf['population']

df1 = df['state']
df2 = df['cases']
df3 = df['deaths']
df4 = df['recovered']
df5 = df['date']

name = np.unique(df1)
#intialising the array indices with 0
countcase = [0] * 16
countdeath = [0] * 16
countrecovered = [0] * 16
countpopulation = [0] * 16


#classifying the total cases,total deaths and total recovered for each state
for i in range(len(df1)):
    if df1[i] == 'Baden-Wuerttemberg':
        countcase[0] += df2[i]
        countdeath[0] += df3[i]
        countrecovered[0] += df4[i]
    if df1[i] == 'Bayern':
        countcase[1] += df2[i]
        countdeath[1] += df3[i]
        countrecovered[1] += df4[i]
    if df1[i] == 'Berlin':
        countcase[2] += df2[i]
        countdeath[2] += df3[i]
        countrecovered[2] += df4[i]
    if df1[i] == 'Brandenburg':
        countcase[3] += df2[i]
        countdeath[3] += df3[i]
        countrecovered[3] += df4[i]
    if df1[i] == 'Bremen':
        countcase[4] += df2[i]
        countdeath[4] += df3[i]
        countrecovered[4] += df4[i]
    if df1[i] == 'Hamburg':
        countcase[5] += df2[i]
        countdeath[5] += df3[i]
        countrecovered[5] += df4[i]
    if df1[i] == 'Hessen':
        countcase[6] += df2[i]
        countdeath[6] += df3[i]
        countrecovered[6] += df4[i]
    if df1[i] == 'Mecklenburg-Vorpommern':
        countcase[7] += df2[i]
        countdeath[7] += df3[i]
        countrecovered[7] += df4[i]
    if df1[i] == 'Niedersachsen':
        countcase[8] += df2[i]
        countdeath[8] += df3[i]
        countrecovered[8] += df4[i]
    if df1[i] == 'Nordrhein-Westfalen':
        countcase[9] += df2[i]
        countdeath[9] += df3[i]
        countrecovered[9] += df4[i]
    if df1[i] == 'Rheinland-Pfalz':
        countcase[10] += df2[i]
        countdeath[10] += df3[i]
        countrecovered[10] += df4[i]
    if df1[i] == 'Saarland':
        countcase[11] += df2[i]
        countdeath[11] += df3[i]
        countrecovered[11] += df4[i]
    if df1[i] == 'Sachsen':
        countcase[12] += df2[i]
        countdeath[12] += df3[i]
        countrecovered[12] += df4[i]
    if df1[i] == 'Sachsen-Anhalt':
        countcase[13] += df2[i]
        countdeath[13] += df3[i]
        countrecovered[13] += df4[i]
    if df1[i] == 'Schleswig-Holstein':
        countcase[14] += df2[i]
        countdeath[14] += df3[i]
        countrecovered[14] += df4[i]
    if df1[i] == 'Thueringen':
        countcase[15] += df2[i]
        countdeath[15] += df3[i]
        countrecovered[15] += df4[i]

k1 = np.unique(df5)

State1 = name[0] * len(k1)
State2 = name[1] * len(k1)
State3 = name[2] * len(k1)
State4 = name[3] * len(k1)
State5 = name[4] * len(k1)
State6 = name[5] * len(k1)
State7 = name[6] * len(k1)
State8 = name[7] * len(k1)
State9 = name[8] * len(k1)
State10 = name[9] * len(k1)
State11 = name[10] * len(k1)
State12 = name[11] * len(k1)
State13 = name[12] * len(k1)
State14 = name[13] * len(k1)
State15 = name[14] * len(k1)
State16 = name[15] * len(k1)

percountcase1 = [0] * len(k1)
percountdeath1 = [0] * len(k1)
percountrecovered1 = [0] * len(k1)

percountcase2 = [0] * len(k1)
percountdeath2 = [0] * len(k1)
percountrecovered2 = [0] * len(k1)

percountcase3 = [0] * len(k1)
percountdeath3 = [0] * len(k1)
percountrecovered3 = [0] * len(k1)

percountcase4 = [0] * len(k1)
percountdeath4 = [0] * len(k1)
percountrecovered4 = [0] * len(k1)

percountcase5 = [0] * len(k1)
percountdeath5 = [0] * len(k1)
percountrecovered5 = [0] * len(k1)

percountcase6 = [0] * len(k1)
percountdeath6 = [0] * len(k1)
percountrecovered6 = [0] * len(k1)

percountcase7 = [0] * len(k1)
percountdeath7 = [0] * len(k1)
percountrecovered7 = [0] * len(k1)

percountcase8 = [0] * len(k1)
percountdeath8 = [0] * len(k1)
percountrecovered8 = [0] * len(k1)

percountcase9 = [0] * len(k1)
percountdeath9 = [0] * len(k1)
percountrecovered9 = [0] * len(k1)

percountcase10 = [0] * len(k1)
percountdeath10 = [0] * len(k1)
percountrecovered10 = [0] * len(k1)

percountcase11 = [0] * len(k1)
percountdeath11 = [0] * len(k1)
percountrecovered11 = [0] * len(k1)

percountcase12 = [0] * len(k1)
percountdeath12 = [0] * len(k1)
percountrecovered12 = [0] * len(k1)

percountcase13 = [0] * len(k1)
percountdeath13 = [0] * len(k1)
percountrecovered13 = [0] * len(k1)

percountcase14 = [0] * len(k1)
percountdeath14 = [0] * len(k1)
percountrecovered14 = [0] * len(k1)

percountcase15 = [0] * len(k1)
percountdeath15 = [0] * len(k1)
percountrecovered15 = [0] * len(k1)

percountcase16 = [0] * len(k1)
percountdeath16 = [0] * len(k1)
percountrecovered16 = [0] * len(k1)
#classifying the total cases,total deaths and total recovered for each state per day
for i in range(len(df1)):
    s = list(k1).index(df5[i])
    if df1[i] == 'Baden-Wuerttemberg':
        percountcase1[s] += df2[i]
        percountdeath1[s] += df3[i]
        percountrecovered1[s] += df4[i]

    if df1[i] == 'Bayern':
        percountcase2[s] += df2[i]
        percountdeath2[s] += df3[i]
        percountrecovered2[s] += df4[i]

    if df1[i] == 'Berlin':
        percountcase3[s] += df2[i]
        percountdeath3[s] += df3[i]
        percountrecovered3[s] += df4[i]
    if df1[i] == 'Brandenburg':
        percountcase4[s] += df2[i]
        percountdeath4[s] += df3[i]
        percountrecovered4[s] += df4[i]
    if df1[i] == 'Bremen':
        percountcase5[s] += df2[i]
        percountdeath5[s] += df3[i]
        percountrecovered5[s] += df4[i]
    if df1[i] == 'Hamburg':
        percountcase6[s] += df2[i]
        percountdeath6[s] += df3[i]
        percountrecovered6[s] += df4[i]
    if df1[i] == 'Hessen':
        percountcase7[s] += df2[i]
        percountdeath7[s] += df3[i]
        percountrecovered7[s] += df4[i]
    if df1[i] == 'Mecklenburg-Vorpommern':
        percountcase8[s] += df2[i]
        percountdeath8[s] += df3[i]
        percountrecovered8[s] += df4[i]
    if df1[i] == 'Niedersachsen':
        percountcase9[s] += df2[i]
        percountdeath9[s] += df3[i]
        percountrecovered9[s] += df4[i]
    if df1[i] == 'Nordrhein-Westfalen':
        percountcase10[s] += df2[i]
        percountdeath10[s] += df3[i]
        percountrecovered10[s] += df4[i]
    if df1[i] == 'Rheinland-Pfalz':
        percountcase11[s] += df2[i]
        percountdeath11[s] += df3[i]
        percountrecovered11[s] += df4[i]
    if df1[i] == 'Saarland':
        percountcase12[s] += df2[i]
        percountdeath12[s] += df3[i]
        percountrecovered12[s] += df4[i]
    if df1[i] == 'Sachsen':
        percountcase13[s] += df2[i]
        percountdeath13[s] += df3[i]
        percountrecovered13[s] += df4[i]
    if df1[i] == 'Sachsen-Anhalt':
        percountcase14[s] += df2[i]
        percountdeath14[s] += df3[i]
        percountrecovered14[s] += df4[i]
    if df1[i] == 'Schleswig-Holstein':
        percountcase15[s] += df2[i]
        percountdeath15[s] += df3[i]
        percountrecovered15[s] += df4[i]
    if df1[i] == 'Thueringen':
        percountcase16[s] += df2[i]
        percountdeath16[s] += df3[i]
        percountrecovered16[s] += df4[i]

case_list=[percountcase1,percountcase2,percountcase3,percountcase4,percountcase5,percountcase6,percountcase7,percountcase8,percountcase9,percountcase10,percountcase11,percountcase12,percountcase13,percountcase14,percountcase15,percountcase16]

s_name=['Baden-Wuerttemberg','Bayern','Berlin','Brandenburg','Bremen','Hamburg','Hessen','Mecklenburg-Vorpommern','Niedersachsen','Nordrhein-Westfalen','Rheinland-Pfalz','Saarland','Sachsen','Sachsen-Anhalt','Schleswig-Holstein','Thueringen']




numdays=147
base = datetime.datetime(2020, 1, 28)
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]

#animation 1###################################################################33

sliders_dict = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "Date:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 300, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 50},
    "len": 0.9,
    "x": 0.1,
    "y": 0,
    "steps": []
}

traces=[]
for i in range(16):
    a=go.Scatter(x=k1,y=case_list[i],
                    mode='lines',name=s_name[i],
                    line=dict(width=1.5))
    traces.append(a)

for i in k1:
    
    slider_step = {"args": [
        [i],
        {"frame": {"duration": 0, "redraw": True},
          "mode": "immediate",
          "transition": {"duration": 0}}
    ],
        "label": i,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)
    
low=len(k1)

frames = [dict(data= [dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase1[:k+1],
                       name = "Baden-Wuerttemberg"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase2[:k+1],
                           name = "Bayern"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase3[:k+1],
                           name= "Berlin"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase4[:k+1],
                           name = "Brandenburg"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase5[:k+1],
                           name = "Bremen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase6[:k+1],
                           name = "Hamburg"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase7[:k+1],
                           name = "Hessen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase8[:k+1],
                           name = "Mecklenburg-Vorpommern"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase9[:k+1],
                           name = "Niedersachsen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase10[:k+1],
                           name = "Nordrhein-Westfalen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase11[:k+1],
                           name = "Rheinland-Pfalz"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase12[:k+1],
                           name = "Saarland"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase13[:k+1],
                           name = "Sachsen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase14[:k+1],
                           name = "Sachsen-Anhalt"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase15[:k+1],
                           name = "Schleswig-Holstein"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase16[:k+1],
                           name = "Thueringen")],
               traces= [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],  #this means that  frames[k]['data'][0]  updates trace1, and   frames[k]['data'][1], trace2 
              )for k  in  range(0, low-1)] 

layout = go.Layout(width=boss_size,
                   height=boss_height,
                   showlegend=True,
                   hovermode='closest',
                   updatemenus=[dict(type='buttons', showactive=False,
                                y=1.05,
                                x=1.15,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, 
                                                    dict(frame=dict(duration=2, 
                                                                    redraw=False),
                                                         transition=dict(duration=0),
                                                         fromcurrent=True,
                                                         mode='immediate')])])])


layout.update(xaxis =dict(range=[min(date_list), max(date_list)], autorange=False),
              yaxis =dict(autorange=True));

fig_dict = {
    "data": traces,
    "layout": layout,
    "frames": frames
    
}
fig_dict["layout"]["sliders"] = [sliders_dict]
fig_dict["layout"]["updatemenus"] = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 100, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 300,
                                                                    "easing": "quadratic-in-out"}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }
]
annotations=[]
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Cases in Fedral State of Germany',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: The Robert Koch Institute' +
                                   'government’s central scientific institution',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))



fig1 = go.Figure(fig_dict)
fig1.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
fig1.update_layout(
    
    
    yaxis_title="Number of Cases",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)
fig1.update_layout(annotations=annotations)


#animation 2####################################################################
death_list=[percountdeath1,percountdeath2,percountdeath3,percountdeath4,percountdeath5,percountdeath6,percountdeath7,percountdeath8,percountdeath9,percountdeath10,percountdeath11,percountdeath12,percountdeath13,percountdeath13,percountdeath14,percountdeath15,percountdeath16]

sliders_dict = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "Date:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 300, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 50},
    "len": 0.9,
    "x": 0.1,
    "y": 0,
    "steps": []
}

traces=[]
for i in range(16):
    a=go.Scatter(x=k1,y=death_list[i],
                    mode='lines',name=s_name[i],
                    line=dict(width=1.5))
    traces.append(a)

for i in k1:
    
    slider_step = {"args": [
        [i],
        {"frame": {"duration": 0, "redraw": True},
          "mode": "immediate",
          "transition": {"duration": 0}}
    ],
        "label": i,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)
    
low=len(k1)

frames = [dict(data= [dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath1[:k+1],
                       name = "Baden-Wuerttemberg"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath2[:k+1],
                           name = "Bayern"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath3[:k+1],
                           name= "Berlin"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath4[:k+1],
                           name = "Brandenburg"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath5[:k+1],
                           name = "Bremen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath6[:k+1],
                           name = "Hamburg"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath7[:k+1],
                           name = "Hessen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath8[:k+1],
                           name = "Mecklenburg-Vorpommern"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath9[:k+1],
                           name = "Niedersachsen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath10[:k+1],
                           name = "Nordrhein-Westfalen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath11[:k+1],
                           name = "Rheinland-Pfalz"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath12[:k+1],
                           name = "Saarland"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath13[:k+1],
                           name = "Sachsen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath14[:k+1],
                           name = "Sachsen-Anhalt"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountdeath15[:k+1],
                           name = "Schleswig-Holstein"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountcase16[:k+1],
                           name = "Thueringen")],
               traces= [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],  #this means that  frames[k]['data'][0]  updates trace1, and   frames[k]['data'][1], trace2 
              )for k  in  range(0, low-1)] 

layout = go.Layout(width=boss_size,
                   height=boss_height,
                   showlegend=True,
                   hovermode='closest',
                   updatemenus=[dict(type='buttons', showactive=False,
                                y=1.05,
                                x=1.15,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, 
                                                    dict(frame=dict(duration=2, 
                                                                    redraw=False),
                                                         transition=dict(duration=0),
                                                         fromcurrent=True,
                                                         mode='immediate')])])])


layout.update(xaxis =dict(range=[min(date_list), max(date_list)], autorange=False),
              yaxis =dict(autorange=True));

fig_dict = {
    "data": traces,
    "layout": layout,
    "frames": frames
    
}
fig_dict["layout"]["sliders"] = [sliders_dict]
fig_dict["layout"]["updatemenus"] = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 100, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 300,
                                                                    "easing": "quadratic-in-out"}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }
]
annotations=[]
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Death Cases in Fedral States of Germany',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: The Robert Koch Institute' +
                                   'government’s central scientific institution',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))



fig2 = go.Figure(fig_dict)
fig2.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
fig2.update_layout(
    
    
    yaxis_title="Number of Cases",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)
fig2.update_layout(annotations=annotations)

####animation 3############################
rec_list=[percountrecovered1,percountrecovered2,percountrecovered3,percountrecovered4,percountrecovered5,percountrecovered6,percountrecovered7,percountrecovered8,percountrecovered9,percountrecovered10,percountrecovered11,percountrecovered12,percountrecovered13,percountrecovered14,percountrecovered15,percountrecovered16]

sliders_dict = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "Date:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 300, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 50},
    "len": 0.9,
    "x": 0.1,
    "y": 0,
    "steps": []
}

traces=[]
for i in range(16):
    a=go.Scatter(x=k1,y=rec_list[i],
                    mode='lines',name=s_name[i],
                    line=dict(width=1.5))
    traces.append(a)

for i in k1:
    
    slider_step = {"args": [
        [i],
        {"frame": {"duration": 0, "redraw": True},
          "mode": "immediate",
          "transition": {"duration": 0}}
    ],
        "label": i,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)
    
low=len(k1)

frames = [dict(data= [dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered1[:k+1],
                       name = "Baden-Wuerttemberg"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered2[:k+1],
                           name = "Bayern"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered3[:k+1],
                           name= "Berlin"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered4[:k+1],
                           name = "Brandenburg"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered5[:k+1],
                           name = "Bremen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered6[:k+1],
                           name = "Hamburg"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered7[:k+1],
                           name = "Hessen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered8[:k+1],
                           name = "Mecklenburg-Vorpommern"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered9[:k+1],
                           name = "Niedersachsen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered10[:k+1],
                           name = "Nordrhein-Westfalen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered11[:k+1],
                           name = "Rheinland-Pfalz"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered12[:k+1],
                           name = "Saarland"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered13[:k+1],
                           name = "Sachsen"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered14[:k+1],
                           name = "Sachsen-Anhalt"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered15[:k+1],
                           name = "Schleswig-Holstein"),
                      dict(type='scatter',
                           x=k1[:k+1],
                           y=percountrecovered16[:k+1],
                           name = "Thueringen")],
               traces= [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],   
              )for k  in  range(0, low-1)] 

layout = go.Layout(width=boss_size,
                   height=boss_height,
                   showlegend=True,
                   hovermode='closest',
                   updatemenus=[dict(type='buttons', showactive=False,
                                y=1.05,
                                x=1.15,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, 
                                                    dict(frame=dict(duration=2, 
                                                                    redraw=False),
                                                         transition=dict(duration=0),
                                                         fromcurrent=True,
                                                         mode='immediate')])])])


layout.update(xaxis =dict(range=[min(date_list), max(date_list)], autorange=False),
              yaxis =dict(autorange=True));

fig_dict = {
    "data": traces,
    "layout": layout,
    "frames": frames
    
}
fig_dict["layout"]["sliders"] = [sliders_dict]
fig_dict["layout"]["updatemenus"] = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 100, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 300,
                                                                    "easing": "quadratic-in-out"}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }
]
annotations=[]
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Recovered Cases in Fedral States of Germany',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: The Robert Koch Institute' +
                                   'government’s central scientific institution',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))


#### line graph########################################
fig3 = go.Figure(fig_dict)
fig3.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
fig3.update_layout(
    
    
    yaxis_title="Number of Cases",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)
fig3.update_layout(annotations=annotations)

###Combine Line graphs

fig6=go.Figure()

#active cases on the latest date
active = [percountcase1[130], percountcase2[130], percountcase3[130], percountcase4[130], percountcase5[130],
          percountcase6[130], percountcase7[130], percountcase8[130], percountcase8[130], percountcase9[130],
          percountcase10[130], percountcase11[130], percountcase12[130], percountcase13[130], percountcase14[130],
          percountcase14[130], percountcase15[130], percountcase16[130]]

sum = 0
sum1 = 0
sum2 = 0
for i in range(0, 15):
    sum += countcase[i]
    sum1 += countrecovered[i]
    sum2 += countdeath[i]
#for getting total active cases
sum = sum - (sum1+sum2)
#collecting the data for geom_bar
total_deaths = []
total_recovered = []
for i in range(len(name)):
    
    
    total_deaths.append(countdeath[i])
    total_recovered.append(countrecovered[i])
a_sum=d_sum=r_sum=0
for i in range(len(name)):
    a_sum+=active[i]
    d_sum+=total_deaths[i]
    r_sum+=total_recovered[i]
#implementation of geom_bar
fig6 = go.Figure(
    go.Bar(x=s_name, y=total_deaths, name='Total Deaths '+str(sum2), marker_color='red', text=total_deaths))

fig6.add_trace(go.Bar(x=s_name, y=total_recovered, name='Total Recovered '+str(sum1), marker_color='green', text=total_recovered
                      ))
fig6.add_trace(go.Bar(x=s_name, y=active, name='New Cases '+str(sum), marker_color='yellow', text=active ))

fig6.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
fig6.update_layout(title_text='Status on 22nd June : Latest')
fig6.update_layout(height=800)

fig6.update_traces(hovertemplate='State : %{x} <br>Cases: %{y}') 
fig6.update_layout(
    
    
    yaxis_title="Number of Cases",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

app = dash.Dash()



app.layout = html.Div([
    html.H1(
        children='COVID-19 Dashboard : Germany',
        style={
            'textAlign': 'center'}
    ),
    dcc.Tabs(id="tabs", value="tab-1", children=[
        dcc.Tab(label='Total Cases', value='tab-1'),
        dcc.Tab(label='Deaths', value='tab-2'),
        dcc.Tab(label='Recovered', value='tab-3'),
        dcc.Tab(label='Latest', value='tab-4')
    ]),
    html.Div(id="tabs-content")
])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([dcc.Graph(id='fig1', figure=fig1)])
    elif tab == 'tab-2':
        return html.Div([dcc.Graph(id='fig2', figure=fig2)])
    elif tab == 'tab-3':
        return html.Div([dcc.Graph(id='fig3', figure=fig3)])
    elif tab == 'tab-4':
        return html.Div([dcc.Graph(id='fig6', figure=fig6)])


if __name__ == '__main__':
    app.run_server(port=8000, host='127.0.0.1')