from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import Bank
from . import db

main = Blueprint('main', __name__)

# Read all banks
@main.route('/')
def index():
    banks = Bank.query.all()
    banks_list = [{"id": bank.id, "name": bank.name, "location": bank.location} for bank in banks]
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        return jsonify(banks_list)
    return render_template('banks.html', banks=banks)

# Create a new bank
@main.route('/add_bank', methods=['GET', 'POST'])
def add_bank():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']

        new_bank = Bank(name=name, location=location)
        db.session.add(new_bank)
        db.session.commit()

        if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
            return jsonify({"message": "Bank added successfully"}), 201
        return redirect(url_for('main.index'))

    return render_template('add_bank.html')

# Read a specific bank
@main.route('/bank/<int:bank_id>')
def bank_detail(bank_id):
    bank = Bank.query.get_or_404(bank_id)
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        return jsonify({"id": bank.id, "name": bank.name, "location": bank.location})
    return render_template('bank_detail.html', bank=bank)


# Update a specific bank
@main.route('/edit_bank/<int:bank_id>', methods=['GET', 'POST'])
def edit_bank(bank_id):
    bank = Bank.query.get_or_404(bank_id)
    if request.method == 'POST':
        bank.name = request.form['name']
        bank.location = request.form['location']
        db.session.commit()
        
        if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
            return jsonify({"message": "Bank updated successfully"})
        return redirect(url_for('main.index'))
    return render_template('edit_bank.html', bank=bank)

# Delete a specific bank
@main.route('/delete_bank/<int:bank_id>', methods=['POST'])
def delete_bank(bank_id):
    bank = Bank.query.get_or_404(bank_id)
    db.session.delete(bank)
    db.session.commit()
    
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        return jsonify({"message": "Bank deleted successfully"})
    return redirect(url_for('main.index'))
