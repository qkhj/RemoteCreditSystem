#coding:utf-8
# 系统管理
from RemoteCreditSystem.models.system.User import User
from RemoteCreditSystem.models.system.Role import Role
from RemoteCreditSystem.models.system.UserRole import UserRole
from RemoteCreditSystem.models.system.Rcs_Menu import Rcs_Menu
from RemoteCreditSystem.models.system.Rcs_Privilege import Rcs_Privilege
from RemoteCreditSystem.models.system_usage.Rcs_Application_Info import Rcs_Application_Info
from RemoteCreditSystem.models.system_usage.Rcs_Application_Advice import Rcs_Application_Advice
from RemoteCreditSystem.models.system_usage.Rcs_Customer_Information import Rcs_Customer_Information


#流程管理
from RemoteCreditSystem.models.process import SC_Loan_Apply
from RemoteCreditSystem.models.process import SC_Apply_Info
from RemoteCreditSystem.models.process import SC_Loan_Purpose
from RemoteCreditSystem.models.process import SC_Credit_History
from RemoteCreditSystem.models.process import SC_Guarantees_For_Others
from RemoteCreditSystem.models.process import SC_Riskanalysis_And_Findings