from flask import Flask, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('Final Model')