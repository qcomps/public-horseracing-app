from .base import Base

from app.db import db


class Result(Base):
    __tablename__ = 'results'
    __table_args__ = (
        None,
        db.UniqueConstraint(
            'horse_id',
            'race_id',
            name='uniq_result'
        )
    )

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    race_id = db.Column(db.Integer, db.ForeignKey('races.id'))
    horse_id = db.Column(db.Integer, db.ForeignKey('horses.id'))
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'))
    jockey_id = db.Column(db.Integer, db.ForeignKey('jockeys.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    race = db.relationship("Race", back_populates="results")
    horse = db.relationship("Horse", back_populates="results")
    trainer = db.relationship("Trainer", back_populates="results")
    jockey = db.relationship("Jockey", back_populates="results")
    owner = db.relationship("Owner", back_populates="results")

    last_raced = db.Column(db.Date)
    lasix = db.Column(db.String)
    blinker_change = db.Column(db.String)
    claiming_price = db.Column(db.DECIMAL)
    cur_year_earn = db.Column(db.DECIMAL)
    cur_year_starts = db.Column(db.Integer)
    cur_year_wins = db.Column(db.Integer)
    cur_year_places = db.Column(db.Integer)
    cur_year_shows = db.Column(db.Integer)
    prior_year_earn = db.Column(db.DECIMAL)
    prior_year_starts = db.Column(db.Integer)
    prior_year_wins = db.Column(db.Integer)
    prior_year_places = db.Column(db.Integer)
    prior_year_shows = db.Column(db.Integer)
    lifetime_earn = db.Column(db.DECIMAL)
    lifetime_starts = db.Column(db.Integer)
    lifetime_wins = db.Column(db.Integer)
    lifetime_places = db.Column(db.Integer)
    lifetime_shows = db.Column(db.Integer)
    turf_earn = db.Column(db.DECIMAL)
    turf_starts = db.Column(db.Integer)
    turf_wins = db.Column(db.Integer)
    turf_places = db.Column(db.Integer)
    turf_shows = db.Column(db.Integer)
    fast_dirt_earn = db.Column(db.DECIMAL)
    fast_dirt_starts = db.Column(db.Integer)
    fast_dirt_wins = db.Column(db.Integer)
    fast_dirt_places = db.Column(db.Integer)
    fast_dirt_shows = db.Column(db.Integer)
    track_earn = db.Column(db.DECIMAL)
    track_starts = db.Column(db.Integer)
    track_wins = db.Column(db.Integer)
    track_places = db.Column(db.Integer)
    track_shows = db.Column(db.Integer)
    distance_earn = db.Column(db.DECIMAL)
    distance_starts = db.Column(db.Integer)
    distance_wins = db.Column(db.Integer)
    distance_places = db.Column(db.Integer)
    distance_shows = db.Column(db.Integer)
    jockey_meet_starts = db.Column(db.Integer)
    jockey_meet_earn = db.Column(db.DECIMAL)
    jockey_meet_wins = db.Column(db.Integer)
    jockey_meet_places = db.Column(db.Integer)
    jockey_meet_shows = db.Column(db.Integer)
    jockey_ytd_starts = db.Column(db.Integer)
    jockey_ytd_earn = db.Column(db.DECIMAL)
    jockey_ytd_wins = db.Column(db.Integer)
    jockey_ytd_places = db.Column(db.Integer)
    jockey_ytd_shows = db.Column(db.Integer)
    trainer_meet_starts = db.Column(db.Integer)
    trainer_meet_earn = db.Column(db.DECIMAL)
    trainer_meet_wins = db.Column(db.Integer)
    trainer_meet_places = db.Column(db.Integer)
    trainer_meet_shows = db.Column(db.Integer)
    trainer_ytd_starts = db.Column(db.Integer)
    trainer_ytd_earn = db.Column(db.DECIMAL)
    trainer_ytd_wins = db.Column(db.Integer)
    trainer_ytd_places = db.Column(db.Integer)
    trainer_ytd_shows = db.Column(db.Integer)
    odds = db.Column(db.Integer)
    post_position = db.Column(db.Integer)
    program_number = db.Column(db.String)
    start_position = db.Column(db.Integer)
    first_call_position = db.Column(db.Integer)
    second_call_position = db.Column(db.Integer)
    third_call_position = db.Column(db.Integer)
    fourth_call_position = db.Column(db.Integer)
    fifth_call_position = db.Column(db.Integer)
    final_position = db.Column(db.Integer)
    first_call_lengths_ahead = db.Column(db.DECIMAL)
    second_call_lengths_ahead = db.Column(db.DECIMAL)
    third_call_lengths_ahead = db.Column(db.DECIMAL)
    fourth_call_lengths_ahead = db.Column(db.DECIMAL)
    fifth_call_lengths_ahead = db.Column(db.DECIMAL)
    final_lengths_ahead = db.Column(db.DECIMAL)
    first_call_lengths_behind = db.Column(db.DECIMAL)
    second_call_lengths_behind = db.Column(db.DECIMAL)
    third_call_lengths_behind = db.Column(db.DECIMAL)
    fourth_call_lengths_behind = db.Column(db.DECIMAL)
    fifth_call_lengths_behind = db.Column(db.DECIMAL)
    final_lengths_behind = db.Column(db.DECIMAL)
    win_pay = db.Column(db.DECIMAL)
    place_pay = db.Column(db.DECIMAL)
    show_pay = db.Column(db.DECIMAL)
    morning_line_odds = db.Column(db.String)
    scratched = db.Column(db.Boolean)
    predicted_win_probability = db.Column(db.DECIMAL)
    predicted_individual_perf = db.Column(db.String)

    def __repr__(self):
        return "<Result(horse='%s', race='%s')>" % (
            self.horse_id, self.race_id)