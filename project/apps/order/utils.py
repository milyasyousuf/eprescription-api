from django.contrib.auth.models import User
from django.apps import apps
from django.conf import settings


def order_notification_to_user():
    pass


def find_nearest_pharmacy():
    return {"pharmacy":1}

def check_drug_availability(pharmacy):
    return True

def order_notification_to_pharmacy(pharmacy):
    print("order notification sent to pharmacy")

def process_order():
    pharmacy = find_nearest_pharmacy()
    if check_drug_availability(pharmacy):
        order_notification_to_pharmacy(pharmacy)