from flask import render_template
from . import main_bp  

@main_bp.route('/')
def main():
    return render_template('login.html')


@main_bp.route('/<page>')
def load_page(page):
    return render_template(f"{page}.html")

