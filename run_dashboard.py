import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.figure_factory as ff

# Load the data
df = pd.read_csv('german_credit_data.csv')
print(f'Data loaded: {df.shape[0]} rows, {df.shape[1]} columns')

# Data preprocessing
df_clean = df.copy()
df_clean['Saving accounts'] = df_clean['Saving accounts'].fillna('unknown')
df_clean['Checking account'] = df_clean['Checking account'].fillna('unknown')
df_clean['Age_Group'] = pd.cut(df_clean['Age'], bins=[0, 25, 35, 45, 55, 100], 
                               labels=['18-25', '26-35', '36-45', '46-55', '55+'])
df_clean['Credit_Amount_Group'] = pd.cut(df_clean['Credit amount'], bins=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])

# Define color scheme
COLORS = {
    'background': '#1a1a1a',
    'paper': '#2d2d2d',
    'text': '#f5f5f5',
    'primary': '#4a90e2',
    'secondary': '#7b68ee',
    'accent': '#ff6b6b',
    'success': '#51cf66',
    'warning': '#ffd43b',
    'grid': '#404040',
    'hover': '#3d3d3d'
}

CHART_COLORS = ['#4a90e2', '#7b68ee', '#ff6b6b', '#51cf66', '#ffd43b', '#ff8cc8', '#06d6a0', '#f72585']

LAYOUT_TEMPLATE = {
    'plot_bgcolor': COLORS['background'],
    'paper_bgcolor': COLORS['paper'],
    'font': {'color': COLORS['text'], 'family': 'Arial, sans-serif'},
    'xaxis': {
        'gridcolor': COLORS['grid'],
        'color': COLORS['text'],
        'showgrid': True
    },
    'yaxis': {
        'gridcolor': COLORS['grid'],
        'color': COLORS['text'],
        'showgrid': True
    },
    'title': {'font': {'size': 20, 'color': COLORS['text']}},
    'legend': {'font': {'color': COLORS['text']}},
    'margin': {'l': 60, 'r': 60, 't': 80, 'b': 60}
}

# Initialize Dash app
app = dash.Dash(__name__)

# Dashboard layout
app.layout = html.Div([
    html.H1('Credit Risk Dashboard', 
            style={'textAlign': 'center', 'color': COLORS['text'], 
                   'backgroundColor': COLORS['background'], 'padding': '20px',
                   'margin': '0', 'fontFamily': 'Arial, sans-serif'}),
    
    # Key metrics row
    html.Div([
        html.Div([
            html.H3(f'{len(df_clean)}', style={'color': COLORS['primary'], 'margin': '0', 'fontSize': '36px'}),
            html.P('Total Records', style={'color': COLORS['text'], 'margin': '0'})
        ], style={'textAlign': 'center', 'backgroundColor': COLORS['paper'], 
                 'padding': '20px', 'margin': '10px', 'borderRadius': '8px',
                 'flex': '1'}),
        
        html.Div([
            html.H3(f'${df_clean["Credit amount"].mean():.0f}', style={'color': COLORS['success'], 'margin': '0', 'fontSize': '36px'}),
            html.P('Avg Credit Amount', style={'color': COLORS['text'], 'margin': '0'})
        ], style={'textAlign': 'center', 'backgroundColor': COLORS['paper'], 
                 'padding': '20px', 'margin': '10px', 'borderRadius': '8px',
                 'flex': '1'}),
        
        html.Div([
            html.H3(f'{df_clean["Duration"].mean():.0f}', style={'color': COLORS['warning'], 'margin': '0', 'fontSize': '36px'}),
            html.P('Avg Duration (months)', style={'color': COLORS['text'], 'margin': '0'})
        ], style={'textAlign': 'center', 'backgroundColor': COLORS['paper'], 
                 'padding': '20px', 'margin': '10px', 'borderRadius': '8px',
                 'flex': '1'}),
        
        html.Div([
            html.H3(f'{df_clean["Age"].mean():.0f}', style={'color': COLORS['accent'], 'margin': '0', 'fontSize': '36px'}),
            html.P('Avg Age', style={'color': COLORS['text'], 'margin': '0'})
        ], style={'textAlign': 'center', 'backgroundColor': COLORS['paper'], 
                 'padding': '20px', 'margin': '10px', 'borderRadius': '8px',
                 'flex': '1'})
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'margin': '20px 0'}),
    
    # Charts grid
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(id='age-sex-chart')
            ], style={'width': '48%', 'display': 'inline-block', 'margin': '1%'}),
            
            html.Div([
                dcc.Graph(id='purpose-pie-chart')
            ], style={'width': '48%', 'display': 'inline-block', 'margin': '1%'})
        ]),
        
        html.Div([
            html.Div([
                dcc.Graph(id='credit-amount-chart')
            ], style={'width': '48%', 'display': 'inline-block', 'margin': '1%'}),
            
            html.Div([
                dcc.Graph(id='housing-job-chart')
            ], style={'width': '48%', 'display': 'inline-block', 'margin': '1%'})
        ]),
        
        html.Div([
            html.Div([
                dcc.Graph(id='savings-checking-chart')
            ], style={'width': '48%', 'display': 'inline-block', 'margin': '1%'}),
            
            html.Div([
                dcc.Graph(id='duration-amount-scatter')
            ], style={'width': '48%', 'display': 'inline-block', 'margin': '1%'})
        ])
    ])
], style={'backgroundColor': COLORS['background'], 'minHeight': '100vh', 'padding': '0', 'margin': '0'})

