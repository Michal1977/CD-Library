from flask import Flask, request, render_template, redirect, url_for

from forms import LibraryForm
from models import cds

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/cd/", methods=["GET", "POST", "DELETE"])
def cd_list():
    form = LibraryForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            cds.create(form.data)
            cds.save_all()
        return redirect(url_for("cd_list"))

    return render_template("cds.html", form=form, cds=cds.all(), error=error)


@app.route("/cd/<int:cd_id>/", methods=["GET", "POST"])
def cd_details(cd_id):
    cd = cds.get(cd_id - 1)
    form = LibraryForm(data=cd)

    if request.method == "POST":
        if form.validate_on_submit():
            cds.update(cd_id - 1, form.data)
        return redirect(url_for("cd_list"))
    return render_template("cd.html", form=form, cd_id=cd_id)


if __name__ == "__main__":
    app.run(debug=True)
