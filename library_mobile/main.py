# main.py  —  V = VIEW (the screen)
# The Model is models.py: the SAME file as Week 10.

import flet as ft
from models import Book


def main(page: ft.Page):
    page.title = "Library"
    page.appbar = ft.AppBar(
        title=ft.Text("Library"),
        bgcolor=ft.Colors.BLUE_100,
    )

    search_box = ft.TextField(
        label="Search title or author",
        prefix_icon=ft.Icons.SEARCH,
    )
    title_box = ft.TextField(label="Title")
    author_box = ft.TextField(label="Author")
    year_box = ft.TextField(label="Year", keyboard_type=ft.KeyboardType.NUMBER)
    book_list = ft.ListView(expand=True)

    def show_message(text):
        page.show_dialog(ft.SnackBar(ft.Text(text)))

    def show_books():
        book_list.controls.clear()
        if search_box.value:
            books = Book.search(search_box.value)
        else:
            books = Book.all()
        for b in books:
            book_list.controls.append(
                ft.ListTile(
                    title=ft.Text(b.title),
                    subtitle=ft.Text(f"{b.author} · {b.year}"),
                    trailing=ft.IconButton(
                        ft.Icons.DELETE,
                        data=b,
                        on_click=delete_clicked,
                    ),
                )
            )
        page.update()

    def save_clicked(e):
        book = Book(title_box.value, author_box.value, year_box.value)
        errors = book.validate()
        if errors:
            show_message(" ".join(errors))
            return
        book.save()
        title_box.value = ""
        author_box.value = ""
        year_box.value = ""
        show_message("Book added.")
        show_books()

    def delete_clicked(e):
        book = e.control.data
        book.delete()
        show_message("Book deleted.")
        show_books()

    def search_changed(e):
        show_books()

    search_box.on_change = search_changed

    page.add(
        search_box,
        title_box,
        author_box,
        year_box,
        ft.Button("Save", on_click=save_clicked),
        book_list,
    )
    show_books()


ft.run(main)
