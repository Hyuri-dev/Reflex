"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

class User(rx.Model):
  """"Modelo de usuario"""
  name:str
  apellido:str
  cedula:int


class State(rx.State):
    users: list[User] = [
      User(
        name= "Julio",
        apellido= "Vergara",
        cedula=26554875,
      ),
      User(
        name="Maria",
        apellido="Rebolledo",
        cedula= 28024244,
      ),
    
    ]

def añadir_usuario (self, form_data: dict):
  self.users.apped(User(**form_data))

def mostrar_usuario (user: User):
  return rx.table.row(
    rx.table.cell(user.name),
    rx.table.cell(user.apellido),
    rx.table.cell(user.cedula)
  )


def formulario ():
  return rx.form(
    rx.vstack(
      rx.input(
        placeholder="Nombre",
        name="Nombre", 
        required= True,
      ),
      rx.input(
        placeholder="Apellido",
        name= "Apellido",
        required= True,
      ),
      rx.input(
        placeholder="Cedula",
        name = "Cedula",
        required= True,
      ), 
      rx.button("subir", type="submit"),
    ),
    on_submit= State.añadir_usuario,
  )

def index() -> rx.Component:
    return rx.table.root(
      rx.table.header(
        rx.table.row(
          rx.table.column_header_cell("Nombre"),
          rx.table.column_header_cell("Apellido"),
          rx.table.column_header_cell("Cedula"),
          
        ),
      ),
      
      rx.table.body(
          rx.foreach(State.users, mostrar_usuario),
      ),
      variant= "surface",
      size= "3"
        )
    
    rx.table.body



app = rx.App()
app.add_page(index)
