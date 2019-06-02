def handler(event, context):
    name = event["name"]

    return "Hello {} !!".format(name)