import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from sqlalchemy import func

from database.tables import *


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

    # << Data check >>

    def check_season(self, season: int) -> bool:
        session = self.create_session()
        return session.query(Seasons).filter(Seasons.id == season).first is not None

    # def check_race(self, id_season, id_track):

    # << Data init >>

    def save_seasons(self, season: int, race_count=0) -> int:
        session = self.create_session()
        if not self.check_season(season):
            session.add(Seasons(season, race_count))
            session.commit()
        return season

    # << Season page >>

    def get_seasons(self) -> list:
        session = self.create_session()
        seasons_data = session.query(Seasons).order_by(Seasons.id.desc())
        return [season_data.id for season_data in seasons_data]

    # << statistic_type >>

    def get_season_statistic(self, season_id: int) -> list:
        session = self.create_session()
        try:
            race_count = session.query(Seasons).filter(Seasons.id == season_id)[0].race_count
        except IndexError:
            race_count = "Error: empty base"
        try:
            driver_leader = session.query(
                Drivers.reduction.label("reduction"),
                func.sum(Points.points).label("points_sum")
            ).join(
                Results, Drivers.id == Results.id_driver
            ).join(
                Races, Results.id_race == Races.id
            ).join(
                Points, Races.race_type == Points.race_type
            ).group_by(Drivers.id).order_by(func.sum(Points.points))
        except IndexError:
            driver_leader = "Не выявлен"

        print(driver_leader)

        return [season_id, race_count]
