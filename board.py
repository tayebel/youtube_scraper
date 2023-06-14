
from yt import *
class dashboard(yt_analysis):
    def __init__(self, channelType=None, eventType=None, location=None, locationRadius=None,
                 maxResults=None, channelId=None, regions_code=None, keyword=None, order=None,
                 publishedAfter=None, publishedBefore=None, relevanceLanguage=None):
        super().__init__(channelType, eventType, location, locationRadius, maxResults, channelId,
                         regions_code, keyword, order, publishedAfter, publishedBefore, relevanceLanguage)

    def board(self):
        self.data ,self.username ,self.video_total, self.subscriber, self.view =self.chan_stats()
        app = Dash(__name__)
        import plotly.express as px

        from dash.exceptions import PreventUpdate

        app.layout = html.Div(children=[
            html.H1(children='Youtube analysis dashboard: '),
            html.Div(children='''This dash is A web application framework to visualize and analyze different youtube channels either random ones or chosing a specific ones through entering  the inputs (e.g channel keyword)) '''),

            html.Label('keywords:'),
            dcc.Input(
                id="q"
            ),
            html.Label('maximum results:'),
            dcc.Input(
                id="m"
            ),
           
            
            html.Button('Update Inputs', id='update-button'),

            html.Button('Save Excel Sheet', id='save-button'),
            
            html.Div(id='body-div'),

            
            dcc.RadioItems(options=['number_of_videos', 'views', 'subscribers'], value='views', id='controls-and-radio-item'),
            
            dash_table.DataTable(page_size=6,id='tbl'),
            dcc.Graph(figure={}, id='controls-and-graph'),
            dcc.Graph(figure={}, id='controls')
            
            
        ])
        
        
        @callback(
           
            Output(component_id='tbl', component_property='data'),
         
            Input('q', "value"),
            Input('m', "value"),
    
            Input('update-button', 'n_clicks'))
        
        
        def update(m,q,n_clicks):
            if n_clicks is not None:
                self.keyword=q
                self.maxResults=m
                self.data ,self.username ,self.video_total, self.subscriber, self.view =self.chan_stats()
               
            return self.data
 
        @callback(
           
            Output(component_id='controls-and-graph', component_property='figure'),
            Output(component_id='controls', component_property='figure'),
            Input(component_id='controls-and-radio-item', component_property='value'))
        
        def update_fig(col_chosen):

            self.data ,self.username ,self.video_total, self.subscriber, self.view =self.chan_stats()
            df=pd.DataFrame(self.data)
            fig2= px.pie(df, values=col_chosen, names='channel_name')
            fig = px.histogram(df, x='channel_name', y=col_chosen, histfunc='avg')
            
            return fig,fig2
        
        @callback(
            Output(component_id='body-div', component_property='children'),
           
            Input(component_id='save-button', component_property='n_clicks'))
            
        
        def update_output(n_clicks):
            if n_clicks is None:
                raise PreventUpdate
            else:
                return self.excel()
        
       
            
        app.run_server(port=8053)

