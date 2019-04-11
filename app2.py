import os

from flask import Flask, jsonify
from flask_compress import Compress
from flask_cors import CORS
from flask_queryinspect import QueryInspect

from controller.group_report_controller import group_report_app
from controller.pdf_controller import pdf_app
from controller.report_controller import report_app
from controller.report_view_controller import list_app
from flaskrun import flaskrun

application = Flask(__name__,
                    template_folder='templates', static_folder="static")

config_name = os.getenv('FLASK_CONFIGURATION', 'default')
# application.config['BUNDLE_ERRORS'] = True
# application.config['TEMPLATES_AUTO_RELOAD'] = True
application.config.from_pyfile('config.cfg', silent=True)
application.debug = False
CORS(application)
Compress(application)
qi = QueryInspect(application)


# compress = FlaskStaticCompress(application)
# csrf = SeaSurf(application)


# @application.errorhandler(404)
# def page_not_found(error):
#     """
#     Args:
#         error:
#     Returns:
#     """
#     application.logger.error('Page not found: %s', error)
#     print(error)
#     return render_template('404.htm', error=error), 404
#
#
# @application.errorhandler(500)
# def internal_server_error(error):
#     """
#
#     Args:
#         error:
#
#     Returns:
#
#     """
#     application.loggpdf_config = pdfkit.configuration(wkhtmltopdf="/opt/wkhtmltox/bin/wkhtmltopdf")
#     # pdf_config = pdfkit.configuration(wkhtmltopdf="/opt/wkhtmltox/bin/wkhtmltopdf")er.error('Server Error: %s', error)
#     print(error)
#     return render_template('500.htm', error=error), 500
#
#
# @application.errorhandler(Exception)
# def unhandled_exception(error):
#     """
#
#     Args:
#         error:
#
#     Returns:
#
#     """
#     application.logger.error('Unhandled Exception: %s', error)
#     print(error)
#     return render_template('500.htm', error=error), 500


@application.route('/')
def home():
    """

    Returns:

    """
    return jsonify({"Provided By": "Think Talent Services Pvt Ltd"})


@application.route('/favicon.ico')
def send_js():
    return ""


application.register_blueprint(report_app, url_prefix='/individual-report')
application.register_blueprint(group_report_app, url_prefix='/group-report')
application.register_blueprint(pdf_app, url_prefix='/pdf')
application.register_blueprint(list_app, url_prefix='/list')

if __name__ == '__main__':
    flaskrun(application)
