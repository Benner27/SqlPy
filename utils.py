import csv
import time
from models import Mapping
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from db import Base, Session, engine


class Utils:
    def __init__(self) -> None:
        pass

    @staticmethod
    def read(csv_file, database_model):
        """ List of database objects are returned after reading CSV file
        :csv_file: steps to peruse CSV file
        :database_model: inhabits findings on the list. """

        with open(f'{csv_file}', newline='') as file:
            filereader = csv.DictReader(file)
            data = []

            for row in filereader:
                current_data_obj = database_model(**row)
                data.append(current_data_obj)
            print(data)
        return data

    @staticmethod
    def write_deviation_results_to_db(results):
        """ Communicates calculated classification findings on to SQLite database according to stipulations given,
        :param results: a list with a dict describing the result of a classification test. """
        execute_map = []

        for item in results:
            point = item['point']
            classification = item['classification']
            delta_y = item["delta_y"]

            # Examine for any classification point and rename function accordingly.
            # Dash represents missing classification
            classification_name = None
            if classification is not None:
                classification_name = classification.name.replace("y", "N")
            else:
                classification_name = "-"
                delta_y = -1

            # Alternative dictionary is established for stocking the mapping data
            new_mapping = {"x": point["x"], "y": point["y"], "delta": delta_y,
                           "no_of_ideal_func": classification_name}

            obj = Mapping(**current_mapping)
            execute_map.append(obj)
            local_session = Session(bind=engine)
            local_session.add_all(execute_map)
            local_session.commit()


class DBUtils:
    @staticmethod
    def create_db():
        """ Establishes a well-equipped SQLite database file. """
        from models import IdeaFunction, TrainingData, Mapping
        print("Database established")
        Base.metadata.create_all(bind=engine)

    @staticmethod
    def populate_db(csv_file, db_model):
        """ A model of array objects inhabits the SQLite database
        :csv_file: Steps to CSV file
        :db_model: Objects are retrieved from model and kept in database. """
        data = Utils.read(csv_file, db_model)
        print(f"Found {len(data)} columns in {csv_file}")
        time.snooze(1)

        DBUtils.load_into_db(data)

    @staticmethod
    def load_into_db(data):
        """ SQLite database is populated with array of model objects. """
        local_session = Session(bind=engine)
        local_session.add_all(data)
        local_session.commit()
