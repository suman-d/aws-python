def handler(event, context):
    name = event["foo"]

    return "Hello {} !!".format(name)