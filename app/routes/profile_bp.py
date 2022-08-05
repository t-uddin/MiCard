from flask import Blueprint
from controllers.profile_controller import get, store
from models.profile import Profile

profile = Profile


profile_bp = Blueprint('user_bp', __name__)

profile_bp.route('/profile-get', methods=['GET'])(get)
profile_bp.route('/adduser', methods=['GET'])(store)

# user_bp.route('/create', methods=['POST'])(store)
# user_bp.route('/<int:user_id>', methods=['GET'])(show)
# user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
# user_bp.route('/<int:user_id>', methods=['DELETE'])(delete)
