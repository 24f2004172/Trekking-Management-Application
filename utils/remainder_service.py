from datetime import date, timedelta

from models.booking import Booking
from models.trek import Trek
from models.notification import Notification
from extensions import db

def send_daily_reminders():

    today = date.today()
    reminder_deadline = today + timedelta(days=3)

    bookings = (
        Booking.query
        .join(Trek)
        .filter(
            Trek.start_date >= today,
            Trek.start_date <= reminder_deadline,
            Booking.booking_status == "Booked"
        )
        .all()
    )

    sent_count = 0

    for booking in bookings:

        trek = booking.trek
        days_until_start = (trek.start_date - today).days
        start_message = (
            'starts today'
            if days_until_start == 0
            else f'starts in {days_until_start} day(s)'
        )

        notification = Notification(
            user_id=booking.user_id,
            message=(
                f'Your trek "{trek.trek_name}" {start_message}. '
                'Get ready—your adventure is very near!'
            )
        )

        db.session.add(notification)

        sent_count += 1

    db.session.commit()

    return sent_count
