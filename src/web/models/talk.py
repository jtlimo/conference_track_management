from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker  

base = declarative_base()

class Talks(base):
    __tablename__ = 'talks'

    id_seq = Sequence('id_seq', metadata=base.metadata)
    id  = Column(Integer, id_seq, server_default=id_seq.next_value(), primary_key=True)
    title = Column(String)
    description = Column(String)

    def __init__(self):
        db_string = ('postgresql://jlima:coolpassword@localhost/conference')
        self.db = create_engine(db_string)
        
    def create_db(self):
        Session = sessionmaker(self.db)
        session = Session()
        base.metadata.create_all(self.db)
        return session
