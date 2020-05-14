import sqlite3
from django.shortcuts import render
from libraryapp.models import Library
from ..connection import Connection


def library_list(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.name,
            l.address
        from libraryapp_library l
        """)

        libraries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            library = Library()
            library.id = row["id"]
            library.name = row["name"]
            library.address = row["address"]

            libraries.append(library)

    template_name = 'libraries/list.html'

    context = {
        'libraries': libraries
    }

    return render(request, template_name, context)