#coding:utf-8
from RemoteCreditSystem import db
import datetime

from flask.ext.login import current_user

# 机构表----测试
class OrgTest(db.Model):
    __tablename__ = 'rcs_org_test'
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(255))
    companyAbbr = db.Column(db.String(255))
    contactPhone = db.Column(db.String(255))
    filingNumber = db.Column(db.String(255))
    companyAddress = db.Column(db.String(255))
    byCompanyCode = db.Column(db.String(255))

    def __init__(self,companyName,companyAbbr,contactPhone,filingNumber,companyAddress,byCompanyCode):
        self.companyName = companyName
        self.companyAbbr = companyAbbr
        self.contactPhone = contactPhone
        self.filingNumber = filingNumber
        self.companyAddress = companyAddress
        self.byCompanyCode = byCompanyCode
        
    def add(self):
        db.session.add(self)