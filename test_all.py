import pytest
import database_utils
import utils
import main
import os

def test_if_database_exists():
    """
    Testar om det finns en databas med korrekt namn.
    """
    assert os.path.exists("database.db")

def test_create_table():
    """
    Testar om det finns en tabell med korrekt namn.
    """
    database_utils.create_table()
    cursor = database_utils.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='observations'")
    result = cursor.fetchone()
    assert result is not None
    assert result[0] == "observations"

def test_create_and_read():
    """
    Testar att det går att lägga till och läsa observationer i databasen..
    """
    database_utils.create_table()
    name = "Testnamn"
    value = 1
    obs_id = database_utils.create(name, value)
    assert obs_id is not None

    result = database_utils.read(obs_id)
    assert result is not None
    assert result[1] == name
    assert result[2] == value

def test_update_observation():
    """
    Testar att det går att uppdatera en observation i databasen.
    """
    database_utils.create_table()
    obs_id = database_utils.create("Före", 1)
    database_utils.update(obs_id, "Efter", 2)
    result = database_utils.read(obs_id)
    assert result[1] == "Efter"
    assert result[2] == 2

def test_delete_observation():
    """
    Testar att det går att radera en observation från databasen.
    """
    database_utils.create_table()
    obs_id = database_utils.create("Test", 1)
    database_utils.delete(obs_id)
    result = database_utils.read(obs_id)
    assert result is None

def test_do_something():
    """
    Testar om do_something lägger till en observation i databasen.
    """
    database_utils.create_table()
    cursor = database_utils.connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM observations")
    before = cursor.fetchone()[0]

    utils.do_something(99)

    cursor.execute("SELECT COUNT(*) FROM observations")
    after = cursor.fetchone()[0]

    assert after == before + 1

def run_once(value):
    """
    Kör main-loopen bara en gång (för att kunna testa)
    """
    utils.do_something(value)

def test_main_run_once():
    database_utils.create_table()
    cursor = database_utils.connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM observations")
    before = cursor.fetchone()[0]

    run_once(42)

    cursor.execute("SELECT COUNT(*) FROM observations")
    after = cursor.fetchone()[0]

    assert after == before + 1