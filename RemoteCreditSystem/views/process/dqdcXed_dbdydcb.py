# coding:utf-8
from flask import Module, session, request, render_template, redirect, url_for,flash

from RemoteCreditSystem import db
from RemoteCreditSystem.config import logger

from RemoteCreditSystem.models.credit_data.sc_co_borrower import SC_Co_Borrower
from RemoteCreditSystem.models.credit_data.sc_guaranty import SC_Guaranty
from RemoteCreditSystem.models.credit_data.sc_guarantees import SC_Guarantees
from RemoteCreditSystem.models.credit_data.sc_dydb_dec import SC_Dydb_Dec

from RemoteCreditSystem import app

# 贷款调查——小额贷款(担保抵押调查表)
@app.route('/Process/dqdc/dqdcXed_dbdydcb/<int:id>', methods=['GET'])
def dqdcXed_dbdydcb(id):
	co_borrower = SC_Co_Borrower.query.filter_by(loan_apply_id=id).all()
	guaranty = SC_Guaranty.query.filter_by(loan_apply_id=id).all()
	guarantees = SC_Guarantees.query.filter_by(loan_apply_id=id).all()

	dydb_dec = SC_Dydb_Dec.query.filter_by(loan_apply_id=id).first()

	return render_template("process/dqdc/dqdcXed_dbdydcb.html",id=id,co_borrower=co_borrower,guaranty=guaranty,
    	guarantees=guarantees,dydb_dec=dydb_dec)

# 贷款调查——编辑小额贷款(担保抵押调查表)
@app.route('/Process/dqdc/edit_dqdcXed_dbdydcb/<int:id>', methods=['POST'])
def edit_dqdcXed_dbdydcb(id):
	try:
		#保存共同借款人
		SC_Co_Borrower.query.filter_by(loan_apply_id=id).delete()
		db.session.flush()
		name_list = request.form.getlist('name')
		relationship_list = request.form.getlist('relationship')
		id_number_list = request.form.getlist('id_number')
		phone_list = request.form.getlist('phone')
		main_business_list = request.form.getlist('main_business')
		address_list = request.form.getlist('address')
		major_assets_list = request.form.getlist('major_assets')
		monthly_income_list = request.form.getlist('monthly_income')
		major_assets_list = request.form.getlist('major_assets')
		monthly_income_list = request.form.getlist('monthly_income')
		home_addr_list = request.form.getlist('home_addr')
		hj_addr_list = request.form.getlist('hj_addr')
		home_list = request.form.getlist('home')
		remark_list = request.form.getlist('remark')
		# 循环获取表单
		for i in range(len(name_list)):
			SC_Co_Borrower(id,name_list[i],relationship_list[i],
                id_number_list[i],phone_list[i],main_business_list[i],
                address_list[i],major_assets_list[i],monthly_income_list[i],
                home_addr_list[i],hj_addr_list[i],home_list[i],remark_list[i]).add()

		#保存担保信息
		SC_Guarantees.query.filter_by(loan_apply_id=id).delete()
		db.session.flush()
		name_db_list = request.form.getlist('name_db')
		address_db_list = request.form.getlist('address_db')
		id_number_db_list = request.form.getlist('id_number_db')
		workunit_db_list = request.form.getlist('workunit_db')
		phone_db_list = request.form.getlist('phone_db')
		relationship_db_list = request.form.getlist('relationship_db')
		major_assets_db_list = request.form.getlist('major_assets_db')
		monthly_income_db_list = request.form.getlist('monthly_income_db')
		home_addr_db_list = request.form.getlist('home_addr_db')
		hj_addr_db_list = request.form.getlist('hj_addr_db')
		home_db_list = request.form.getlist('home_db')
		remark_db_list = request.form.getlist('remark_db')
		# 循环获取表单
		for i in range(len(name_db_list)):
			SC_Guarantees(id,name_db_list[i],address_db_list[i],
                id_number_db_list[i],workunit_db_list[i],phone_db_list[i],
                relationship_db_list[i],major_assets_db_list[i],monthly_income_db_list[i],
                home_addr_db_list[i],hj_addr_db_list[i],home_db_list[i],remark_db_list[i]).add()

		#保存有无抵押物
		SC_Guaranty.query.filter_by(loan_apply_id=id).delete()
		db.session.flush()
		obj_name_list = request.form.getlist('obj_name')
		owner_address_list = request.form.getlist('owner_address')
		description_list = request.form.getlist('description')
		registration_number_list = request.form.getlist('registration_number')
		appraisal_list = request.form.getlist('appraisal')
		mortgage_list = request.form.getlist('mortgage')
		# 循环获取表单
		for i in range(len(obj_name_list)):
			SC_Guaranty(id,obj_name_list[i],owner_address_list[i],
				description_list[i],registration_number_list[i],appraisal_list[i],
				mortgage_list[i],0).add()

		dydb_dec = SC_Dydb_Dec.query.filter_by(loan_apply_id=id).first()
		if dydb_dec:
			dydb_dec.dec = request.form['dec']
		else:
			SC_Dydb_Dec(id,request.form['dec']).add()

		# 事务提交
		db.session.commit()
		# 消息闪现
		flash('保存成功','success')
	except:
		# 回滚
		db.session.rollback()
		logger.exception('exception')
		# 消息闪现
		flash('保存失败','error')

	return redirect('process/dqdc/dqdcXed_dbdydcb/%d' % id)