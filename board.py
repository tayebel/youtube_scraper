from yt import *

class dashboard(yt_analysis):
    def __init__(self, channelType=None, eventType=None, location=None, locationRadius=None,
                 maxResults=None, channelId=None, regions_code=None, keyword=None, order=None,
                 publishedAfter=None, publishedBefore=None, relevanceLanguage=None):
        super().__init__(channelType, eventType, location, locationRadius, maxResults, channelId,
                         regions_code, keyword, order, publishedAfter, publishedBefore, relevanceLanguage)
    
    def board(self):
        try:
            self.data, self.username, self.video_total, self.subscriber, self.view = self.chan_stats()
            country_codes = [country.alpha_2 for country in pycountry.countries]

            app = dash.Dash(__name__,assets_folder='assets')
           
            app.layout = html.Div(children=[
                html.H1(children='Youtube channels analysis dashboard: '),
                html.Div(children='''This dash is A web application framework to visualize and analyze different youtube channels  '''),

                html.Label('Search by:'),
                dcc.Dropdown(
                    id='input-type',
                    options=[
                        {'label': 'keyword', 'value': 'keyword'},
                        {'label': 'maxResults', 'value': 'maxResults'},
                        {'label': 'regions_code', 'value': 'regions_code'},
                        
                        {'label': 'username', 'value': 'username'},
                        {'label': 'eventType', 'value': 'eventType'},
                        {'label': 'location', 'value': 'location'},
                        {'label': 'locationRadius', 'value': 'locationRadius'},
                        
                        {'label': 'channelId', 'value': 'channelId'},
                        
                        
                        
                        {'label': 'publishedAfter', 'value': 'publishedAfter'},
                    
                        
                    ],
                    value=[],
                    multi=True
                ),

                html.Div(id='input-q-container', children=[
                    html.Label('Enter a keyword:'),
                    dcc.Input(id='input-q', type='text')
                ], style={'display': 'none'}),

                html.Div(id='input-m-container', children=[
                    html.Label('Enter the maximum results:'),
                    dcc.Input(id='input-m', type='number')
                ], style={'display': 'none'}),
                
                html.Div(id='input-r-container', children=[
                    html.Label('Enter a  region code:'),
                    dcc.Input(id='input-r', type='text',
                        list='region-options',
                    ),
                    html.Datalist(
                        id='region-options',
                        children=[html.Option(value=code) for code in country_codes],
                    )
                ], style={'display': 'none'}),
                
                html.Div(id='input-c-container', children=[
                    html.Label('Enter a  username:'),
                    dcc.Input(id='input-c', type='text')
                ], style={'display': 'none'}),
                
                html.Div(id='input-e-container', children=[
                html.Label('Enter an event type:'),
                dcc.Input(
                    id='input-e',
                    type='text',
                )
            ], style={'display': 'none'}),
                
                html.Div(id='input-l-container', children=[
                    html.Label('Enter a  location:'),
                    dcc.Input(id='input-l', type='text',
                    placeholder='Latitude, Longitude (e.g., 37.42307, -122.08427)')
                ], style={'display': 'none'}),
                
                html.Div(id='input-lr-container', children=[
                    html.Label('Enter a  location raduis:'),
                    dcc.Input(id='input-lr', type='text',
                    placeholder='Radius in meters (e.g., 1000)')
                ], style={'display': 'none'}),
                
                html.Div(id='input-cd-container', children=[
                    html.Label('  channel ID:'),
                    dcc.Input(id='input-cd', type='text')
                ], style={'display': 'none'}),
                
                
                html.Div(id='input-p-container', children=[
                    html.Label('Published after:'),
                    dcc.Input(id='input-p',  type='datetime',
                    inputMode='text',
                    placeholder='YYYY-MM-DDTHH:MM:SSZ')
                ], style={'display': 'none'}),
                
                
                html.Button('Search', id='update-button'),

                html.Button('Save Excel Sheet', id='save-button'),

                html.Div(id='body-div'),

               
                
                dash_table.DataTable(page_size=6, id='tbl'),
                dcc.RadioItems(options=['number_of_videos', 'views', 'subscribers'], value='views', id='controls-and-radio-item'),
                dcc.Graph(figure={}, id='controls-and-graph'),
                dcc.Graph(figure={}, id='controls')
            ])

            @app.callback(
                Output('input-q-container', 'style'),
                Output('input-m-container', 'style'),
                Output('input-r-container', 'style'),
                Output('input-c-container', 'style'),
                Output('input-e-container', 'style'),
                Output('input-l-container', 'style'),
                Output('input-lr-container', 'style'),
                Output('input-cd-container', 'style'),
                Output('input-p-container', 'style'),
                Input('input-type', 'value'))
            def update_input_style(input_type):
                q_style = {'display': 'none'}
                m_style = {'display': 'none'}
                r_style = {'display': 'none'}
                c_style = {'display': 'none'}
                e_style = {'display': 'none'}
                l_style = {'display': 'none'}
                lr_style = {'display': 'none'}
                cd_style = {'display': 'none'}
                p_style = {'display': 'none'}
                
                if 'keyword' in input_type:
                    q_style = {'display': 'block'}
                if 'maxResults' in input_type:
                    m_style = {'display': 'block'}
                if 'regions_code' in input_type:
                    r_style = {'display': 'block'}
                if 'username' in input_type:
                    c_style = {'display': 'block'}
                if 'eventType' in input_type:
                    e_style = {'display': 'block'}
                if 'location' in input_type:
                    l_style = {'display': 'block'}
                if 'locationRadius' in input_type:
                    lr_style = {'display': 'block'}
                if 'channelId' in input_type:
                    cd_style = {'display': 'block'}
                if 'publishedAfter' in input_type:
                    p_style = {'display': 'block'}
            
                    
                return q_style, m_style,r_style,c_style,e_style,l_style,lr_style,cd_style,p_style

            @app.callback(
                Output(component_id='tbl', component_property='data'),
                Output(component_id='controls-and-graph', component_property='figure'),
                Output(component_id='controls', component_property='figure'),
                Input('update-button', 'n_clicks'),
                Input(component_id='controls-and-radio-item', component_property='value'),
                
                *[State(f'input-{input_param}', 'value') for input_param in ['q', 'm', 'r', 'c',
                                                                            'e', 'l', 'lr', 'cd', 'p']],
                State('input-type', 'value'))
                
            def update(n_clicks,col_chosen, input_q, input_m,input_r,input_c,input_e,input_l,input_lr,input_cd,input_p, input_type):
                if n_clicks is not None:
                    if 'keyword' in input_type:
                        self.keyword = input_q
                    else:
                        self.keyword = None
                    
                    if 'maxResults' in input_type:
                        self.maxResults = input_m
                    else:
                        self.maxResults = None
                        
                    if 'regions_code' in input_type:
                        self.regions_code = input_r
                    else:
                        self.regions_code = None
                    if 'channelType' in input_type:
                        self.usernam = input_c
                    else:
                        self.channelType = None
                    if 'eventType' in input_type:
                        self.eventType = input_e
                    else:
                        self.eventType = None   
                    if 'location' in input_type:
                        self.location = input_l
                    else:
                        self.location = None 
                    if 'locationRadius' in input_type:
                        self.locationRadius = input_lr
                    else:
                        self.locationRadius = None 
                    if 'channelId' in input_type:
                        self.channelId = input_cd
                    else:
                        self.channelId = None 
                    if 'publishedAfter' in input_type:
                        self.publishedAfter = input_p
                    else:
                        self.publishedAfter = None 
                       
                    self.data, self.username, self.video_total, self.subscriber, self.view = self.chan_stats()
                df = pd.DataFrame(self.data)
                fig2 = px.pie(df, values=col_chosen, names='channel_name')
                fig = px.histogram(df, x='channel_name', y=col_chosen, histfunc='avg')
               
                return self.data,fig,fig2
            
            
         
                




            @app.callback(
                Output(component_id='body-div', component_property='children'),
                Input(component_id='save-button', component_property='n_clicks'))
            def update_output(n_clicks):
                if n_clicks is None:
                    raise PreventUpdate
                else:
                    return self.excel()

            app.run_server(port=8053)
        except HttpError as e:
            if e.resp.status == 403:
                app = dash.Dash(__name__)
                app.layout = html.Div(children=[
                html.H1(children='Youtube channels analysis dashboard: '),
                html.Div(style={ 'color': 'red'},children='''Quota exceeded. Please try again later.''')])
                app.run_server(port=8053)
            elif e.resp.status == 400 or e.resp.status == 401:
                app = dash.Dash(__name__)
                app.layout = html.Div(children=[
                html.H1(children='Youtube channels analysis dashboard: '),
                html.Div(style={ 'color': 'red'},children='''Invalid API key. Please check your credentials.''')])
                app.run_server(port=8053)
                # Run alternative code specific to invalid API key scenario
                # ...
            else:
                app = dash.Dash(__name__)
                app.layout = html.Div(children=[
                html.H1(children='Youtube channels analysis dashboard: '),
                html.Div(style={ 'color': 'red'},children=f"An error occurred:{e}")])
                app.run_server(port=8053)
                
                        