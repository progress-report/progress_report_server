from sqlalchemy import create_engine, MetaData, Table, Column, Integer
from sqlalchemy.sql import select, text


class Datastore():
    __conn = None
    __metadata = MetaData()
    __ohio = Table('data_vote_twelve',
                   __metadata,
                   Column('ush_dvote_08', Integer()),
                   Column('ush_rvote_08', Integer()),
                   Column('ush_tvote_08', Integer()),
                   Column('HOUSE_DISTRICT', Integer()),
             )

    def __init__(self, app=None, conn_string=None):
        engine = create_engine(conn_string or app.config['SQLALCHEMY_DATABASE_URI'])
        self.metadata.create_all(engine)
        self.__conn = engine.connect()

    #
    # PROPERTIES
    #

    @property
    def conn(self): return self.__conn

    @property
    def metadata(self): return self.__metadata

    @property
    def ohio(self): return self.__ohio

    #
    # METHODS
    #

    def get_ohio_district_voting_data(self):
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
