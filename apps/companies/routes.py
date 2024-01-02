from flask.views import MethodView
from flask import jsonify, request
from apps import db
from apps.companies.models import Companies
class CompaniesAPIView(MethodView):
    def get(self):
        companies:list[Companies] = Companies.query.all()
        companies_data = [{'id': company.id, 'name': company.name, 'description': company.description} for company in companies]
        return jsonify(companies_data), 200
    def post(self):
        try:
            data = request.get_json()
            db.session.add(Companies(name=data['name'], description=data['description']))
            db.session.commit()
            db.session.close()
            return jsonify({'status': 'success','message': 'Company created successfully'}), 200
        except KeyError:
            return jsonify({'status': 'failed','message': 'Required fields missing'}), 400
    def put(self):
        try:
            data = request.get_json()
            company = Companies.query.filter_by(id=data['id']).first()
            company.name = data['name']
            company.description = data['description']
            db.session.commit()
            db.session.close()
            return jsonify({'status': 'success','message': 'Company updated successfully'}), 200
        except KeyError:
            return jsonify({'status': 'failed','message': 'Required fields missing'}), 400