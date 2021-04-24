# from app.api import bp
# from flask import jsonify, url_for, request
# from app.models import Place
# from app import db
# from app.api.errors import bad_request

# @bp.route('/places/<int:id>', methods=['GET'])

# def get_place(id):
#     return jsonify(Place.query.get_or404(id).to_dict())

# # @bp.route('/places', methods=['GET'])
# # def get_places():
# #     return jsonify(Place.query.all.to_dict)

# @bp.route('/places', methods=['POST'])
# def create_place():
#     try:
#         place = request.form.get('name')
#         db.session.add(place)
#         db.session.commit()
#         response = jsonify(place.to_dict())
#         response.status_code = 201
#         response.headers['Location'] = url_for('api.get_place', id=place.ide)
#         return response
#     except Exception:
#         error_code = 500
#         return render_template('error.html', page_title=error_code), error_code



# @bp.route('/places/<int:id>', methods=['PUT'])
# def update_place(id):
#     pass
