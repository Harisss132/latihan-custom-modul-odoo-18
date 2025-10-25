from odoo import models, fields

class PollQuestion(models.Model):
    _name = "poll.question"
    _description = "Poll Question"
    
    name = fields.Char(string="Question")
    description = fields.Text(string="Description")
    answer_id = fields.One2many(comodel_name="poll.answer", inverse_name="question_id", string="Answers")
    
class PollAnswer(models.Model):
    _name = "poll.answer"
    _description = "Poll Answer"
    
    name = fields.Char(string="Answer")
    count= fields.Integer(string="Vote Count")
    question_id = fields.Many2one(comodel_name="poll.question")