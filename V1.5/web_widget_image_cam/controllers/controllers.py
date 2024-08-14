# # from odoo import http
# # from odoo.http import request, route
# # import json
#
# #
# # class MedicalEndoscopesController(http.Controller):
# #
# #     @route('/medical_endoscopes/save_video', type='json', auth='user')
# #     def save_video(self, recorded_data):
# #         medical_endoscopes_model = request.env['medical.endoscopes']
# #         medical_endoscopes_model._save_video(recorded_data)
# #         print("@@@@@@@@@@@@@@@@@")
# #         return {'success': True}
# import json
#
# import boto3
# from odoo import http, fields, models
# from werkzeug.utils import secure_filename
#
#
# class VideoController(http.Controller):
#     @http.route('/upload_video', type='http', auth="user", methods=['POST'], csrf=False)
#     def upload_video(self, **post):
#         env = http.request.env
#         record_id = post.get('record_id')
#         medical_record = env['medical.endoscopes'].sudo().browse(int(record_id))
#         medical_record.video_url = "Sakr A"
#         print("medical_record", medical_record.name)
#
#         # video_file = post.get('video')
#         # if video_file and record_id:
#         #     filename = secure_filename(video_file.filename)
#         #     # s3 = boto3.client('s3')
#         #     # bucket_name = 'your-bucket-name'
#         #     # object_name = f"videos/{filename}"
#         #     # s3.upload_fileobj(video_file, bucket_name, object_name)
#         #     # video_url = f'https://{bucket_name}.s3.amazonaws.com/{object_name}'
#         #     # print("@@@@@@@@@@video_url", video_url)
#         #     # Update the medical.endoscopes record
#         #     env = http.request.env
#         #     medical_record = env['medical.endoscopes'].sudo().browse(int(record_id))
#         #     print("medical_record",medical_record.name)
#         #     if medical_record:
#         #         medical_record.write({'video_url': video_url})
#         #         return http.request.make_response(json.dumps({"success": True, "video_url": video_url}),
#         #                                           headers=[('Content-Type', 'application/json')])
#         #     else:
#         #         return http.request.make_response(json.dumps({"success": False, "error": "Record not found"}),
#         #                                           headers=[('Content-Type', 'application/json')])
#         # return http.request.make_response(json.dumps({"success": False, "error": "No video found"}),
#         #                                   headers=[('Content-Type', 'application/json')])

# from odoo import http
# from odoo.http import request

# class MedicalEndoscopesController(http.Controller):
#     @http.route('/medical_endoscopes/', type='http', auth='user')
#     def downloadImage1(self):
#         # Dummy content (replace with your actual content)
#         dummy_content = b"This is a dummy file content."

#         # Create a response with the dummy content
#         response = request.make_response(dummy_content)
#         response.headers['Content-Disposition'] = 'attachment; filename=dummy.txt'
#         return response
