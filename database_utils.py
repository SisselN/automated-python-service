import sqlite3
import logging
import pytest
import os

logger = logging.getLogger(__name__)
"""
Skapar en databas och ansluter till den.
"""
try:
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    logger.info("Anslutning till databasen upprättad.")
except sqlite3.Error as e:
    logger.error(f"Fel vid anslutning till databasen: {e}")


def create_table():
    """
    Skapar en tabell.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value REAL
        )
    """)
    connection.commit()

# Funktioner för CRUD
def create(name, value):
    try:
        cursor.execute("INSERT INTO observations (name, value) VALUES (?, ?)", (name, value))
        connection.commit()
        logger.info(f"Observation skapad: {name}, {value}")
        return cursor.lastrowid
    except sqlite3.Error as e:
        logger.error(f"Fel vid skapande: {e}")
        return None

def read(observation_id):
    try:
        cursor.execute("SELECT * FROM observations WHERE id = ?", (observation_id,))
        logger.info(f"Observation {observation_id} läst.")
        return cursor.fetchone()
    except sqlite3.Error as e:
        logger.error(f"Fel vid läsning: {e}")
        return None

def update(observation_id, name, value):
    try:
        cursor.execute("UPDATE observations SET name = ?, value = ? WHERE id = ?", (name, value, observation_id))
        connection.commit()
        logger.info(f"Observation uppdaterad.")
    except sqlite3.Error as e:
        logger.error("Fel vid uppdatering: {e}")
        return None

def delete(observation_id):
    try:
        cursor.execute("DELETE FROM observations WHERE id = ?", (observation_id,))
        connection.commit()
        logger.info(f"Observation {observation_id} borttagen")
    except sqlite3.Error as e:
        print(f"Fel vid borttagning: {e}")
        return None
