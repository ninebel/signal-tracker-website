from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy 
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import datetime