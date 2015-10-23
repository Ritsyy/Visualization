from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from .VisualMozilla import *
import csv

# # Create your views here.

def home(request):
	data={}
	data["products"]="Firefox"
	# resultFirefox = postrequestsFirefox(data)
	data["products"]="Firefox for Android"
	# resultFirefoxForAndroid = postrequestsFirefoxForAndroid(data)
	data["products"]="Firefox OS"
	# resultFirefoxOS = postrequestsFirefoxOS(data)
	data["products"]="Firefox for iOS"
	# resultFirefoxForiOS = postrequestsFirefoxForiOS(data)
	# print my_list
	# with open("/home/richa/djangoprojects/VisualMozilla/src/static/static/data.csv", "wb") as f:
	#     writer = csv.writer(f)
	#     writer.writerows(my_list)
	return render_to_response("index.html",locals(),context_instance=RequestContext(request))