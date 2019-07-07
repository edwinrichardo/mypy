from flask import Blueprint, request, jsonify
import pandas as pd

servicesAPI = Blueprint("servicesAPI", __name__)


@servicesAPI.route("/get_maximum", methods=['GET', 'POST'])
def get_maximum():
    df = pd.read_csv("./Data/Complaint.csv")
    r = "Maximum is {}".format(df.Count.max())
    return r

