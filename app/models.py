from __future__ import annotations
from typing import Optional, List
from datetime import time
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Time

class AudioProject(SQLModel, table=True):
    """Association table for many-to-many between AudioFile and Project."""
    project_id: int = Field(foreign_key="project.id", primary_key=True)
    audio_id: int = Field(foreign_key="audiofile.id", primary_key=True)

class AudioFile(SQLModel, table=True):
    """Represents an uploaded audio file."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    path: str
    # duration as a time object (HH:MM:SS)
    duration: time = Field(
        default=None,
        sa_column=Column(Time(), nullable=False)
    )

    # Relationships
    # labels: List[Label] = Relationship(back_populates="audio")
    # project_associations: List[AudioProject] = Relationship(back_populates="audio")
    # projects: List[Project] = Relationship(
    #     back_populates="audios",
    #     link_model=AudioProject
    # )

class Label(SQLModel, table=True):
    """Represents an instance of a trigger labeled within an audio file."""
    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="project.id")
    audio_id: int = Field(foreign_key="audiofile.id")
    trigger_id: int = Field(foreign_key="trigger.id")
    # start and end times as time objects
    start_time: time = Field(
        default=None,
        sa_column=Column(Time(), nullable=False)
    )
    end_time: time = Field(
        default=None,
        sa_column=Column(Time(), nullable=False)
    )

    # Relationships
    # project: Optional[Project] = Relationship(back_populates="labels")
    # audio: Optional[AudioFile] = Relationship(back_populates="labels")
    # trigger: Optional[Trigger] = Relationship(back_populates="labels")

class Project(SQLModel, table=True):
    """Represents a labeling project grouping triggers and labels."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    # Relationships
    # triggers: List[Trigger] = Relationship(back_populates="project")
    # labels: List[Label] = Relationship(back_populates="project")
    # audio_associations: List[AudioProject] = Relationship(back_populates="project")
    # audios: List[AudioFile] = Relationship(
    #     back_populates="projects",
    #     link_model=AudioProject
    # )

class Trigger(SQLModel, table=True):
    """Represents a trigger (keyword) within a project."""
    id: Optional[int] = Field(default=None, primary_key=True)
    label: str
    project_id: int = Field(foreign_key="project.id")

    # Relationships
    # project: Optional[Project] = Relationship(back_populates="triggers")
    # labels: List[Label] = Relationship(back_populates="trigger")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, nullable=False)
    email: str
    hashed_password: str