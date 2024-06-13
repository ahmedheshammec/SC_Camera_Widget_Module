from odoo import api, fields, models, http, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import base64


import io
import zipfile





class MedicalEndoscopes(models.Model):
    # _inherit = 'medical.endoscopes'
    _name = 'medical.endoscopes'
    _description = 'Medical Endoscopes'

    name = fields.Char(string='Request Number', required=True, readonly=True, default=lambda self: _('New'), copy=False)

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    video = fields.Binary(string="Video")
    video_data = fields.Char(string="Video Data")


    def save_video(self, video_data):
        print("@@@@@@@@@@@@@_save_video", video_data)
        print("@@@@@@@@@@@@@record_id", )
        video_data_bytes = base64.b64decode(video_data)

        self.write({
            'video_data': 'Video Data Placeholder',  # You can replace this with relevant video metadata
            'video': base64.b64encode(video_data_bytes),  # Store binary data as base64 in the video field
        })

    img1 = fields.Binary(string="Image 1", )
    img2 = fields.Binary(string="Image 2", )
    img3 = fields.Binary(string="Image 3", )
    img4 = fields.Binary(string="Image 4", )
    img5 = fields.Binary(string="Image 5", )
    img6 = fields.Binary(string="Image 6", )
    img7 = fields.Binary(string="Image 7", )
    img8 = fields.Binary(string="Image 8", )
    img9 = fields.Binary(string="Image 9", )
    img10 = fields.Binary(string="Image 10", )
    img11 = fields.Binary(string="Image 11", )
    img12 = fields.Binary(string="Image 12", )
    img13 = fields.Binary(string="Image 13", )
    img14 = fields.Binary(string="Image 14", )
    img15 = fields.Binary(string="Image 15", )
    img16 = fields.Binary(string="Image 16", )
    img17 = fields.Binary(string="Image 17", )
    img18 = fields.Binary(string="Image 18", )
    img19 = fields.Binary(string="Image 19", )
    img20 = fields.Binary(string="Image 20", )
    img21 = fields.Binary(string="Image 21", )
    img22 = fields.Binary(string="Image 22", )
    img23 = fields.Binary(string="Image 23", )
    img24 = fields.Binary(string="Image 24", )
    img25 = fields.Binary(string="Image 25", )
    img26 = fields.Binary(string="Image 26", )
    img27 = fields.Binary(string="Image 27", )
    img28 = fields.Binary(string="Image 28", )
    img29 = fields.Binary(string="Image 29", )
    img30 = fields.Binary(string="Image 30", )
    img31 = fields.Binary(string="Image 31", )
    img32 = fields.Binary(string="Image 32", )
    img33 = fields.Binary(string="Image 33", )
    img34 = fields.Binary(string="Image 34", )
    img35 = fields.Binary(string="Image 35", )
    img36 = fields.Binary(string="Image 36", )
    img37 = fields.Binary(string="Image 37", )
    img38 = fields.Binary(string="Image 38", )
    img39 = fields.Binary(string="Image 39", )
    img40 = fields.Binary(string="Image 40", )
    img41 = fields.Binary(string="Image 41", )
    img42 = fields.Binary(string="Image 42", )
    img43 = fields.Binary(string="Image 43", )
    img44 = fields.Binary(string="Image 44", )
    img45 = fields.Binary(string="Image 45", )
    img46 = fields.Binary(string="Image 46", )
    img47 = fields.Binary(string="Image 47", )
    img48 = fields.Binary(string="Image 48", )
    img49 = fields.Binary(string="Image 49", )
    img50 = fields.Binary(string="Image 50", )
    img51 = fields.Binary(string="Image 51", )
    img52 = fields.Binary(string="Image 52", )
    img53 = fields.Binary(string="Image 53", )
    img54 = fields.Binary(string="Image 54", )
    img55 = fields.Binary(string="Image 55", )
    img56 = fields.Binary(string="Image 56", )
    img57 = fields.Binary(string="Image 57", )
    img58 = fields.Binary(string="Image 58", )
    img59 = fields.Binary(string="Image 59", )
    img60 = fields.Binary(string="Image 60", )
    img61 = fields.Binary(string="Image 61", )
    img62 = fields.Binary(string="Image 62", )
    img63 = fields.Binary(string="Image 63", )
    img64 = fields.Binary(string="Image 64", )
    img65 = fields.Binary(string="Image 65", )
    img66 = fields.Binary(string="Image 66", )
    img67 = fields.Binary(string="Image 67", )
    img68 = fields.Binary(string="Image 68", )
    img69 = fields.Binary(string="Image 69", )
    img70 = fields.Binary(string="Image 70", )
    img71 = fields.Binary(string="Image 71", )
    img72 = fields.Binary(string="Image 72", )
    img73 = fields.Binary(string="Image 73", )
    img74 = fields.Binary(string="Image 74", )
    img75 = fields.Binary(string="Image 75", )
    img76 = fields.Binary(string="Image 76", )
    img77 = fields.Binary(string="Image 77", )
    img78 = fields.Binary(string="Image 78", )
    img79 = fields.Binary(string="Image 79", )
    img80 = fields.Binary(string="Image 80", )
    img81 = fields.Binary(string="Image 81", )
    img82 = fields.Binary(string="Image 82", )
    img83 = fields.Binary(string="Image 83", )
    img84 = fields.Binary(string="Image 84", )
    img85 = fields.Binary(string="Image 85", )
    img86 = fields.Binary(string="Image 86", )
    img87 = fields.Binary(string="Image 87", )
    img88 = fields.Binary(string="Image 88", )
    img89 = fields.Binary(string="Image 89", )
    img90 = fields.Binary(string="Image 90", )
    img91 = fields.Binary(string="Image 91", )
    img92 = fields.Binary(string="Image 92", )
    img93 = fields.Binary(string="Image 93", )
    img94 = fields.Binary(string="Image 94", )
    img95 = fields.Binary(string="Image 95", )
    img96 = fields.Binary(string="Image 96", )
    img97 = fields.Binary(string="Image 97", )
    img98 = fields.Binary(string="Image 98", )
    img99 = fields.Binary(string="Image 99", )
    img100 = fields.Binary(string="Image 100", )
    # Check boxes #
    is_img1 = fields.Boolean(string="Is Image1", )
    is_img2 = fields.Boolean(string="Is Image2", )
    is_img3 = fields.Boolean(string="Is Image3", )
    is_img4 = fields.Boolean(string="Is Image4", )
    is_img5 = fields.Boolean(string="Is Image5", )
    is_img6 = fields.Boolean(string="Is Image 6", )
    is_img7 = fields.Boolean(string="Is Image 7", )
    is_img8 = fields.Boolean(string="Is Image 8", )
    is_img9 = fields.Boolean(string="Is Image 9", )
    is_img10 = fields.Boolean(string="Is Image 10", )
    is_img11 = fields.Boolean(string="Is Image 11", )
    is_img12 = fields.Boolean(string="Is Image 12", )
    is_img13 = fields.Boolean(string="Is Image 13", )
    is_img14 = fields.Boolean(string="Is Image 14", )
    is_img15 = fields.Boolean(string="Is Image 15", )
    is_img16 = fields.Boolean(string="Is Image 16", )
    is_img17 = fields.Boolean(string="Is Image 17", )
    is_img18 = fields.Boolean(string="Is Image 18", )
    is_img19 = fields.Boolean(string="Is Image 19", )
    is_img20 = fields.Boolean(string="Is Image 20", )
    is_img21 = fields.Boolean(string="Is Image 21", )
    is_img22 = fields.Boolean(string="Is Image 22", )
    is_img23 = fields.Boolean(string="Is Image 23", )
    is_img24 = fields.Boolean(string="Is Image 24", )
    is_img25 = fields.Boolean(string="Is Image 25", )
    is_img26 = fields.Boolean(string="Is Image 26", )
    is_img27 = fields.Boolean(string="Is Image 27", )
    is_img28 = fields.Boolean(string="Is Image 28", )
    is_img29 = fields.Boolean(string="Is Image 29", )
    is_img30 = fields.Boolean(string="Is Image 30", )
    is_img31 = fields.Boolean(string="Is Image 31", )
    is_img32 = fields.Boolean(string="Is Image 32", )
    is_img33 = fields.Boolean(string="Is Image 33", )
    is_img34 = fields.Boolean(string="Is Image 34", )
    is_img35 = fields.Boolean(string="Is Image 35", )
    is_img36 = fields.Boolean(string="Is Image 36", )
    is_img37 = fields.Boolean(string="Is Image 37", )
    is_img38 = fields.Boolean(string="Is Image 38", )
    is_img39 = fields.Boolean(string="Is Image 39", )
    is_img40 = fields.Boolean(string="Is Image 40", )
    is_img41 = fields.Boolean(string="Is Image 41", )
    is_img42 = fields.Boolean(string="Is Image 42", )
    is_img43 = fields.Boolean(string="Is Image 43", )
    is_img44 = fields.Boolean(string="Is Image 44", )
    is_img45 = fields.Boolean(string="Is Image 45", )
    is_img46 = fields.Boolean(string="Is Image 46", )
    is_img47 = fields.Boolean(string="Is Image 47", )
    is_img48 = fields.Boolean(string="Is Image 48", )
    is_img49 = fields.Boolean(string="Is Image 49", )
    is_img50 = fields.Boolean(string="Is Image 50", )
    is_img51 = fields.Boolean(string="Is Image 51", )
    is_img52 = fields.Boolean(string="Is Image 52", )
    is_img53 = fields.Boolean(string="Is Image 53", )
    is_img54 = fields.Boolean(string="Is Image 54", )
    is_img55 = fields.Boolean(string="Is Image 55", )
    is_img56 = fields.Boolean(string="Is Image 56", )
    is_img57 = fields.Boolean(string="Is Image 57", )
    is_img58 = fields.Boolean(string="Is Image 58", )
    is_img59 = fields.Boolean(string="Is Image 59", )
    is_img60 = fields.Boolean(string="Is Image 60", )
    is_img61 = fields.Boolean(string="Is Image 61", )
    is_img62 = fields.Boolean(string="Is Image 62", )
    is_img63 = fields.Boolean(string="Is Image 63", )
    is_img64 = fields.Boolean(string="Is Image 64", )
    is_img65 = fields.Boolean(string="Is Image 65", )
    is_img66 = fields.Boolean(string="Is Image 66", )
    is_img67 = fields.Boolean(string="Is Image 67", )
    is_img68 = fields.Boolean(string="Is Image 68", )
    is_img69 = fields.Boolean(string="Is Image 69", )
    is_img70 = fields.Boolean(string="Is Image 70", )
    is_img71 = fields.Boolean(string="Is Image 71", )
    is_img72 = fields.Boolean(string="Is Image 72", )
    is_img73 = fields.Boolean(string="Is Image 73", )
    is_img74 = fields.Boolean(string="Is Image 74", )
    is_img75 = fields.Boolean(string="Is Image 75", )
    is_img76 = fields.Boolean(string="Is Image 76", )
    is_img77 = fields.Boolean(string="Is Image 77", )
    is_img78 = fields.Boolean(string="Is Image 78", )
    is_img79 = fields.Boolean(string="Is Image 79", )
    is_img80 = fields.Boolean(string="Is Image 80", )
    is_img81 = fields.Boolean(string="Is Image 81", )
    is_img82 = fields.Boolean(string="Is Image 82", )
    is_img83 = fields.Boolean(string="Is Image 83", )
    is_img84 = fields.Boolean(string="Is Image 84", )
    is_img85 = fields.Boolean(string="Is Image 85", )
    is_img86 = fields.Boolean(string="Is Image 86", )
    is_img87 = fields.Boolean(string="Is Image 87", )
    is_img88 = fields.Boolean(string="Is Image 88", )
    is_img89 = fields.Boolean(string="Is Image 89", )
    is_img90 = fields.Boolean(string="Is Image 90", )
    is_img91 = fields.Boolean(string="Is Image 91", )
    is_img92 = fields.Boolean(string="Is Image 92", )
    is_img93 = fields.Boolean(string="Is Image 93", )
    is_img94 = fields.Boolean(string="Is Image 94", )
    is_img95 = fields.Boolean(string="Is Image 95", )
    is_img96 = fields.Boolean(string="Is Image 96", )
    is_img97 = fields.Boolean(string="Is Image 97", )
    is_img98 = fields.Boolean(string="Is Image 98", )
    is_img99 = fields.Boolean(string="Is Image 99", )
    is_img100 = fields.Boolean(string="Is Image 100", )




    def dowonloadAllImages(self):
        self.ensure_one()  # Ensures the method is called on a single record
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zip_file:
            for counter in range(1, 101):
                field_name = f'img{counter}'
                image_data = getattr(self, field_name)
                if image_data:
                    image_filename = f'{field_name}.jpg'
                    zip_file.writestr(image_filename, base64.b64decode(image_data))

        buffer.seek(0)
        zip_content = buffer.read()

        # Format the ID to be five digits long with leading zeros
        formatted_id = f'{self.id:05d}'
        zip_filename = f'MI-{formatted_id}.zip'

        # Create an attachment to hold the zip file
        attachment = self.env['ir.attachment'].create({
            'name': zip_filename,
            'type': 'binary',
            'datas': base64.b64encode(zip_content),
            'res_model': self._name,
            'res_id': self.id,
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': '_blank',
        }
        # return True

    doctor_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    operator = fields.Char(string="Operator")
    referred_by = fields.Many2many('res.partner.category', string="Referred By", related="patient_id.category_id",
                                   readonly=True)
    id_patient = fields.Char(string="ID")
    # age = fields.Integer(string="Age", related="patient_id.member_age")
    # birth_date = fields.Date(string="Date of Birth", related="patient_id.birth_date")
    date = fields.Datetime(string="Date", default=fields.Datetime.now)
    indications = fields.Text(string="Indication For Examination")
    procedures = fields.Char(string="Procedures")
    medications = fields.Char(string="Medications")
    findings = fields.Text(string="Findings")
    conclusions = fields.Text(string="Conclusions")
    recommendations = fields.Text(string="Recommendations")
    nurse = fields.Char(string="Nurse")
    nurse_assistant = fields.Char(string="Nursing assistant")
    patient_phone = fields.Char(string="Patient Phone", related="patient_id.phone", readonly=True)

    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    video_url = fields.Char(string='Video URL')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('medical.endoscopes') or _('New')
        return super(MedicalEndoscopes, self).create(vals_list)

    birth_date = fields.Date(string="Date of Birth", related="patient_id.birth_date")

    # Replace the age field with a computed one
    age = fields.Integer(string="Age", compute="_compute_age_from_birth_date")

    @api.depends('birth_date')
    def _compute_age_from_birth_date(self):
        for record in self:
            if record.birth_date:
                today = datetime.now().date()
                birth_date = fields.Date.from_string(record.birth_date)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0
