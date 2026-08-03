from extensions import db


class StaffProfile(db.Model):
    __tablename__ = "staff_profiles"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    designation = db.Column(db.String(100))

    experience = db.Column(db.Integer)

    emergency_contact = db.Column(db.String(15))

    status = db.Column(
        db.Enum("Active", "Inactive", name="staff_status"),
        default="Active"
    )

    user = db.relationship(
        "User",
        back_populates="staff_profile"
    )

    def __repr__(self):
        return f"<StaffProfile {self.id}>"