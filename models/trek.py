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

    image_url = db.Column(
        db.String(255),
        nullable=False,
        default="/images/hampta.jpg"
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

    def to_dict(self):
        return {
            "id": self.id,
            "trek_name": self.trek_name,
            "location": self.location,
            "description": self.description,
            "difficulty": self.difficulty,
            "duration": self.duration,
            "total_slots": self.total_slots,
            "available_slots": self.available_slots,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "status": self.status,
            "image_url": self.image_url,
            "assigned_staff_id": self.assigned_staff_id,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f"<Trek {self.trek_name}>"