from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy 
from functools import wraps
import yfinance as yf
from celery import Celery, Task, shared_task
from celery.schedules import crontab
import redis