# Callbacks for updating charts
@app.callback(
    [Output('age-sex-chart', 'figure'),
     Output('purpose-pie-chart', 'figure'),
     Output('credit-amount-chart', 'figure'),
     Output('housing-job-chart', 'figure'),
     Output('savings-checking-chart', 'figure'),
     Output('duration-amount-scatter', 'figure')],
    [Input('age-sex-chart', 'id')]
)
def update_charts(_):
    # Age by Sex chart
    age_sex_counts = df_clean.groupby(['Age_Group', 'Sex']).size().reset_index(name='Count')
    fig1 = px.bar(age_sex_counts, x='Age_Group', y='Count', color='Sex',
                  title='Age Distribution by Gender',
                  color_discrete_sequence=CHART_COLORS)
    fig1.update_layout(**LAYOUT_TEMPLATE)
    
    # Purpose pie chart
    purpose_counts = df_clean['Purpose'].value_counts()
    fig2 = px.pie(values=purpose_counts.values, names=purpose_counts.index,
                  title='Loan Purpose Distribution',
                  color_discrete_sequence=CHART_COLORS)
    fig2.update_layout(**LAYOUT_TEMPLATE)
    
    # Credit amount histogram
    fig3 = px.histogram(df_clean, x='Credit amount', nbins=30,
                        title='Credit Amount Distribution',
                        color_discrete_sequence=[CHART_COLORS[0]])
    fig3.update_layout(**LAYOUT_TEMPLATE)
    
    # Housing vs Job
    housing_job = df_clean.groupby(['Housing', 'Job']).size().reset_index(name='Count')
    fig4 = px.bar(housing_job, x='Housing', y='Count', color='Job',
                  title='Housing Type by Job Category',
                  color_discrete_sequence=CHART_COLORS)
    fig4.update_layout(**LAYOUT_TEMPLATE)
    
    # Savings vs Checking accounts
    savings_checking = df_clean.groupby(['Saving accounts', 'Checking account']).size().reset_index(name='Count')
    fig5 = px.bar(savings_checking, x='Saving accounts', y='Count', color='Checking account',
                  title='Savings vs Checking Accounts',
                  color_discrete_sequence=CHART_COLORS)
    fig5.update_layout(**LAYOUT_TEMPLATE)
    
    # Duration vs Amount scatter
    fig6 = px.scatter(df_clean, x='Duration', y='Credit amount', color='Purpose',
                      title='Duration vs Credit Amount by Purpose',
                      color_discrete_sequence=CHART_COLORS)
    fig6.update_layout(**LAYOUT_TEMPLATE)
    
    return fig1, fig2, fig3, fig4, fig5, fig6

if __name__ == '__main__':
    print('Dashboard initialized successfully!')
    print('Starting server...')
    print('='*60)
    print('🚀 DASHBOARD READY!')
    print('📊 Open your browser and go to: http://127.0.0.1:8050')
    print('🎨 Theme: Black & Off-White')
    print('📈 Features: Interactive charts, KPI metrics, responsive layout')
    print('⚡ Press Ctrl+C to stop the server')
    print('='*60)
    
    # Run the server
    app.run(debug=False, host='127.0.0.1', port=8050)