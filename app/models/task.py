# Task List API Project
# Katrina Kimzey
# Cohort 15 - Paper

from flask import current_app
from app import db
from datetime import datetime


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True, default=None)

    def to_dict(self):
        ret_dict = {
            "id" : self.task_id,
            "title" : self.title,
            "description" : self.description,
            "is_complete" : bool(self.completed_at),
        }

        if self.goal_id:
            ret_dict["goal_id"] = self.goal_id

        return ret_dict
