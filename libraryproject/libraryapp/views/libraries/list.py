import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Library
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def library_list(request):
    if request.method == 'GET':
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

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_library
            (
                name, address
            )
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['address']
                ))

        return redirect(reverse('libraryapp:libraries'))