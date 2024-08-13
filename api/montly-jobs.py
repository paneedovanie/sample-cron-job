import datetime

def handler(request, response):
    # Your cron job logic here
    now = datetime.datetime.now()
    return response.json({
        "message": "Python cron job executed",
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")
    })