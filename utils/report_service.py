from sqlalchemy import func

from extensions import db
from models.booking import Booking
from models.trek import Trek


def generate_monthly_report():
    trek_count = Trek.query.count()

    participant_count = Booking.query.count()

    popular_treks = (
        db.session.query(
            Trek.trek_name,
            func.count(Booking.id)
        )
        .join(Booking)
        .group_by(Trek.id)
        .order_by(
            func.count(Booking.id).desc()
        )
        .all()
    )

    return {
        "trek_count": trek_count,
        "participant_count": participant_count,
        "popular_treks": popular_treks
    }