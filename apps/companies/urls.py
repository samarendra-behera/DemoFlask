from apps.companies import cbp

from apps.companies.routes import CompaniesAPIView

cbp.add_url_rule('/', view_func=CompaniesAPIView.as_view('companies'))