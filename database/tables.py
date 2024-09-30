import sqlalchemy
import sqlalchemy.ext.declarative as dec

from datetime import date, datetime, time

SqlAlchemyBase = dec.declarative_base()


# << Static bases >>

class Points(SqlAlchemyBase):
    __tablename__ = "points"
    race_type = sqlalchemy.Column(sqlalchemy.String, primary_key=True, nullable=False)
    position = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    points = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __init__(self, type_of_race: str, position: int, points: str):
        self.type_of_race = type_of_race
        self.position = position
        self.points = points


class Seasons(SqlAlchemyBase):
    __tablename__ = "seasons"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, unique=True)
    race_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    def __init__(self, season_id: int, race_count: int):
        self.id = season_id
        self.race_count = race_count


class Tracks(SqlAlchemyBase):
    __tablename__ = "tracks"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    length = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    turn_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    debut = sqlalchemy.Column(sqlalchemy.Date, nullable=False)

    def __init__(self, name: str, length: int, turn_count: int, debut: date):
        self.name = name
        self.length = length
        self.turn_count = turn_count
        self.debut = debut


class Teams(SqlAlchemyBase):
    __tablename__ = "teams"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    country = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    debut = sqlalchemy.Column(sqlalchemy.Date, nullable=True)

    def __init__(self, name: str, country: str, debut: date):
        self.name = name
        self.county = country
        self.debut = debut


class Drivers(SqlAlchemyBase):
    __tablename__ = "drivers"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    id_season = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    id_team = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    fullname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    reduction = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    country = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    birthday = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    debut = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    height = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def __init__(self, id_season: int, id_team: int, fullname: str, reduction: str,
                 country: str, birthday: date, debut: date, height: int):
        self.id_season = id_season
        self.id_team = id_team
        self.fullname = fullname
        self.reduction = reduction
        self.country = country
        self.birthday = birthday
        self.debut = debut
        self.height = height


# << Updated bases >>

class Races(SqlAlchemyBase):
    __tablename__ = "races"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    id_season = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    id_track = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    race_type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    event_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)

    def __init__(self, id_season: int, id_track: int, race_type: str, event_date: datetime):
        self.id_season = id_season
        self.id_track = id_track
        self.race_type = race_type
        self.event_date = event_date


class Results(SqlAlchemyBase):
    __tablename__ = "results"
    id_race = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    id_driver = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    position = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    best_time = sqlalchemy.Column(sqlalchemy.Time, nullable=False)
    best_lap = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

    def __init__(self, id_race: int, id_driver: int, position: int, best_time: time, best_lap=False):
        self.id_race = id_race
        self.id_driver = id_driver
        self.position = position
        self.best_time = best_time
        self.best_lap = best_lap
