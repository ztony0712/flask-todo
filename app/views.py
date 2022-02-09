# this is the file for route and jump

from flask import render_template, request, redirect, url_for
from app import app, db
from datetime import datetime

from .model import Item
from .forms import ItemForm, TitleForm


@app.route("/")
def index():
    finished = Item.query.filter_by(complete=True).all()
    unfinished = Item.query.filter_by(complete=False).all()
    item_list = unfinished+finished
    form = ItemForm()
    return render_template("index.html", item_list=item_list, form=form)
# index page


@app.route("/add", methods=["POST"])
def add():
    form = TitleForm()

    if form.validate_on_submit():
        title = request.form.get("title")
        today = datetime.today()
        new_item = Item(title=form.title.data, complete=False,
                        date=today, code='', dcp='', total=1, step=1)
        db.session.add(new_item)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    return redirect(url_for("index"))
# add an item with title


@app.route("/update/<int:item_id>")
def update(item_id):
    item = Item.query.filter_by(id=item_id).first()
    result = item.total - item.step
    if result > 0:
        item.total = result
    else:
        item.total = 1
        item.step = 1
        item.complete = not item.complete
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    return redirect(url_for("index"))
# mark specified item to finished/unfinished


@app.route("/delete/<int:item_id>")
def delete(item_id):
    item = Item.query.filter_by(id=item_id).first()

    db.session.delete(item)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    return redirect(url_for("index"))
# delete specified item


@app.route("/edit/<int:item_id>")
def edit(item_id):
    item = Item.query.filter_by(id=item_id).first()
    form = ItemForm(obj=item)

    return render_template("description.html", item=item, form=form)
# jump to edit page of specified item


@app.route("/submit/<int:item_id>", methods=["POST"])
def submit(item_id):
    item = Item.query.filter_by(id=item_id).first()
    form = ItemForm(obj=item)

    if form.validate_on_submit():
        title = request.form.get("title")
        date = request.form.get("date")
        code = request.form.get("code")
        dcp = request.form.get("dcp")
        total = request.form.get("total")
        step = request.form.get("step")

        date = datetime.strptime(date, '%Y-%m-%d').date()
        item.date = date
        item.title = title
        item.code = code
        item.dcp = dcp
        item.total = total
        item.step = step

        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return redirect(url_for("index"))
    print(form.errors)
    return render_template("description.html", item=item, form=form)
# submit detail modification of item


@app.route("/rtn")
def rtn():
    return redirect(url_for("index"))
# return to index page


@app.route("/finished")
def finished():
    form = ItemForm()
    item_list = Item.query.filter_by(complete=True).all()
    return render_template("index.html", item_list=item_list, form=form)
# show all item finished


@app.route("/unfinished")
def unfinished():
    form = ItemForm()
    item_list = Item.query.filter_by(complete=False).all()
    return render_template("index.html", item_list=item_list, form=form)
# show all item unfinished
