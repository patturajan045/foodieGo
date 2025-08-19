
from flask import session, render_template, redirect, url_for
from . import admin_Bp

@admin_Bp.route('/admin')
def admin_dashboard():
    user = session.get("user")

    
    if not user:
        return redirect(url_for("authBp.login"))  
    elif user.get("role") != "admin":
        return render_template("admin.html", is_admin=False)

    # If admin
    return render_template("admin.html", is_admin=True, name=user.get("name"), email=user.get("email"))


