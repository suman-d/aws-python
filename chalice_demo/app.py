from chalice import Chalice

app = Chalice(app_name='helloworld')

@app.lambda_function()
def hello_world(event, context):
    return 'hello world!'
