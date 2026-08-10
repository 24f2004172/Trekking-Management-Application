from datetime import datetime
from extensions import db


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    trek_id = db.Column(
        db.Integer,
        db.ForeignKey("treks.id"),
        nullable=False
    )

    booking_date = db.Column(
        db.DateTime,
        default=datetime.now()
    )

    booking_status = db.Column(
        db.Enum(
            "Booked",
            "Cancelled",
            "Completed",
            name="booking_status"
        ),
        default="Booked"
    )

    payment_status = db.Column(
        db.Enum(
            "Pending",
            "Paid",
            "Failed",
            name="payment_status"
        ),
        default="Pending"
    )

    number_of_people = db.Column(
        db.Integer,
        default=1
    )

    user = db.relationship(
        "User",
        back_populates="bookings"
    )

    trek = db.relationship(
        "Trek",
        back_populates="bookings"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "trek_id": self.trek_id,
            "booking_date": self.booking_date.isoformat() if self.booking_date else None,
            "booking_status": self.booking_status,
            "payment_status": self.payment_status,
            "number_of_people": self.number_of_people,
            "user_name": self.user.name if self.user else None,
            "trek_name": self.trek.trek_name if self.trek else None,
            "trek_image": self.trek.image_url if self.trek else None
        }

    def __repr__(self):
        return f"<Booking {self.id}>"
