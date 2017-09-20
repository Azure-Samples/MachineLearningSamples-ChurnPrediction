# This script generates the scoring and schema files
# necessary to opearaitonalize Churn Prediction
# Init and run functions
from azureml.api.schema.dataTypes import DataTypes
from azureml.api.schema.sampleDefinition import SampleDefinition
from azureml.api.realtime.services import generate_schema
import pandas

# Prepare the web service definition by authoring
# init() and run() functions. Test the fucntions
# before deploying the web service.
def init():
    from sklearn.externals import joblib

    # load the model file
    global model
    model = joblib.load('model.pkl')

def run(input_df):
    import json
    input_df_encoded = input_df

    input_df_encoded = input_df_encoded.drop('year', 1)
    input_df_encoded = input_df_encoded.drop('month', 1)
    input_df_encoded = input_df_encoded.drop('churn', 1)
    


    columns_encoded = ['age', 'annualincome', 'calldroprate', 'callfailurerate', 'callingnum',
       'customerid', 'monthlybilledamount', 'numberofcomplaints',
       'numberofmonthunpaid', 'numdayscontractequipmentplanexpiring',
       'penaltytoswitch', 'totalminsusedinlastmonth', 'unpaidbalance',
       'percentagecalloutsidenetwork', 'totalcallduration', 'avgcallduration',
       'churn', 'customersuspended_No', 'customersuspended_Yes',
       'education_Bachelor or equivalent', 'education_High School or below',
       'education_Master or equivalent', 'education_PhD or equivalent',
       'gender_Female', 'gender_Male', 'homeowner_No', 'homeowner_Yes',
       'maritalstatus_Married', 'maritalstatus_Single', 'noadditionallines_\\N',
       'occupation_Non-technology Related Job', 'occupation_Others',
       'occupation_Technology Related Job', 'state_AK', 'state_AL', 'state_AR',
       'state_AZ', 'state_CA', 'state_CO', 'state_CT', 'state_DE', 'state_FL',
       'state_GA', 'state_HI', 'state_IA', 'state_ID', 'state_IL', 'state_IN',
       'state_KS', 'state_KY', 'state_LA', 'state_MA', 'state_MD', 'state_ME',
       'state_MI', 'state_MN', 'state_MO', 'state_MS', 'state_MT', 'state_NC',
       'state_ND', 'state_NE', 'state_NH', 'state_NJ', 'state_NM', 'state_NV',
       'state_NY', 'state_OH', 'state_OK', 'state_OR', 'state_PA', 'state_RI',
       'state_SC', 'state_SD', 'state_TN', 'state_TX', 'state_UT', 'state_VA',
       'state_VT', 'state_WA', 'state_WI', 'state_WV', 'state_WY',
       'usesinternetservice_No', 'usesinternetservice_Yes',
       'usesvoiceservice_No', 'usesvoiceservice_Yes']
    
    for column_encoded in columns_encoded:
        if not column_encoded in input_df.columns:
            input_df_encoded[column_encoded] = 0

    columns_to_encode = ['customersuspended', 'education', 'gender', 'homeowner', 'maritalstatus', 'noadditionallines', 'occupation', 'state', 'usesinternetservice', 'usesvoiceservice']
    for column_to_encode in columns_to_encode:
        dummies = pandas.get_dummies(input_df[column_to_encode])
        one_hot_col_names = []
        for col_name in list(dummies.columns):
            one_hot_col_names.append(column_to_encode + '_' + col_name)
            input_df_encoded[column_to_encode + '_' + col_name] = 1
        input_df_encoded = input_df_encoded.drop(column_to_encode, 1)
    
    pred = model.predict(input_df_encoded)
    return json.dumps(str(pred[0]))

df = pandas.DataFrame(data=[[12,168147,0.06,0,4251078442,1,'Yes','Bachelor or equivalent','Male','Yes','Single',71,'\\N',0,7,96,'Technology Related Job',371,'WA',15,19,'No','No',0.82,5971,663,0,2015,1]], columns=['age' , 'annualincome' , 'calldroprate' , 'callfailurerate' , 'callingnum' , 'customerid' , 'customersuspended' , 'education' , 'gender' , 'homeowner' , 'maritalstatus' , 'monthlybilledamount' , 'noadditionallines' , 'numberofcomplaints' , 'numberofmonthunpaid' , 'numdayscontractequipmentplanexpiring' , 'occupation' , 'penaltytoswitch' , 'state' , 'totalminsusedinlastmonth' , 'unpaidbalance' , 'usesinternetservice' , 'usesvoiceservice' , 'percentagecalloutsidenetwork' , 'totalcallduration' , 'avgcallduration' , 'churn' , 'year' , 'month'])
df.dtypes
df

init()
input1 = pandas.DataFrame(data=[[12,168147,0.06,0,4251078442,1,'Yes','Bachelor or equivalent','Male','Yes','Single',71,'\\N',0,7,96,'Technology Related Job',371,'WA',15,19,'No','No',0.82,5971,663,0,2015,1]], columns=['age' , 'annualincome' , 'calldroprate' , 'callfailurerate' , 'callingnum' , 'customerid' , 'customersuspended' , 'education' , 'gender' , 'homeowner' , 'maritalstatus' , 'monthlybilledamount' , 'noadditionallines' , 'numberofcomplaints' , 'numberofmonthunpaid' , 'numdayscontractequipmentplanexpiring' , 'occupation' , 'penaltytoswitch' , 'state' , 'totalminsusedinlastmonth' , 'unpaidbalance' , 'usesinternetservice' , 'usesvoiceservice' , 'percentagecalloutsidenetwork' , 'totalcallduration' , 'avgcallduration' , 'churn' , 'year' , 'month'])
run(input1)

inputs = {"input_df": SampleDefinition(DataTypes.PANDAS, df)}
# The prepare statement writes the scoring file (main.py) and
# the scchema file (service_schema.json) the the output folder.
#prepare(run_func=run, init_func=init, input_types=inputs, )
generate_schema(run_func=run, inputs=inputs, filepath='service_schema.json')
print("Schema generated")
