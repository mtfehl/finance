"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from typing import List
from random import random
from projects.pj02 import constants
from math import sin, cos, pi, sqrt


__author__ = "730321206"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Distance between two points."""
        x_dist: float = ((other.x - self.x) ** 2)
        y_dist: float = ((other.y - self.y) ** 2)
        total_distance: float = sqrt((x_dist) + (y_dist))
        return total_distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Enables movement of cells and immunization of infected cells."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Infected cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Vulnerable cell."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def immunize(self) -> None:
        """An immune cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        elif self.is_infected() is True:
            return "blue"
        elif self.is_immune() is True:
            return "purple"
        else:
            return "gray"
        
    def contact_with(self, other_cell: Cell) -> None:
        """Called if a cell comes into contact with another cell."""
        if self.is_infected() is True:
            if other_cell.is_vulnerable() is True:
                other_cell.contract_disease()
        if other_cell.is_infected() is True:
            if self.is_vulnerable() is True:
                self.contract_disease()


class Model:
    """The state of the simulation."""

    population: List[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        non_vulnerable: int = infected + immune
        if infected >= cells:
            raise ValueError("Too many cells are beginning as infected!")
        elif infected <= 0:
            raise ValueError("Some cells must begin as infected!")
        elif immune >= cells:
            raise ValueError("Too many cells are beginning as immune!")
        elif non_vulnerable >= cells:
            raise ValueError("You need to begin with non-infected cells!")
        for _ in range(non_vulnerable, cells):
            start_location = self.random_location()
            start_direction = self.random_direction(speed)
            self.population.append(Cell(start_location, start_direction))
        for _ in range(0, infected):
            start_location = self.random_location()
            start_direction = self.random_direction(speed)
            a_cell = Cell(start_location, start_direction)
            a_cell.contract_disease()
            self.population.append(a_cell)
        for _ in range(0, immune):
            start_location = self.random_location()
            start_direction = self.random_direction(speed)
            immune_cell = Cell(start_location, start_direction)
            immune_cell.sickness = constants.IMMUNE
            self.population.append(immune_cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2.0 * pi * random()
        direction_x = cos(random_angle) * speed
        direction_y = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1

    def check_contacts(self) -> None:
        """Determines whether any two cells come into contact with one another."""
        for cell in self.population:
            for other_cell in self.population:
                if cell != other_cell:
                    if cell.location.distance(other_cell.location) < constants.CELL_RADIUS:
                        cell.contact_with(other_cell)

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        list: List[int] = []
        for cells in self.population:
            if cells.is_infected() is True:
                list.append(1)
            if cells.is_vulnerable() is True:
                list.append(2)
            if cells.is_immune() is True:
                list.append(3)
        if 1 in list:
            return False
        else:
            return True