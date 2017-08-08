from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Datastore():
    __conn = None

    def __init__(self, app):
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        self.__conn = engine.connect()

    #
    # PROPERTIES
    #

    @property
    def conn(self): return self.__conn

    #
    # METHODS
    #

    def select_ohio_district_voting_data(self):
        s = text(
                'SELECT "HOUSE_DISTRICT", '
                    'SUM(ush_dvote_08), '
                    'SUM(ush_rvote_08), '
                    'SUM(ush_tvote_08) '
                    'FROM data_vote_twelve '
                    'WHERE "HOUSE_DISTRICT" != 0 '
                    'GROUP BY "HOUSE_DISTRICT" '
                    'ORDER BY "HOUSE_DISTRICT" '
                )
        return self.conn.execute(s).fetchall()
