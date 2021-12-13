from flask import Blueprint

from app.controllers.captchas_controller import generate_captcha, validate_captcha

bp_captchas = Blueprint("bp_captchas", __name__, url_prefix="/captchas")

bp_captchas.post('/generate/<int:num_chars>')(generate_captcha)
bp_captchas.post('/validate')(validate_captcha)
