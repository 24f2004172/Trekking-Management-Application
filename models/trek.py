from datetime import datetime
from extensions import db


class Trek(db.Model):
    __tablename__ = "treks"

    id = db.Column(db.Integer, primary_key=True)

    trek_name = db.Column(db.String(150), nullable=False)

    location = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text)

    difficulty = db.Column(
        db.Enum("Easy", "Moderate", "Hard", name="difficulty_levels"),
        nullable=False
    )

    duration = db.Column(db.Integer, nullable=False)

    total_slots = db.Column(db.Integer, nullable=False)

    available_slots = db.Column(db.Integer, nullable=False)

    start_date = db.Column(db.Date)

    end_date = db.Column(db.Date)

    status = db.Column(
        db.Enum(
            "Pending",
            "Approved",
            "Open",
            "Closed",
            "Completed",
            name="trek_status"
        ),
        default="Pending"
    )

    assigned_staff_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.now
    )

    staff = db.relationship(
        "User",
        back_populates="assigned_treks"
    )

    bookings = db.relationship(
        "Booking",
        back_populates="trek",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Trek {self.trek_name}>"