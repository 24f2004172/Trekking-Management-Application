import csv
import os

from models.booking import Booking


def export_booking_history(user_id):

    bookings = Booking.query.filter_by(
        user_id=user_id
    ).all()

    os.makedirs("exports", exist_ok=True)

    filename = f"exports/user_{user_id}.csv"

    with open(
        filename,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "User ID",
            "Trek Name",
            "Location",
            "Booking Status",
            "Date"
        ])

        for booking in bookings:

            writer.writerow([
                booking.user_id,
                booking.trek.trek_name,
                booking.trek.location,
                booking.booking_status,
                booking.booking_date
            ])

    return filename