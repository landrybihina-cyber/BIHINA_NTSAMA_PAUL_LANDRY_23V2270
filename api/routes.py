from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file, jsonify
from api.app import db
from api.model import Student                        # CORR: 'from app.models' → 'from model' (fichier s'appelle model.py)
import pandas as pd
import numpy as np
import io


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    if not data or not isinstance(data, list):
        return jsonify({'error': 'Donnees invalides'}), 400

    count = 0
    for item in data:
        try:
            moy = float(item.get('moyenne', 0)) if item.get('moyenne') else None
            if moy is None:
                notes = []
                for k in ['note_math', 'note_info', 'note_anglais']:
                    val = item.get(k)
                    if val not in (None, ''):
                        notes.append(float(val))
                moy = round(sum(notes) / len(notes), 2) if notes else None

            student = Student(
                nom=item.get('nom', ''),
                prenom=item.get('prenom', ''),
                filiere=item.get('filiere', ''),
                niveau=item.get('niveau', 'L3'),
                note_math=float(item['note_math']) if item.get('note_math') else None,
                note_info=float(item['note_info']) if item.get('note_info') else None,
                note_anglais=float(item['note_anglais']) if item.get('note_anglais') else None,
                moyenne=moy
            )
            db.session.add(student)
            count += 1
        except Exception:
            continue

    db.session.commit()
    return jsonify({'message': f'{count} etudiant(s) enregistre(s) avec succes'})


@main.route('/liste')
def liste():
    search = request.args.get('search', '')
    if search:
        students = Student.query.filter(
            Student.nom.ilike(f'%{search}%') |
            Student.prenom.ilike(f'%{search}%') |
            Student.filiere.ilike(f'%{search}%')
        ).all()
    else:
        students = Student.query.all()
    return render_template('liste.html', students=students, search=search)


@main.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Etudiant supprime.', 'danger')
    return redirect(url_for('main.liste'))


@main.route('/stats')
def stats():
    students = Student.query.all()
    moyennes = [s.moyenne for s in students if s.moyenne is not None]

    if moyennes:
        arr = np.array(moyennes)
        stat = {
            'total':      len(students),
            'moyenne':    round(float(np.mean(arr)), 2),
            'ecart_type': round(float(np.std(arr)), 2),
            'minimum':    round(float(np.min(arr)), 2),
            'maximum':    round(float(np.max(arr)), 2),
            'mediane':    round(float(np.median(arr)), 2),
        }

        filieres = {}
        for s in students:
            filieres[s.filiere] = filieres.get(s.filiere, 0) + 1

        tranches = {'0-5': 0, '5-10': 0, '10-15': 0, '15-20': 0}
        for m in moyennes:
            if m < 5:      tranches['0-5']   += 1
            elif m < 10:   tranches['5-10']  += 1
            elif m < 15:   tranches['10-15'] += 1
            else:          tranches['15-20'] += 1

        niveaux = {}
        for s in students:
            niveaux[s.niveau] = niveaux.get(s.niveau, 0) + 1

    else:
        stat = {'total': len(students), 'moyenne': 0, 'ecart_type': 0,
                'minimum': 0, 'maximum': 0, 'mediane': 0}
        filieres, tranches, niveaux = {}, {}, {}

    return render_template(
        'stats.html',
        stat=stat,
        filieres=filieres,
        tranches=tranches,
        niveaux=niveaux,
        moyennes=moyennes
    )


@main.route('/export/csv')
def export_csv():
    students = Student.query.all()
    data = [{'nom': s.nom, 'prenom': s.prenom, 'filiere': s.filiere,
              'niveau': s.niveau, 'math': s.note_math, 'info': s.note_info,
              'anglais': s.note_anglais, 'moyenne': s.moyenne} for s in students]
    df = pd.DataFrame(data)
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name='etudiants.csv'
    )


@main.route('/export/excel')
def export_excel():
    students = Student.query.all()
    data = [{'nom': s.nom, 'prenom': s.prenom, 'filiere': s.filiere,
              'niveau': s.niveau, 'math': s.note_math, 'info': s.note_info,
              'anglais': s.note_anglais, 'moyenne': s.moyenne} for s in students]
    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Etudiants')
    output.seek(0)
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='etudiants.xlsx'
    )
