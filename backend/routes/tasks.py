from celery import shared_task
from model.models import *
from jinja2 import Template
from celery import shared_task
from routes.send_email import send_email
from datetime import datetime



@shared_task(ignore_result=True)
def monthly_reminder():
    users = User.query.all()
    for user in users:
        orders = Order.query.filter_by(user_id=user.id).all()
        total_amount=0
        count=0
        if orders:
            for order in orders:
                if order.time.month == (datetime.now().month):
                    total_amount+=order.price*order.qty
                    count+=1
                
        import os
        print(os.getcwd())
        file_path=os.path.join(os.getcwd(),'templates','monthly_report.html')
        with open(file_path, 'r') as f:
            template = Template(f.read())
            send_email(user.email, "Shopzee-Monthly Report",
                            template.render(name=user.name, count = count, total_amount = total_amount))
    return "OK"

