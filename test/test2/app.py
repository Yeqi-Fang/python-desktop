from flask import Flask, render_template
import json
import plotly
# from plotly import graph_objs as go
# import numpy as np
import plotly.express as px
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def kek():
    # t = np.linspace(0, 10, 100)
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(
    #     x=t, y=np.sin(t),
    #     name='sin',
    #     mode='markers',
    #     marker_color='rgba(152, 0, 0, .8)'
    # ))
    # fig.add_trace(go.Scatter(
    #     x=t, y=np.cos(t),
    #     name='cos',
    #     marker_color='rgba(255, 182, 193, .9)'
    # ))
    # fig.update_traces(mode='markers', marker_line_width=2, marker_size=10)
    # fig.update_layout(title='Styled Scatter',
    #                   yaxis_zeroline=False, xaxis_zeroline=False)
    df = px.data.iris()
    print(df)
    fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
                         color='species', title="Iris Dataset")
    # graph2JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    data = [fig]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('test2.html', graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(debug=False)
