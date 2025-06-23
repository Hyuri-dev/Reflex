"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from collections import Counter

import reflex as rx

from rxconfig import config

class User(rx.Model):
  """"Modelo de usuario"""
  name:str
  apellido:str
  cedula:int
  genero: str


class State(rx.State):
    users: list[User] = [
      User(
        name = "hyuri",
        apellido = "darko",
        cedula = 4545,
        genero = "Hombre"
      )
    ]
    users_for_graph: list[dict] = []
    
    def añadir_usuario (self, form_data: dict):
      self.users.append(User(**form_data))
      self.transform_data()
    
    def transform_data (self):
      contador_genero = Counter (
        user.gender for user in self.users
      )
      
      self.usuarios_grafico = [{
        "name": grupo_genero, "value": count 
      } for grupo_genero, count in gender.counts.items()]



def mostrar_usuario (user: User):
  return rx.table.row(
    rx.table.cell(user.name),
    rx.table.cell(user.apellido),
    rx.table.cell(user.cedula),
    rx.table.cell(user.genero),
  )



def formulario_modal () -> rx.Component:
  return rx.dialog.root(
    rx.dialog.trigger(
      rx.button(
        rx.icon("plus", size = 26),
        rx.text("Añadir Usuario" , size = "4"),
        style = {"_hover": rx.color("red", 6)},
        background = "violet",
      ),
      
    ),
    rx.dialog.content(
      rx.dialog.title(
        "Añadir Nuevo Usuario",
        ),
      rx.dialog.description(
      "Llene el formulario con los datos para agregar al usuario",
    ),
    rx.form(
      rx.flex(
            rx.input(
            placeholder="Nombre",
            name="Nombre", 
          ),
          rx.input(
            placeholder="Apellido",
            name= "Apellido",
          ),
          rx.input(
            placeholder="Cedula",
            name = "Cedula",
            required= True,
          ),
          rx.select(
            ["Hombre" , "Mujer"],
            placeholder = "hombre",
            name= "Genero"
          ),
          rx.flex(
            rx.dialog.close(
              rx.button(
                "Cancel",
                variant="soft",
                color_scheme="gray",
              ),
            ),
            rx.dialog.close(
              rx.button(
                "Añadir" , type = "submit"
              ),
            ),
            spacing= "3",
            justify = "end",
          ),
          direction = "column",
          spacing = "4"
        ),
        on_submit= State.añadir_usuario,
        reset_on_submit= True,
    ),
      max_width = "450px",
    ),         
  )

def grafico ():
  return rx.recharts.bar_chart(
    rx.recharts.bar (
      data_key = "value",
      stroke = rx.color ("yellow" , 9),
      fill = rx.color ("yellow" , 8)
    ),
    rx.recharts.x_axis(data_key = "name"),
    rx.recharts.y_axis (),
    data = State.usuarios_grafico,
    width = "100%",
    height = 250,
  )

def index() -> rx.Component:
    return rx.vstack(
      formulario_modal(),
      rx.table.root(
        rx.table.header(
          rx.table.row(
            rx.table.column_header_cell("Nombre"),
            rx.table.column_header_cell("Apellido"),
            rx.table.column_header_cell("Cedula"),
            rx.table.column_header_cell("Genero"),
            style = {"_hover": {"bg": rx.color("purple", 8)}},
            align = "center"
            ),
          ),
        
      rx.table.body(
          rx.foreach(State.users, mostrar_usuario),
      ),
      variant= "surface", 
      size= "3",
      width = "100%"
        ),
      grafico(),
    )



app = rx.App(
  theme = rx.theme (radius = "full" , accent_color ="grass"),
)
app.add_page(index,
              title = "Colums data app",
              description = "Ejemplo de columnas en reflex")
