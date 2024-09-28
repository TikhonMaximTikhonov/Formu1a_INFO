import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm
import sqlalchemy

from sqlalchemy.orm import Session

SqlAlchemyBase = dec.declarative_base()


class DataBase:
    def __init__(self, db_file):
        self.factory = None
        self.main_init(db_file)

    def main_init(self, db_file):
        if self.factory:
            return
        conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
        engine = sqlalchemy.create_engine(conn_str, echo=False)
        self.factory = orm.sessionmaker(bind=engine)
        SqlAlchemyBase.metadata.create_all(engine)

    def create_session(self) -> Session:
        return self.factory()


# << Static bases >>

class Points(SqlAlchemyBase):
    __tablename__ = "points"
    type_of_race = sqlalchemy.Column(sqlalchemy.String, primary_key=True, nullable=False)
    position = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    points = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __init__(self, type_of_race: str, position: int, points: str):
        self.type_of_race = type_of_race
        self.position = position
        self.points = points


class Season(SqlAlchemyBase):
    __tablename__ = "seasons"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, unique=True)
    race_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    def __init__(self, season_id: int, race_count: int):
        self.id = season_id
        self.race_count = race_count


# << Updated bases >>
