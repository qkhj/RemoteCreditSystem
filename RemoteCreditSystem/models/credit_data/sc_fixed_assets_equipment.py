#coding:utf-8
__author__ = 'Johnny'

from RemoteCreditSystem import db

# 固定资产详单-设备或器材
class SC_Fixed_Assets_Equipment(db.Model):
    '''
     固定资产详单-设备或器材
    '''
    __tablename__ = 'sc_fixed_assets_equipment'
    id = db.Column(db.Integer, primary_key=True)
    loan_apply_id=db.Column(db.Integer)
    name=db.Column(db.String(32))#设备名称
    # amount=db.Column(db.Integer)#数量
    # type_brand=db.Column(db.String(32))#型号或品牌
    purchase_date=db.Column(db.Date)#购置时间
    purchase_price=db.Column(db.String(32))#原始单价
    # production_date=db.Column(db.Date)#生产时间
    total_price= db.Column(db.String(32))#总价
    # price= db.Column(db.String(32))#折旧后价值
    # outward=db.Column(db.String(64))#外观评价
    # remark=db.Column(db.String(64))#备注
    rate =db.Column(db.String)#折旧率
    total =db.Column(db.String)#数量
    rate_price=db.Column(db.String)#折旧后价值


    def __init__(self,loan_apply_id,name,purchase_date,purchase_price,rate,total,total_price,
                 rate_price):
        self.loan_apply_id = loan_apply_id
        self.name = name
        self.purchase_date = purchase_date
        self.purchase_price = purchase_price
        self.total_price = total_price
        self.rate = rate
        self.total = total
        self.rate_price = rate_price


    def add(self):
        db.session.add(self)